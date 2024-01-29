#!/usr/bin/python3
"""script to return todo list progress based on employee ID."""
import requests as r
import sys

if __name__ == '__main__':
    link = 'https://jsonplaceholder.typicode.com/'
    empl_id = r.get(link + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(link + 'todos', params={'userId': sys.argv[1]}).json()
    is_done = [title.get("title") for title in to_do if
                 title.get('completed') is True]
    print(is_done)
    print("Employee {} is done with tasks({}/{}):".format(empl_id.get("name"),
                                                          len(is_done),
                                                          len(to_do)))
    [print("\t {}".format(title)) for title in completed]
