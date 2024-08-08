#!/usr/bin/python3
"""
this module is for expermenting a fake API
"""
import csv
import requests
import sys

if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json['username']

    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    csv_file = f'{employee_id}.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow(
                    [employee_id,
                        employee_name,
                        task['completed'],
                        task['title']]
                    )

    print("data has been written")

