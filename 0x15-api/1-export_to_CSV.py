#!/usr/bin/python3
"""1. Export to CSV """
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    
    user_id = int(sys.argv[1])
    user = requests.get(url + "/users/{}".format(user_id))
    name = user.json().get('username')
    todos = requests.get(url + '/todos')
    file_name = sys.argv[1] + '.csv'

    with open(file_name, mode='w') as f:
        w = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
        for todo in todos.json():
            if todo.get('userId') == user_id:
                w.writerow([user_id, name, str(todo.get('completed')),
                                todo.get('title')])
