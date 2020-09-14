#!/usr/bin/python3
""" gather user todo from api"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    all_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    data = {}
    for user in all_user:
        user_id = user.get("id")
        user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(user_id)).json()
        todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user_id)).json()
        user_name = user.get("username")
        data_list = []
        for stuff in todo:
            data_object = {}
            data_object["task"] = stuff.get("title")
            data_object["completed"] = stuff.get("completed")
            data_object["username"] = user_name
            data_list.append(data_object)
        data[user_id] = data_list
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(data, json_file)
