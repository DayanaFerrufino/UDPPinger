# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
from time import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

# Store delay values in a list
delayValues = []

# Counter for lost packets
lostPackets = 0

# Records the time when the first heartbeat is received 
timeoutStart = None

# Divider for recording heartbeat messages
print("\n\n---------------------- Heartbeat Monitor ---------------------\n")

while True:

    # Set the timeout for receiving message from client to 3 seconds
    serverSocket.settimeout(3)

    try:
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024) 

        # Records the time when the first heartbeat is received
        if timeoutStart is None:
            timeoutStart = time()

        # Decode heartbeat message
        num, times = message.decode('utf-8').split()
        
        # Parse the heartbeat message
        seqNum = int(num)
        timestamp = float(times)

        # Collect heartbeat details
        host = address[0]
        byte = len(message)
        delay = int((time() - timestamp) * 1000)
        delayValues.append(delay)

        # Generate random number in the range of 0 to 10 
        rand = random.randint(0, 10)

        # If rand is less is than 4, we consider the packet lost and do not respond
        if rand < 4:
            lostPackets += 1
            print(f"Request timed out for heartbeat {seqNum}")
        else:
            print(f"Received from {host}: bytes={byte} sequence number={seqNum} time={delay}ms")

    except timeout:

        # If no heartbeat is received from the client within the timeout period
        print("No heartbeat received in 1 second, client may have stopped")

        # Close the socket when more than 10 seconds have passed since the first heartbeat was received
        if timeoutStart and (time() - timeoutStart > 10):
            print("\n\nClosing Socket")
            serverSocket.close()
            break

        continue

# Summary of heartbeat statistics
print("\n-------------------- Heartbeat Statistics --------------------\n")
if delayValues:

    # Calculate the average delay
    avg = sum(delayValues) / len(delayValues)

    # Display the average delay
    print(f"Average Delay: {avg}ms")

# If all heartbeats timed out or lose and no delays were recorded
else:
    print("No successful heartbeats received")

# Calculate packet loss rate and display it
lossRate = (lostPackets / 10) * 100
print(f"Packet Loss Rate: {lossRate:.1f}%")
print("\n--------------------------------------------------------------\n\n")
