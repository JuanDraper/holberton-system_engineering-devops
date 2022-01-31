#!/usr/bin/python3
""" returns info about the TODO list of a given ID """
import json
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/" +
                     sys.argv[1])
    d = json.loads(r.text)
    n = d.get('name')
    r = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                     "?userId=" + sys.argv[1])
    td = json.loads(r.text)
    ts = len(td)
    comp = [task for task in td if task.get('completed')]
    dn = len(comp)
    print("Employee {} is done with tasks({}/{}):".format(n, dn, ts))
    for task in comp:
        print("    ", task.get('title'))
