#!/usr/bin/python3
"""
this module is for expermenting a fake API
"""
import json
import requests
import sys

if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json['name']
    user_name = response_json['username']

    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    json_file = f"{employee_id}.json"
    dict_data = {employee_id: []}
    for task in todos_data:
        task_dict = {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
        }
        dict_data[employee_id].append(task_dict)

    with open(json_file, 'w') as file:
        json.dump(dict_data, file)
