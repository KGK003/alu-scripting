import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    # Define the base URL for the Reddit API endpoint
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    
    # Set the headers to mimic a real user request (important to avoid being blocked)
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Send a GET request to the Reddit API
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the status code is 200, we can process the response
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response

            # Get the top 10 posts from the response
            posts = data.get('data', {}).get('children', [])
            for post in posts[:10]:  # Loop through the first 10 posts
                print(post['data']['title'])  # Print the title of each post

        else:
            # If the status code is not 200, it could mean the subreddit doesn't exist
            print(None)

    except requests.exceptions.RequestException:
        # Handle any request exceptions (e.g., network issues)
        print(None)

