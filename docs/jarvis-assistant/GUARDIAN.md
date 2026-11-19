# Jarvis Guardian — optional defensive security companion

Status: reserved for discovery after secure local MVP. Not an antivirus, EDR or security guarantee. No implementation, privileged service or active response authorized by this document.

## Goals
- Read supported OS security signals (Microsoft Defender, Windows Firewall, Windows Event Log, update status) through documented read-only interfaces; correlate and explain alerts locally.
- Detect suspicious changes and connections using scoped authorized metadata, flag known vulnerable installed software, offer phishing warnings for explicitly submitted URLs/text. Use existing OS protection and reputable data sources rather than writing a kernel driver or claiming zero-day detection.
- Separate Jarvis own security policy (deny unauthorized tools/egress) from device security advice. Never grant Guardian a bypass of Privacy Shield.
- PC security notifications may be shown on authenticated mobile companion; iOS system-wide scanning/monitoring is not assumed.

## Permissions and safe response
Read-only and informational by default; no privileged agent, raw network payload inspection, credential scraping, offensive scanning, stealth, persistence, remote shell, tampering with Defender, deletion/quarantine, firewall changes or automatic remediation. Use trusted OS mechanisms and guide owner to act. Any future response capability requires separate threat model, narrowly scoped authorization, explicit confirmation and rollback. Do not automatically upload suspicious files, URLs with tokens, event logs, process arguments or memory dumps. Minimize metadata, redact and keep local. No instructions from logs, webpages or alerts can trigger tools. No claims of protection against compromised OS/admin malware.

## Discovery / acceptance
Start with synthetic event fixtures, validate supported Windows APIs and minimum permissions, distinguish observed events vs inferred risk, test malformed events, spoofing, false positives, alert fatigue, data leakage, performance and offline behavior. Test with synthetic events and approved benign test artifacts in disposable VM; never introduce live malware into personal PC. Confirm privacy and read-only behavior with network/filesystem monitoring, audit dependencies and allow disable/uninstall. Mobile notifications generic by default. No deployment until Foundation and Privacy Shield gates pass.
