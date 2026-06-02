"""
Naver Search API: Batch Multi-Query Example
See more at: https://apify.com/johnvc/naver-search-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/naver-search-api/input-schema?fpr=9n7kx3

This script shows the batch capability of the Naver Search API on Apify: pass a
list of queries with the `queries` input and the Actor runs each one in a single
run, tagging every result row with the `query` it came from. That makes it easy
to compare brands, topics, or keywords side by side. Inputs are kept small so
your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from collections import defaultdict
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# This run uses the `queries` list to search several terms at once. Each row in
# the output carries the `query` it came from, so one run gives you comparable
# result sets. maxResultsPerQuery is kept small (5) to keep this first run cheap:
# you are billed per result row. Raise it, add more queries, or switch `where`
# to "nexearch", "web", "image", or "video" once you know your budget.
run_input = {
    "queries": ["삼성전자", "LG전자", "SK하이닉스"],  # batch: 3 Korean queries (electronics firms)
    "where": "news",            # nexearch | web | news | image | video
    "maxResultsPerQuery": 5,    # small on purpose to keep it cheap
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/naver-search-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} result row(s) across {len(run_input['queries'])} queries.\n")

# Group the results by their source query so the batch structure is visible.
by_query = defaultdict(list)
for item in items:
    by_query[item.get("query", "")].append(item)

# Print a short report per query.
for query in run_input["queries"]:
    rows = by_query.get(query, [])
    print(f"=== {query} ({len(rows)} result row(s)) ===")
    for item in rows:
        position = item.get("position")
        title = item.get("title", "")
        link = item.get("link", "")
        print(f"  {position}. {title}")
        print(f"     {link}")
    print()
