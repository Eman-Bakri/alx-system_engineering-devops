#!/usr/bin/python3
"""Function that print first 10 titles on a Reddit API"""

def top_ten(subreddit):
    """Print the 10 hottest posts titles."""
    import requests

    request_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if request_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in request_info.json().get("data").get("children")]
