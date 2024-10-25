#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "CustomUserAgent/0.1"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        if response.status_code != 200:
            print(None)
            return None

        data = response.json().get("data", {}).get("children", [])

        if not data:
            print(None)
            return None

        for post in data:
            print(post.get('data', {}).get('title'))

    except requests.RequestException:
        print(None)
