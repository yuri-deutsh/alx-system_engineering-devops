#!/usr/bin/python3
"""
Queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """returns number of total subscribers"""
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except ValueError:
        return 0


# Test the function with a valid subreddit
print(number_of_subscribers('python'))  # Should return the number of subscribers

# Test the function with an invalid subreddit
print(number_of_subscribers('invalidsubredditname12345'))  # Should return 0

