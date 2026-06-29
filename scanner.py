import socket

# Ask the user for a target IP address or website
host = input("Enter an IP address or website: ")

# We are going to check port 80 (HTTP)
port = 80

# Create a TCP socket using IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wait at most 1 second for a response
sock.settimeout(1)

# Attempt to connect to the target and port
result = sock.connect_ex((host, port))

# Check whether the port is open
if result == 0:
    print(f"✅ Port {port} is OPEN")
else:
    print(f"❌ Port {port} is CLOSED")

# Close the socket
sock.close()