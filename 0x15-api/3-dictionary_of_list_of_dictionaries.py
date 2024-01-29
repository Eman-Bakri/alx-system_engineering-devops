#!/usr/bin/python3
"""Exports information of all employees in JSON format"""
import json
import requests

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/"
    users = requests.get(link + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(link + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
