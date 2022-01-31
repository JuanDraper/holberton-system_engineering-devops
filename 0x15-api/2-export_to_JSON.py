#!/usr/bin/python3
""" returns info about the TODO list of a given ID and exports
    it to json"""
import json
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/" +
                     sys.argv[1])
    d = json.loads(r.text)
    un = d.get('username')
    r = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                     "?userId=" + sys.argv[1])
    td = json.loads(r.text)
    ts = [task for task in td]
    ans = {sys.argv[1]: []}
    for task in ts:
        tdict = {"task": task.get('title'),
                 'completed': task.get('completed'), 'username': un}
        ans.get(sys.argv[1]).append(tdict)
        with open(sys.argv[1] + ".json", "w") as f:
            json.dump(ans, f)
