# 4. Cybersecurity Incident Report: DNS & ICMP Traffic Analysis

**Skills:** tcpdump · DNS · UDP · ICMP · root-cause analysis

## Summary
Customers reported they could not reach `yummyrecipesforme.com`. I analyzed a packet capture taken with **tcpdump**.

## Key findings
- The browser sent a **UDP** DNS query to the DNS server (`203.0.113.2`).
- The server returned an **ICMP** error: **`udp port 53 unreachable`**, first seen at timestamp `13:24:32.192571`.
- The failure repeated three times in a row.
- Port 53 is the standard DNS port, so no DNS service was accepting requests.

## Likely cause
The DNS service on the server was turned off, crashed, or blocked by a firewall, so the domain name could not be translated to an IP address.

## Investigation timeline
1. Customers reported the site was unreachable.
2. Analyst reproduced the error in a browser.
3. Analyst captured packets with tcpdump while reloading the page.
4. Logs revealed the ICMP port-unreachable errors.

📄 [Original report](original-report.pdf)
