### Amazon Bedrock 💖 ScrapeGraphAI

[ScrapeGraphAI](https://scrapegraphai.com/) is a python library that uses large language models(LLM) and direct graph logic to create scraping pipelines for websites, documents and XML files.

In these examples, we will show you how to integrate [Amazon Bedrock](https://aws.amazon.com/bedrock/) ⛰️ with ScrapeGraphAI to extract information from multiple sources using natural language prompts.

#### Instructions

1. Set AWS credentials

    ```bash
    # Option 1: (recommended) AWS CLI
    aws configure

    # Option 2: environment variables
    export AWS_ACCESS_KEY_ID=...
    export AWS_SECRET_ACCESS_KEY=...
    export AWS_SESSION_TOKEN=...
    export AWS_DEFAULT_REGION=...
    ```

2. Install dependencies

    ```bash
    # Install Python packages
    pip install -r requirements.txt

    # Install browsers
    # https://playwright.dev/python/docs/browsers#install-browsers
    playwright install

    # Install system dependencies
    # https://playwright.dev/python/docs/browsers#install-system-dependencies
    playwright install-deps
    ```

3. Start the demo application

    ```bash
    # Run the full application
    streamlit run pages/scrapegraphai_bedrock.py

    # or just a single demo
    streamlit run pages/smart_scraper.py
    ```

![](scrapegraphai_bedrock.gif)