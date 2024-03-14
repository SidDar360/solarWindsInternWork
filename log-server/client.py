import requests
import json

# Define the server URL
server_url = "http://127.0.0.1:5000/logs"  # Replace with actual server URL

# Specify the log file path
log_file_path = "logs.json"  # Replace with your actual log file path

# Load log lines from the file
with open(log_file_path, "r") as log_file:
    log_lines = json.load(log_file)  # Assuming JSON format

# Send each log line as a separate POST request
for log_line in log_lines:
    response = requests.post(server_url, json=log_line["message"])
    if response.status_code == 201:
        print("Log sent successfully")
    else:
        print(f"Error sending log: {response.status_code} - {response.text}")
