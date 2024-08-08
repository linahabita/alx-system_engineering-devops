#!/usr/bin/python3
"""
this module is for expermenting a fake API
"""
import json
import requests

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users/"

    users = requests.get(url)
    users_json = users.json()
    dict_data = {}

    for user in users_json:
        u_id = user['id']
        todos_url = (
                f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"
        )
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        dict_data[u_id] = []
        for task in todos_data:
            task_dict = {
                    "username": user['username'],
                    "task": task['title'],
                    "completed": task['completed']
            }
            dict_data[u_id].append(task_dict)

    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as file:
        json.dump(dict_data, file)
