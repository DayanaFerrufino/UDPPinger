from socket import *
from time import time, ctime, sleep

# Server's IP Address and Port Number
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Interval between heartbeats is 1 second
interval = 1

# Divider for sending heartbeat
print("\n\n--------------- Sending Heartbeats ----------------\n")

for seqNum in range(1, 11):

    # Record the current time before sending the message
    timestamp = time()
    message = f"{seqNum} {timestamp}"
    
    # Send the heartbeat message to the server
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
    
    # Display sent message
    print(f"Sent heartbeat {seqNum} at {ctime(timestamp)}")
    sleep(interval)

# Close the socket when all ping messages are sent
print("\n\nClosing Socket")
print("\n---------------------------------------------------\n\n")
clientSocket.close()

