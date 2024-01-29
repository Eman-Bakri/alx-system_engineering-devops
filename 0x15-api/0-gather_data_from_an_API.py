#!/usr/bin/python3
"""script to return todo list progress based on employee ID."""
import requests as r
import sys

if __name__ == '__main__':
    link = 'https://jsonplaceholder.typicode.com/'
    user_id = r.get(link + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(link + 'todos', params={'userId': sys.argv[1]}).json()
    completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(user_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))
    [print("\t {}".format(title)) for title in completed]
