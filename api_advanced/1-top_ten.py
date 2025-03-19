#!/usr/bin/python3
"""
top_ten.py

This script queries the Reddit API to retrieve the titles of the first 10 hot posts
from a given subreddit. If the subreddit does not exist or there is a request error,
it prints None.

Usage:
    python3 1-main.py <subreddit>
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed
    for a given subreddit.

    Args:
        subreddit (str): The subreddit name to query.

    If the subreddit is invalid, it prints None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    # A more realistic User-Agent string to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        # Send the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        if response.status_code != 200:
            print(None)  # Invalid subreddit or other issues
        else:
            # If valid response, extract the posts and print the titles
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            # Print the titles of the first 10 posts
            for post in posts:
                print(post['data']['title'])

    except requests.exceptions.RequestException:
        print(None)  # In case of network-related or other exceptions

