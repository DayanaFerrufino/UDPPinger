## Group Members
- Chenilyn Espineda
- Dayana Ferrufino
- Nicole Balay

# Running the Complete UDP Pinger & Heartbeat Project

## Prerequisites
- Python 3.6+
- No external libraries required
- Repository cloned locally

## 1. Clone & Navigate
~~~bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>/410-Project
~~~

## 2. Part A: UDP Ping

1. **Start the server**  
   ~~~bash
   cd PartA
   python UDP_server.py
   ~~~
2. **Run the client** (in a second terminal)  
   ~~~bash
   cd PartA
   python UDP_client.py
   ~~~
3. **Verify output**  
   - `Sent Ping <n> at …` logs  
   - `Received: PING <n> …` echoes  
   - `RTT: …` times  
   - `Request timed out` for lost packets

![Screenshot 2025-04-30 112410](https://github.com/user-attachments/assets/847e3aea-2e50-4b4a-b28b-4049536cfbe9)

## 2. Part B: UDP Ping w/ Stats

1. **Start the server**  
   ~~~bash
   cd PartA
   python UDP_server.py
   ~~~
2. **Run the client** (in a second terminal)  
   ~~~bash
   cd PartA
   python UDP_client.py
   ~~~
3. **Verify output**  
   - `Sent Ping <n> at …` logs  
   - `Received: PING <n> …` echoes  
   - `RTT: …` times  
   - `Request timed out` for lost packets
  Stats at the ends
   - `Minimum RTT:` <value> seconds
   - `Maximum RTT:` <value> seconds
   - `Average RTT:` <value> seconds
   - `Packet loss rate:` <value>%

![Screenshot 2025-04-30 114453](https://github.com/user-attachments/assets/1f2bac6f-0869-4d9d-985b-10773c2b82b6)

