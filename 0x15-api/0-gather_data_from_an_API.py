#!/usr/bin/python3
""" gather user todo from api"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).json()
    user_name = user.get("name")
    done_list = []
    for complete in todo:
        if complete.get("completed") is True:
            done_list.append(complete)
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, len(done_list), len(todo)))
    for done in done_list:
        print("\t {}".format(done.get("title")))
