import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12000)
interval = 1.0 #seconds between heartbeats

try:
   
    for seq in range(1, 11):
        sent_ts = time.time()
        message = f"{seq} {sent_ts}"
        
        sock.sendto(message.encode('utf-8'), server_addr)
        
        print(f"Sent heartbeat {seq} at {time.ctime(sent_ts)}")
        time.sleep(interval)

finally:
    print("closing socket")
    sock.close()
