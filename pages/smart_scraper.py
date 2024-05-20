"""
Smart Scraper powered by Amazon Bedrock
https://scrapegraph-doc.onrender.com/docs/Graphs/smart_scraper_graph
"""

import streamlit as st

from helper import add_graph_config_settings
from scrapegraphai.graphs import SmartScraperGraph

st.set_page_config(page_title="Smart Scraper", page_icon="🥐")
st.markdown("""
### Smart Scraper

Comprehensive web scraping tool that automates the process of extracting information from web pages using a natural language model to interpret and answer prompts.
""")

# 0. Get user input
source = st.text_input(
    label="Link to scrape",
    value="https://perinim.github.io/projects"
)

prompt = st.text_area(
    label="Write the prompt",
    value="List me all the articles"
)

# 1. Define graph configuration
add_graph_config_settings()
graph_config = {
    "llm": {
        "model": f"bedrock/{st.session_state.llm}",
        "temperature": st.session_state.temperature
    },
    "embeddings": {
        "model": f"bedrock/{st.session_state.embedder}"
    }
}

# 2. Create the graph instance and run it
graph = SmartScraperGraph(
    prompt=prompt,
    source=source,
    config=graph_config
)

# 3. Scrape away!
def run():
    """Execute graph and return result"""
    with st.spinner("Running graph 🏃"):
        st.session_state.output = None
        try:
            st.session_state.output = graph.run()
        except Exception as ex:
            st.error(ex, icon="🚨")

run = st.button(
    label="Run",
    on_click=run,
    disabled=not prompt or not source
)

if st.session_state.get('output', None):
    st.write("### Output")
    st.write(st.session_state.output)
