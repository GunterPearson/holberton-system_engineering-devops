#!/usr/bin/python3
""" gather user todo from api"""
import requests
from sys import argv
import csv


if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()
    user_name = user.get("username")
    with open("{}.csv".format(user_id), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for ob in todo:
            writer.writerow([user_id, user_name, ob.get("completed"),
                            ob.get("title")])
