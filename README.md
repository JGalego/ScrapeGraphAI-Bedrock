### Amazon Bedrock 💖 ScrapeGraphAI

[ScrapeGraphAI](https://scrapegraphai.com/) is a python library that uses large language models(LLM) and direct graph logic to create scraping pipelines for websites, documents and XML files.

In these examples, we will show you how to integrate [Amazon Bedrock](https://aws.amazon.com/bedrock/) ⛰️ with ScrapeGraphAI to extract information from multiple sources using natural language prompts.

#### Instructions

0/ Set AWS credentials

	```bash
	export AWS_ACCESS_KEY_ID=...
	export AWS_SECRET_ACCESS_KEY=...
	export AWS_SESSION_TOKEN=...
	export AWS_DEFAULT_REGION=...
	```

1/ Install dependencies

	```bash
	pip install -r requirements.txt
	```

2a/ Run the application

	```bash
	streamlit run pages/scrapegraphai_bedrock.py
	```

2b/ Run a single demo

	```bash
	streamlit run pages/smart_scraper.py
	```

![](scrapegraphai_bedrock.gif)