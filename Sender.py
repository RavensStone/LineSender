# sender.py

import http.client
import http.client
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Send a file line by line to a server.')
parser.add_argument('file', type=str, help='The file to send line by line')
parser.add_argument('--ip', type=str, default='127.0.0.1', help='The server IP address (default is 127.0.0.1)')
parser.add_argument('--port', type=int, default=80, help='The server port (default is 80)')

args = parser.parse_args()

if not args.file:
    print("\nERROR: Missing required arguments.\n")
    print("Usage: python sender.py <file> [--ip <ip_address>] [--port <port>]\n")
    print("Where:")
    print("  <file>         = The file to send, line by line.")
    print("  --ip           = The server's IP address (default is 127.0.0.1)")
    print("  --port         = The server's port number (default is 5000)")
    sys.exit(1)

# Get the IP address, port, and file from the command line
ip_address = args.ip
port = args.port
file_path = args.file

# Open the file and read line by line
with open(file_path, 'r') as file:
    # Create an HTTP connection using the IP address and port
    conn = http.client.HTTPConnection(ip_address, port)
    headers = {'Content-type': 'text/plain'}

    for line in file:
        line = line.strip()  # Remove any extra whitespace or newline characters

        if line:  # Only send non-empty lines
            # Send the current line as a POST request
            conn.request("POST", "/receive", body=line, headers=headers)

            # Get the server's response
            response = conn.getresponse()
            print(f"Sent line: {line}")
            print(f"Response: {response.status}, {response.reason}")
            print(response.read().decode())  # Print the server's response

    conn.close()