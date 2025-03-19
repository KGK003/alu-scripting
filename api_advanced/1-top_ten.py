#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    # More realistic User-Agent string to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for response status code
        if response.status_code != 200:
            print(None)  # Invalid subreddit or other issues
        else:
            # If the status code is 200, process the response
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            # Print the titles of the first 10 posts
            for post in posts:
                print(post['data']['title'])

    except requests.exceptions.RequestException:
        print(None)  # If a network or other exception occurs
