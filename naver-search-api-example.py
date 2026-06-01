"""
Naver Search API: A Quick Start Example
See more at: https://apify.com/johnvc/naver-search-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/naver-search-api/input-schema?fpr=9n7kx3

This script shows how to call the Naver Search API on Apify from Python and read
its structured JSON output. It searches Naver, South Korea's largest search
engine, and prints clean result rows. Inputs are kept small so your first call
stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one query, the web vertical, just 5 results) to keep
# this first run inexpensive: you are billed per result row. Raise
# maxResultsPerQuery, add more queries, or switch `where` to "nexearch",
# "news", "image", or "video" once you know your budget.
run_input = {
    "query": "서울 맛집",        # a query in Korean (Seoul restaurants)
    "where": "web",              # nexearch | web | news | image | video
    "maxResultsPerQuery": 5,     # small on purpose to keep it cheap
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/naver-search-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} result row(s).\n")

# Show a few key fields from each result.
for item in items:
    result_type = item.get("result_type")
    position = item.get("position")
    title = item.get("title", "")
    link = item.get("link", "")
    print(f"{position}. [{result_type}] {title}")
    print(f"   {link}\n")
