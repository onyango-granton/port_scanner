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