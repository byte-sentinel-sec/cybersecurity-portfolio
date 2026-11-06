# 1. Security Risk Assessment Report

**Skills:** risk assessment · network hardening · MFA · firewall configuration · password policy

## Scenario
A business network had weak security practices: shared passwords, a default database admin password, and no firewall rules limiting traffic. I selected three hardening measures to apply first and explained why they work.

## Recommended hardening measures
1. **Multi-Factor Authentication (MFA)**: enforced for all employee and administrator accounts.
2. **Firewall Access Control Lists (ACLs)**: strict rules to block unauthorized traffic entering or leaving the network.
3. **Password management & credential policy**: unique individual accounts (no sharing) and replace the default database admin password with a strong passphrase of 12+ characters mixing letters, numbers, and symbols.

## Why they are effective
- MFA and strong passwords stop credential-based attacks. Even if a password is stolen or guessed, the attacker cannot supply the second factor.
- Firewall rules create a barrier that stops attackers from scanning internal databases for weaknesses.

## Implementation frequency
| Control | Cadence |
|---|---|
| MFA | Always on, required at every login |
| Firewall rules | Audited and updated monthly to remove outdated rules |
| Admin passwords | Rotated every 60 days |

📄 [Original report](original-report.pdf)
