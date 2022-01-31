#!/usr/bin/python3
""" returns info about the TODO list of a given ID and exports
    it to json"""
import json
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/")
    d = json.loads(r.text)
    ans = {}
    for user in d:
        un = user.get('username')
        uId = str(user.get('id'))
        r = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                         "?userId=" + uId)
        td = json.loads(r.text)
        ts = [task for task in td]
        ans [uId] = []
        for task in ts:
            tdict = {"task": task.get('title'),
                     'completed': task.get('completed'),
                     'username': un}
            ans.get(uId).append(tdict)
    with open("todo_all_employees.json", "w") as f:
        json.dump(ans, f) 
