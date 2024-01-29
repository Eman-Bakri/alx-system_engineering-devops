#!/usr/bin/python3
"""Exporting data in CSV format"""
import csv
import requests as r
import sys

if __name__ == "__main__":
    empl_id = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/"
    empl = r.get(link + "users/{}".format(user_id)).json()
    username = empl.get("username")
    to_do = r.get(link + "todos", params={"userId": empl_id}).json()

    with open("{}.csv".format(empl_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([empl_id, username, elm.get("completed"),
                          elm.get("title")]) for elm in to_do]
