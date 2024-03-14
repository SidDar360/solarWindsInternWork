from flask import Flask, request, jsonify

app = Flask(__name__)

# Define log file path
log_file = "logs.txt"

@app.route('/logs', methods=['POST'])
def receive_logs():
  print("Received a POST request to /logs")  # Added for debugging
  # Check if request is JSON
  if not request.is_json:
    return jsonify({'error': 'Request must be JSON'}), 400

  # Get the JSON data (assuming an array of log messages)
  data = request.get_json()

  # Open the log file in append mode
  with open(log_file, "a") as f:
    for log_line in data:
      # Write each log line to the file
    #   f.write(f"{log_line['message']}\n")
      f.write(f"{log_line}")
    f.write("\n")

  # Return a success response
  return jsonify({'message': 'Logs received'}), 201

if __name__ == '__main__':
  app.run(debug=True)
