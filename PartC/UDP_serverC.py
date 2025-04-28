# Heartbeat_server.py

import socket, time, random

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 12000))
server.settimeout(3.0) # to track whether the client has been missed for too long

while True: # will continue indefinitely 
    try:
        data, addr = server.recvfrom(1024)
    except socket.timeout:
        print("No heartbeat for 3 seconds: client may have stopped")
        continue

    seq_str, ts_str = data.decode('utf-8').split()
    seq = int(seq_str)
    sent_ts = float(ts_str)
    
    # Generate random number in the range of 0 to 10 
    rand = random.randint(0, 10)
    
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        print(f"Request timed out for heartbeat {seq}")
    else:
        delay_ms = int((time.time() - sent_ts) * 1000)
        byte_count = len(data)
        host = addr[0]
        print(f"Reply from {host}: bytes={byte_count} time={delay_ms}ms")
