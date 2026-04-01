#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag

def request_wikipedia(url, params=None):
	HEADERS = { "User-Agent": "roads_to_philosophy/1.0 (42-school exercise)" }
	
	response = requests.get(url, params=params, headers=HEADERS, timeout=10)
	if response.status_code != 200:
		raise RuntimeError("Error: server returned a non-200 status code.")
	
	return BeautifulSoup(response.text, "html.parser")


def get_page_title(soup):
	title_tag = soup.find("h1", id="firstHeading")
	
	if not title_tag:
		raise RuntimeError("Error: unable to read page title.")
	title = title_tag.get_text(strip=True)
	if not title:
		raise RuntimeError("Error: page title is empty.")
	
	return title


def get_redirected_from_title(soup):
	redirected = soup.find("span", class_="mw-redirectedfrom")
	
	if not redirected:
		return None
	redirected_link = redirected.find("a")
	if not redirected_link:
		return None
	
	redirected_title = redirected_link.get_text(strip=True)
	return redirected_title or None


def is_valid_article_link(href):
	if not href or not href.startswith("/wiki/"):
		return False
	
	target = href[len("/wiki/"):]
	if not target:
		return False
	if ":" in target:
		return False
	
	return True


def is_in_italic(tag):
	return tag.find_parent(["i", "em"]) is not None


def get_first_valid_link_from_paragraph(paragraph):
	bracket_depth = 0

	for node in paragraph.descendants:
		if isinstance(node, NavigableString):
			for char in str(node):
				if char == "(":
					bracket_depth += 1
				elif char == ")" and bracket_depth > 0:
					bracket_depth -= 1
			continue

		if not isinstance(node, Tag) or node.name != "a":
			continue

		if bracket_depth > 0:
			continue

		if is_in_italic(node):
			continue

		href = node.get("href", "")
		if not is_valid_article_link(href):
			continue

		return href.split("#", 1)[0]

	return None


def get_first_valid_link_from_intro(soup):
	content = soup.find("main", id="content")
	if not content:
		return None

	for node in content.descendants:
		if not isinstance(node, Tag):
			continue

		if node.name == "h2":
			break

		if node.name != "p":
			continue

		if not node.get_text(" ", strip=True):
			continue

		link = get_first_valid_link_from_paragraph(node)
		if link:
			return link

	return None


def print_and_register_title(title, visited_titles, seen_titles):
	if title in seen_titles:
		print("It leads to an infinite loop !")
		return False
	
	visited_titles.append(title)
	seen_titles.add(title)
	print(title)
	
	return True


def main():
	if len(sys.argv) != 2:
		print("Error: invalid number of arguments.")
		sys.exit(1)

	request_value = sys.argv[1].strip()
	if not request_value:
		print("Error: empty request.")
		sys.exit(1)

	visited_titles = []
	seen_titles = set()

	try:
		current_soup = request_wikipedia("https://en.wikipedia.org/wiki/Special:Search", params={"search": request_value})

		while True:
			redirected_from = get_redirected_from_title(current_soup)
			if redirected_from:
				if not print_and_register_title(redirected_from, visited_titles, seen_titles):
					return

			current_title = get_page_title(current_soup)
			if not print_and_register_title(current_title, visited_titles, seen_titles):
				return

			if current_title.lower() == "philosophy":
				print(str(len(visited_titles)) + " roads from " + request_value + " to philosophy !")
				return

			next_link = get_first_valid_link_from_intro(current_soup)
			if not next_link:
				print("It leads to a dead end !")
				return

			current_soup = request_wikipedia("https://en.wikipedia.org" + next_link)

	except requests.RequestException:
		print("Error: unable to connect to Wikipedia.")
		sys.exit(1)
		
	except RuntimeError as runtime_error:
		print(str(runtime_error))
		sys.exit(1)
		
	except Exception:
		print("Error: unexpected failure during execution.")
		sys.exit(1)


if __name__ == "__main__":
	main()
