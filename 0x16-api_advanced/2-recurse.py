#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], a=""):
    """recursive function that queries the Reddit API and returns a
    list containing the titles"""

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/102.0.0.0 Safari/537.36'
            }
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    request = requests.get(url=url, headers=headers, allow_redirects=False)
    if request.status_code != 200:
        return None
    else:
        hot_list.extend(_titles_list(
            request.json().get('data').get('children')))
        a = request.json().get('data').get('after')
        if a is None:
            return hot_list
        return recurse(subreddit, hot_list, a)

def _titles_list(hot_list, titles=[]):
    """titles list of hot posts"""
    if len(hot_list) == 0:
        return titles
    else:
        titles.append(hot_list[0].get('data').get('title'))
        return _titles_list(hot_list[1:], titles)
