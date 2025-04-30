from socket import *
from time import time, ctime

# Server's IP Address and Port Number
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set the timeout for receiving response to 1 second
clientSocket.settimeout(1)

# Store Round-Trip Time (RTT) values in a list
rttValues = []

# Counter for lost packets
lostPackets = 0

# Divider for sending ping requests
print("\n\n-------------- Sending Ping Requests --------------\n")

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
        rttValues.append(rtt)

        # Display server's response and the RTT
        print(f"Received: {response}")
        print(f"RTT: {rtt} seconds\n")

    # If no response is received from the server within the timeout period
    except timeout:

        # Increment any lost packet by 1
        lostPackets += 1
        print(f"Ping {i}: Request Timed Out\n")

# Close the socket when all ping messages are sent
print("\nClosing Socket")
clientSocket.close()

# Summary of ping statistics
print("\n----------------- Ping Statistics -----------------\n")
if rttValues:

    # Calculate the average RTT
    avg = sum(rttValues) / len(rttValues)

    # Display the minimum, maximum, and average of RTT
    print(f"Minimum RTT: {min(rttValues)} seconds")
    print(f"Maximum RTT: {max(rttValues)} seconds")
    print(f"Average RTT: {avg} seconds")

# If all pings timed out and no RTTs were recorded
else:
    print("No successful pings to calculate RTT statistics.")

# Calculate packet loss rate and display it
lossRate = (lostPackets / 10) * 100
print(f"Packet Loss Rate: {lossRate:.1f}%") 
print("\n---------------------------------------------------\n\n")