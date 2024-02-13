#!/usr/bin/python3
"""Function return a list of all hot articles."""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Returns titles list of all hot artciles on a subreddit."""
    import requests

    request_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit), params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if request_info.status_code >= 400:
        return None

    title_list = hot_list + [child.get("data").get("title")
                        for child in request_info.json()
                        .get("data")
                        .get("children")]

    info = request_info.json()
    if not info.get("data").get("after"):
        return title_list

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
