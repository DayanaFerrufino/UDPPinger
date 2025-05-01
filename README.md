### Group Members
- Chenilyn Espineda
- Dayana Ferrufino
- Nicole Balay

# Running the Complete UDP Pinger & Heartbeat Project

## Prerequisites
- Python 3.6+
- No external libraries required
- Repository cloned locally

## Clone & Navigate
~~~bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>/410-Project
~~~

## Part A: UDP Pinger

1. **Start the server**  
   ~~~bash
   cd PartA
   python UDP_serverA.py
   ~~~
2. **Run the client** (in a second terminal)  
   ~~~bash
   cd PartA
   python UDP_clientA.py
   ~~~
3. **Verify output**  

   ****Successful Response****
   ~~~
   Sent Ping <sequence number> at <date & time>  
   Received: PING <sequence number & timestamp>  
   RTT: <round trip time> seconds
   ~~~

   ****Timed-Out Response****
   ~~~
   Sent Ping <sequence number> at <date & time>  
   Ping <sequence number>: Request Timed Out
   ~~~


![Screenshot 2025-04-30 112410](https://github.com/user-attachments/assets/847e3aea-2e50-4b4a-b28b-4049536cfbe9)

## Part B: UDP Pinger with Stats

1. **Start the server**  
   ~~~bash
   cd PartB
   python UDP_serverB.py
   ~~~
2. **Run the client** (in a second terminal)  
   ~~~bash
   cd PartB
   python UDP_clientB.py
   ~~~
3. **Verify output**  
   
   ****Successful Response****
   ~~~
   Sent Ping <sequence number> at <date & time>  
   Received: PING <sequence number & timestamp>  
   RTT: <round trip time> seconds
   ~~~

   ****Timed-Out Response****
   ~~~
   Sent Ping <sequence number> at <date & time>  
   Ping <sequence number>: Request Timed Out
   ~~~
   
   ****Statistics at the End****
   ~~~
   Minimum RTT: <value> seconds
   Maximum RTT: <value> seconds
   Average RTT: <value> seconds
   Packet loss rate: <value>%
   ~~~


![Screenshot 2025-04-30 114453](https://github.com/user-attachments/assets/1f2bac6f-0869-4d9d-985b-10773c2b82b6)


## Part C: UDP Heartbeat

1. **Start the server**  
   ~~~bash
   cd PartC
   python UDP_serverC.py
   ~~~
2. **Run the client** (in a second terminal)  
   ~~~bash
   cd PartC
   python UDP_clientC.py
   ~~~
3. **Verify output**  
   
   ****Successful Heartbeat Received****
   ~~~
   Received from <client IP>: bytes=<size> sequence number=<number> time=<delay>ms
   ~~~

   ****Packet Loss****
   ~~~
   Request timed out for heartbeat <sequence number>
   ~~~

   ****No Heartbeat Message Received****
   ~~~
   No heartbeat received in 1 second, client may have stopped
   ~~~

   ****Statistics at the End****
   ~~~
   Average Delay: <value>ms
   Packet Loss Rate: <value>%
   ~~~

![Screenshot 2025-04-30 114453](https://github.com/user-attachments/assets/1f2bac6f-0869-4d9d-985b-10773c2b82b6)