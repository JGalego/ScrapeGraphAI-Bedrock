"""
JSON Scraper powered by Amazon Bedrock
https://scrapegraph-doc.onrender.com/docs/Graphs/json_scraper_graph
"""

from io import StringIO

import streamlit as st

from helper import add_graph_config_settings

from scrapegraphai.graphs import JSONScraperGraph

st.set_page_config(page_title="JSON Scraper", page_icon="🌸")
st.markdown("""
### JSON Scraper

Searches a JSON file for answers to a given prompt.
""")

# 0. Get user input
uploaded_file = st.file_uploader(
    label="Upload a file",
    type=['json']
)

prompt = st.text_area(
    label="Write the prompt",
    value="List me all questions and options in the math section, no answers."
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
if uploaded_file:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    source = stringio.read()
    graph = JSONScraperGraph(
        prompt=prompt,
        source=source,
        config=graph_config
    )

# 3. Scrape away!
def run():
    """Execute graph and return result"""
    st.session_state.output = None
    try:
        st.session_state.output = graph.run()
    except Exception as ex:
        st.error(ex, icon="🚨")

run = st.button(
    label="Run",
    on_click=run,
    disabled='graph' not in vars()
)

if st.session_state.get('output', None):
    st.write("### Output")
    st.write(st.session_state.output)
