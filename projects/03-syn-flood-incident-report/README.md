# 3. Cybersecurity Incident Report: SYN Flood (DoS)

**Skills:** TCP/IP · log analysis · denial-of-service identification

## Problem
Visitors received a **connection timeout** error. A timeout occurs when a browser or gateway tries to reach a web server and gets no response within a set time.

## Finding
Network logs showed an abnormal, rapid spike of incoming SYN packets every second with no completed connections. **Likely cause: SYN flood attack (a type of DoS).**

## How the attack disrupts the site
**Normal TCP three-way handshake:**
1. Client sends **SYN** to the server
2. Server replies with **SYN-ACK**
3. Client replies with **ACK**, completing the connection

**During the attack:** the attacker sends thousands of SYN packets and never completes the handshake. The server reserves memory for each half-open connection, exhausting its resources until legitimate users cannot connect.

📄 [Original report](original-report.pdf)
