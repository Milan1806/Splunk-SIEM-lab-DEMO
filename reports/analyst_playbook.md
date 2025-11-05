# Analyst Playbook — Brute-force & Privilege Escalation (Demo)

## Objective
Triage and investigate alerts for brute-force and potential privilege escalation events.

## 1) Initial Triage (Brute-force alert)
- Review alert details: user, src_ip, host, time window, failure count.
- Check whether the IP is internal (RFC1918) or external. External IPs with high failures should be higher priority.
- Investigate recent successful logins from the same user or IP.

## 2) Investigation (Privilege Escalation)
- If a sudo event follows a successful login within a short window, confirm the user identity and reason for sudo.
- Check process command line in logs (if available) and asset owner.

## 3) Response Actions
- For confirmed malicious activity: block IP, reset account, enforce MFA, and escalate to incident response.
- For compromised accounts: rotate credentials and perform forensic snapshot of affected host.

## Notes
This is a demo playbook — adapt to your environment and policies.
