from socket import *
from time import time, ctime

# Server's IP Address and Port Number
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set the timeout for receiving data to 1 second
clientSocket.settimeout(1)

# Loop to send 10 ping messages
for i in range(1, 11):

    # Record the current time before sending the ping
    startTime = time()
    message = f"Ping {i} {startTime}"

    try:
        # Send the ping message to the server
        clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
        
        # Convert the start time to a human-readable format for logging
        timestamp = ctime(startTime)
        print(f"Sent Ping {i} at {timestamp} ")

        # Try to receive a response from the server
        # Buffer size is 4096 bytes
        modifiedMessage, serverAddress = clientSocket.recvfrom(4096)
        # Decode response from bytes to a string
        response = modifiedMessage.decode('utf-8')
        
        # Record the time after receiving the response
        endTime = time()
        # Calculate the Round-Trip Time (RTT)
        rtt = endTime - startTime
        
        # Print server's response and the RTT
        print(f"Received: {response}")
        print(f"RTT: {rtt} seconds\n")
        
    # When no response is received from the server within the timeout period
    except timeout:
        print(f"Ping {i}: Request timed out\n")

# Close the socket when all ping messages are sent
print("Closing Socket")
clientSocket.close()