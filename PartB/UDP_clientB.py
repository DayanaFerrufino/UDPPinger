import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12000)
sock.settimeout(1.0)

# Part B stats
rtts = []
lost = 0

try:
    for i in range(1, 11):
        start = time.time()
        message = f"Ping {i} {start}"

        try:
        
            sock.sendto(message.encode('utf-8'), server_addr)
            # human-readable log
            hr_ts = time.ctime(start)
            print(f"Sent Ping {i} at {hr_ts}")
      
            data, _ = sock.recvfrom(4096)
            text = data.decode('utf-8')

            elapsed = time.time() - start
            rtts.append(elapsed)

            print(f"Received: {text}")
            print(f"RTT: {elapsed} seconds\n")

        except socket.timeout:
            lost += 1
            print("Request timed out\n")

finally:
    print("closing socket")
    sock.close()

# Part B summary
if rtts:
    print(f"Minimum RTT: {min(rtts)} seconds")
    print(f"Maximum RTT: {max(rtts)} seconds")
    avg = sum(rtts) / len(rtts)
    print(f"Average RTT: {avg} seconds")
else:
    print("No successful pings to calculate RTT statistics.")

loss_rate = (lost / 10) * 100
print(f"Packet loss rate: {loss_rate:.1f}%") 
