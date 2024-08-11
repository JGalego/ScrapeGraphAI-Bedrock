"""
Script Creator Scraper powered by Amazon Bedrock
https://scrapegraph-doc.onrender.com/docs/Graphs/script_creator_graph
"""

import streamlit as st

from pages.helper import add_graph_config_settings

from scrapegraphai.graphs import ScriptCreatorGraph

st.markdown("""
### Script Generator

Generates a web scraping script for a given framework/library.
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

st.session_state.library = st.text_input(
    label="Enter a library",
    value="beautifulsoup"
)

# 1. Define graph configuration
add_graph_config_settings()
graph_config = {
    "llm": {
        "model": f"bedrock/{st.session_state.llm}",
        "model_kwargs": {
            "temperature": st.session_state.temperature
        }
    },
    "embeddings": {
        "model": f"bedrock/{st.session_state.embedder}"
    },
    "library": st.session_state.library
}

# 2. Create the graph instance and run it
graph = ScriptCreatorGraph(
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
            st.session_state.script_generator_output = graph.run()
        except Exception as ex:
            st.error(ex, icon="🚨")

run = st.button(
    label="Run",
    on_click=run,
    disabled='graph' not in vars()
)

if st.session_state.get('script_generator_output', None):
    st.write("### Output")
    st.code(st.session_state.script_generator_output)
