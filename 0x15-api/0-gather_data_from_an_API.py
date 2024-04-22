#!/usr/bin/python3
"""returns information about his/her TODO list progress"""
import sys
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user_result = requests.get(url + "users/{}".format(sys.argv[1]))
    user = user_result.json()

    todos_result = requests.get(url + "todos", params={"userId": sys.argv[1]})
    todos = todos_result.json()
    completed = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} has completed {}/{} tasks:".format(user.get("name"),
        len(completed), len(todos)))
    for c in completed:
        print("\t{}".format(c))
