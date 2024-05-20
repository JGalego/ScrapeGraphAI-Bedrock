"""
ScrapeGraphAI with Amazon Bedrock
"""

import streamlit as st

from st_pages import Page, show_pages

# Add home page info
st.set_page_config(page_title="ScrapeGraphAI / Amazon Bedrock", page_icon="⛰️")
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

# Display pages
show_pages([
    Page("pages/scrapegraphai_bedrock.py", "Home", "🏠"),
    Page("pages/smart_scraper.py", "Smart Scraper", "🥐"),
    Page("pages/json_scraper.py", "JSON Scraper", "🌸"),
    Page("pages/csv_scraper.py", "CSV Scraper", "🍴"),
    Page("pages/script_generator.py", "Script Generator", "👨‍💻"),
    Page("pages/search_graph.py", "Search Graph", "🔎"),
    Page("pages/xml_scraper.py", "XML Scraper", "🧾")
])