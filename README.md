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

![image](https://github.com/user-attachments/assets/f2ee68f6-77ca-4087-add8-20dc3faf944a)

