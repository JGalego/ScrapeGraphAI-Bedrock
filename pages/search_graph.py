"""
Search Graph powered by Amazon Bedrock
https://scrapegraph-doc.onrender.com/docs/Graphs/search_graph
"""

import streamlit as st

from pages.helper import add_graph_config_settings

from scrapegraphai.graphs import SearchGraph

st.markdown("""
### Search Graph

Searches the internet for answers to a given prompt.
""")

# 0. Get user input
prompt = st.text_area(
    label="Write the prompt",
    value="List me Chioggia's famous dishes."
)

st.session_state.search_engine = st.radio(
    label="Select search engine",
    options=["DuckDuckGo", "Google"]
)

st.session_state.max_results = st.slider(
    label="Choose the max number of search results",
    min_value=1,
    max_value=5,
    value=3
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
    "search_engine": st.session_state.search_engine,
    "max_results": st.session_state.max_results
}

# 2. Create the graph instance and run it
graph = SearchGraph(
    prompt=prompt,
    config=graph_config
)

# 3. Scrape away!
def run():
    """Execute graph and display results"""
    with st.spinner("Running graph 🏃"):
        st.session_state.output = None
        try:
            st.session_state.search_graph_output = graph.run()
        except Exception as ex:
            st.error(ex, icon="🚨")

run = st.button(
    label="Run",
    on_click=run,
    disabled=not prompt
)

if st.session_state.get('search_graph_output', None):
    st.write("### Output")
    st.write(st.session_state.search_graph_output)
