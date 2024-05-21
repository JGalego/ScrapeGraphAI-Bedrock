"""
Helper functions
"""

import streamlit as st

from scrapegraphai.helpers import models_tokens

@st.cache_data
def list_models():
    """
    Lists all Amazon Bedrock models supported by ScrapeGraphAI.
    """
    return list(models_tokens['bedrock'].keys())

def add_graph_config_settings():
    """
    Adds widgets for graph config settings.
    """
    models = list_models()
    embedders = sorted([model for model in models if "embed" in model])
    llms = sorted(list(set(models) - set(embedders)))

    st.session_state.llm = st.selectbox(
        label="Choose a model",
        options=llms,
        index=llms.index("anthropic.claude-3-sonnet-20240229-v1:0")
    )

    st.session_state.embedder = st.selectbox(
        label="Choose an embedder",
        options=embedders,
        index=embedders.index("cohere.embed-multilingual-v3")
    )

    with st.expander("Advanced Settings 📻"):
        st.session_state.temperature = st.slider(
            label="Pick a temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.0
        )
