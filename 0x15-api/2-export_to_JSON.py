#!/usr/bin/python3
"""Exporting in JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/"
    user = requests.get(link + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(link + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
