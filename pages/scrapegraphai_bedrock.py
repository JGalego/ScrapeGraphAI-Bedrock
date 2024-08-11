"""
ScrapeGraphAI with Amazon Bedrock
"""

import streamlit as st

st.markdown("""
### Amazon Bedrock 💖 ScrapeGraphAI

[ScrapeGraphAI](https://scrapegraphai.com/) is a python library that uses large language models(LLM) and direct graph logic to create scraping pipelines for websites, documents and XML files.

In these examples, we will show you how to integrate [Amazon Bedrock](https://aws.amazon.com/bedrock/) ⛰️ with ScrapeGraphAI to extract information from multiple sources using natural language prompts.
""")

# Add video
width = max(75, 0.01)
side = max((100 - width) / 2, 0.01)
_, container, _ = st.columns([side, width, side])
container.video("https://youtu.be/ljoY1W6gPnY")
