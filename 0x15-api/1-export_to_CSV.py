#!/usr/bin/python3
""" returns info about the TODO list of a given ID
    and exportis it to CSand exportis it to CSV"""
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
    with open(sys.argv[1] + ".csv", "w") as f:
        for task in ts:
            data = ['"' + sys.argv[1] + '"', '"' + un + '"', '"' +
                    str(task.get('completed')) + '"', '"' + task.get('title') +
                    '"']
            f.write(",".join(data) + '\n')
