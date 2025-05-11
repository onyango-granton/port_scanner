import pyfiglet
import sys
import socket
from datetime import datetime

# Generate and display an ASCII art banner for the port scanner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Check if the user provided exactly one argument (the target IP address or hostname)
if len(sys.argv) == 2:
    # Resolve the hostname to an IPv4 address
    target = socket.gethostbyname(sys.argv[1])
else:
    # Exit the program with an error message if no argument is provided
    sys.exit("Program needs an IP ADDR argument \npython main.py 0.0.0.0")

# Display a message indicating the start of the scanning process with the target and current timestamp
print("Scanning {} started at: {}".format(target, datetime.now()))

try:
    # Iterate through all possible ports (1 to 65534)
    for port in range(1, 65535):
        # Create a socket object for IPv4 and TCP connections
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        socket.setdefaulttimeout(1)

        # Attempt to connect to the target on the specified port
        result = s.connect_ex((target, port))
        # If the connection is successful (result is 0), the port is open
        if result == 0:
            print("Port {} is open".format(port))
        # Close the socket after checking the port
        s.close()