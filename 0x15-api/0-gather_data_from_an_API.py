#!/usr/bin/python3
"""
this module is for expermenting a fake API
"""
import requests
import sys

if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json['name']

    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks("
        f"{done_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task['title']}")
