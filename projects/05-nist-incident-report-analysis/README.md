# 5. Incident Report Analysis (NIST CSF)

**Skills:** NIST Cybersecurity Framework · incident response · DoS · IDS/IPS · recovery planning

## Summary
A DoS attack (ICMP flood) took down internal network services for two hours. An unconfigured firewall allowed the attacker to flood the network with ICMP pings.

## NIST CSF breakdown
| Function | What I documented |
|---|---|
| **Identify** | Attacker exploited an unconfigured firewall to flood the network with ICMP packets. |
| **Protect** | Firewall rule to rate-limit ICMP; source IP verification to catch spoofed addresses; network monitoring software. |
| **Detect** | Network monitoring to baseline normal traffic and catch spikes; IDS/IPS to filter suspicious ICMP traffic. |
| **Respond** | Incident team blocked all incoming ICMP at the firewall and took non-critical services offline to focus on containment. |
| **Recover** | Restored critical services first, then phased recovery of core infrastructure; automated config backups; out-of-band IT updates; all-clear email to users. |

## Reflection
The incident exposed a gap in perimeter defense. Manual response contained the threat in two hours, but relying on reactive measures slows recovery and hurts productivity, so automation and monitoring are priorities.

📄 [Original report](original-report.pdf)
