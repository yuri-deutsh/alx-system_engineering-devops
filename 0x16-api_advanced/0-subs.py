#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("Invalid subreddit")
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)
    
    # Print the status code for debugging
    print("Status code:", response.status_code)

    if response.status_code != 200:
        return 0

    try:
        results = response.json()
        # Print the JSON response for debugging
        print("Response JSON:", results)
        return results['data']['subscribers']
    except (ValueError, KeyError) as e:
        print("Error:", e)
        return 0

