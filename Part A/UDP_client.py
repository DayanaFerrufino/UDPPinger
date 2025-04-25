import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12000)
sock.settimeout(1.0)

try:
    for i in range(1, 11):
        start = time.time()
        message = f"Ping {i} {start}"

        try:
            sent = sock.sendto(message.encode('utf-8'), server_addr)
           
            # human‐readable time for our logs
            hr_ts = time.ctime(start)
            print(f"Sent Ping {i} at {hr_ts}  (raw: {start:.6f})")

            data, _ = sock.recvfrom(4096)
            text = data.decode('utf-8')
            elapsed = time.time() - start
            print(f"Received: {text}")
            print(f"RTT: {elapsed:.4f} seconds\n")
        except socket.timeout:
            print(f"Ping {i}: Request timed out\n")

finally:
    print("closing socket")
    sock.close()
