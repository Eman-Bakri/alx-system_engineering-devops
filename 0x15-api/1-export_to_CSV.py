#!/usr/bin/python3
"""Exporting data in CSV format"""
import csv
import requests as r
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/"
    usr = r.get(link + "users/{}".format(user_id)).json()
    username = usr.get("username")
    to_do = r.get(link + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, elm.get("completed"),
                          elm.get("title")]) for elm in to_do]
