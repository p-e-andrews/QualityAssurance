import requests
import pytest


presidents = ["Adams", "Arthur", "Biden", "Buchanan", "Bush", "Carter", "Cleveland", "Clinton", "Coolidge",
              "Eisenhower", "Fillmore", "Ford", "Garfield", "Grant", "Harding", "Harrison", "Hayes", "Hoover",
              "Jackson", "Jefferson", "Johnson", "Kennedy", "Lincoln", "Madison", "McKinley", "Monroe", "Nixon",
              "Obama", "Pierce", "Polk", "Reagan", "Roosevelt", "Taft", "Taylor", "Truman", "Trump", "Tyler", "Buren",
              "Washington", "Wilson"]   # Alphabetical, no duplicates == 40 names

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    resp_data = resp.json()
    assert "DuckDuckGo" in resp_data["Heading"]


def test_ddg1():
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json&pretty=1")
    resp_data = resp.json()
    ddg_related = resp_data["RelatedTopics"]    # list of RelatedTopics (dictionaries)
    ddg_text = ""   # faster than a list
    for i in ddg_related:
        text_field = i["Text"]
        ddg_text = ddg_text + text_field
    # tests that each president is present in the response
    for i in presidents:
        assert i in ddg_text

# Citations:
# https://www.loc.gov/rr/print/list/057_pral.html
# https://www.dataquest.io/blog/python-api-tutorial/
# https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json&pretty=1
# Senior Programmer C. Reinschild
# Professor Cindy Halliday
