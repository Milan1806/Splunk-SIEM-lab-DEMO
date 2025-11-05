# SIEM Threat Detection Lab (Splunk) — Demo (Synthetic)

**Overview — friendly, human tone**  
This is a **safe, synthetic demo** of a SIEM threat detection lab built around Splunk-style artifacts. I created this repository to demonstrate how I would design detections and dashboards for common attacks such as brute-force login attempts and privilege escalation. Everything here is synthetic — no real logs, credentials, or sensitive data are included. Use it as a portfolio piece or a learning aid.

**Why this project**  
Detecting brute-force and privilege-escalation activity is fundamental for protecting systems. This demo shows a practical pipeline: generate logs, write SPL detection queries, visualize alerts on dashboards, and produce a short analyst playbook for investigation and response.

**What's included**  
- `data/` — synthetic syslog/auth logs (CSV) simulating failed/successful logins and sudo or admin privilege events.  
- `queries/` — example Splunk SPL correlation searches for brute-force and privilege escalation detections.  
- `dashboards/` — simplified JSON snippets and screenshots for dashboards (visuals only).  
- `scripts/` — Python scripts to generate synthetic logs and aggregate metrics.  
- `reports/` — a sample analyst playbook and short executive summary.  
- `images/` — PNG images: dashboard mockups and example charts.

**Key demo outcomes (synthetic)**  
- Identified simulated brute-force clusters using a threshold/aggregation approach.  
- Flagged potential privilege escalation events by correlating successful logins with subsequent sudo/admin events from the same host/user.  
- Provided sample SPL and dashboard visualizations to help triage and accelerate analyst response.

**How to use**  
1. Review `scripts/generate_synthetic_logs.py` to see the log schema and generation method.  
2. Open `data/auth_logs.csv` to inspect the synthetic events.  
3. Load the SPL queries in `queries/` into your Splunk instance (replace placeholders) or test them against the CSV using Splunk's CSV lookup features or sample tools.  
4. See `dashboards/` for visual examples and `images/` for quick screenshots to include in a portfolio.

**Ethics & safety**  
This repo is intentionally synthetic and safe for public sharing. Do not use it to test against production systems without proper authorization.
