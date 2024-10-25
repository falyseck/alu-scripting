#!/usr/bin/python3
"""
1-top_ten
This module contains a function to query the Reddit API
and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, prints None.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data', {}).get('children', [])
    if not posts:
        print(None)
        return

    for post in posts[:10]:
        print(post['data']['title'])
    
    return "OK"  # Return "OK" after printing titles
