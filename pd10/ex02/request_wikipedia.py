#!/usr/bin/env python3

import requests
import sys
import dewiki

def build_filename(query):
    cleaned = "_".join(query.split())
    return cleaned + ".wiki"

def request_wikipedia_api(params):
    API_URL = "https://en.wikipedia.org/w/api.php"
    HEADERS = { "User-Agent": "request_wikipedia/1.0 (42-school exercise)" }
    
    response = requests.get(API_URL, params=params, headers=HEADERS, timeout=10)
    if response.status_code != 200:
        raise RuntimeError("Wikipedia API returned a non-200 status code.")
    return response.json()

def find_best_title(query):
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "srlimit": 1,
        "format": "json",
    }
    data = request_wikipedia_api(params)
    search_data = data.get("query", {}).get("search", [])
    if not search_data:
        raise RuntimeError("No result found for this request.")
    return search_data[0].get("title")

def fetch_wiki_content(title):
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "rvslots": "main",
        "titles": title,
        "format": "json",
    }
    data = request_wikipedia_api(params)
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        raise RuntimeError("No page data found in API response.")

    page = next(iter(pages.values()))
    revisions = page.get("revisions")
    if not revisions:
        raise RuntimeError("No content found for this page.")

    raw = revisions[0].get("slots", {}).get("main", {}).get("*")
    if not raw:
        raise RuntimeError("Page content is empty.")

    plain_text = dewiki.from_string(raw).strip()
    if not plain_text:
        raise RuntimeError("Content could not be converted to plain text.")
    return plain_text

def main():
    if len(sys.argv) != 2:
        print("Error: invalid number of arguments.")
        sys.exit(1)

    query = sys.argv[1].strip()
    if not query:
        print("Error: empty request.")
        sys.exit(1)

    filename = build_filename(query)

    try:
        title = find_best_title(query)
        content = fetch_wiki_content(title)

        with open(filename, "w", encoding="utf-8") as output_file:
            output_file.write(content)
    except requests.RequestException:
        print("Error: unable to contact Wikipedia API.")
        sys.exit(1)
    except (RuntimeError, ValueError, KeyError):
        print("Error: unable to retrieve valid Wikipedia content.")
        sys.exit(1)
    except OSError:
        print("Error: unable to write output file.")
        sys.exit(1)

if __name__ == '__main__':
    main()