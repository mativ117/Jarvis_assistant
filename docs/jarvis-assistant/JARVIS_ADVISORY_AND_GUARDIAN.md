# Jarvis 360 — Decision Intelligence and High-Assurance Guardian
**Date:** 2026-11-21  
**Status:** RESEARCH / PROPOSED. Not user-approved architecture, not implemented or audited. Complements [JARVIS_360_RESEARCH.md](JARVIS_360_RESEARCH.md).  
**Security:** no standing administrator rights, malware, exploit code, unauthorized testing or attack-back. Existing Foundation NO GO remains in force.

## 1. Platform boundaries and authorized alternatives

| Constraint | Supported alternative | Irreducible limit |
|---|---|---|
| Internet unavailable | Preinstalled on-device models, offline speech, encrypted local BrainOS, signed manual knowledge packs, Reflex Engine and cached OS diagnostics | No new cloud knowledge/signature updates and no online bank balance |
| PC unavailable | Real native on-device iPhone runtime, app's own memory and knowledge | Cannot inspect inaccessible PC or data that was not synced |
| iOS background/screen | App Intents/Shortcuts, user-initiated ScreenCaptureKit, widgets, notifications and documented background modes | No silent perpetual system-wide control, privileged malware scanning or unrestricted overlays |
| PC high-privilege threats | Windows built-in Defender, tamper protection, Secure Boot/TPM, OS virtualization defenses, trusted offline scan/recovery, tiny separately authorized broker | A normal assistant cannot guarantee it outranks a compromised kernel/hypervisor/firmware |
| Data center or connectivity outage | Encrypted peer sync on LAN, bounded event replay, idempotent commands and safe degradation | Devices with no communication path cannot sync immediately |

Apple platform capabilities are feature/OS/hardware/permission dependent and must be verified for the intended target version; new ScreenCaptureKit screen sharing still requires user permission and approved lifecycle. Direct system control on iOS remains restricted.

## 2. Guardian's actual security authority

Design for *strongest effective protection with least privilege*, **not permanent highest privilege**:
- **G0 — local safeguards:** Guardian and policy broker automatically reject unapproved Jarvis tools, prompt-injection-driven actions, outbound data transfers and unsafe capture. Stop local worker/sessions; never require host admin privilege.
- **G1 — read-only OS telemetry:** query supported Windows Defender, firewall, Event Log and hardware health interfaces with constrained identities. Correlate signals; be honest about uncertainty and stale feeds.
- **G2 — user-preapproved reversible actions:** isolate an individual Jarvis component, pause a local adapter, throttle/deny an owned outbound connection and revoke a Jarvis session. Apply bounded rules independently of the LLM.
- **G3 — trusted elevated maintenance broker:** a small OS-signed, closely audited Windows service receives an authenticated typed request with explicit resource and TTL. Use UAC / Windows Administrator protection and OS/vendor APIs with user authorization for narrow host actions: Defender scan, allowlisted firewall change, reversible host quarantine, trusted restore. Never expose a generic admin shell, allow model-authored commands or let Jarvis self-grant permissions. Enforce rate limits, replay protection, tamper-resistant journal, rollback and protection against confused-deputy attacks.
- **G4 — offline recovery:** when the normal OS cannot be trusted, give owner verified guidance to boot Microsoft Defender Offline / trusted recovery media, restore encrypted offline backups or reinstall. The running Jarvis app must not claim to defeat a kernel-level adversary.
- **Forbidden:** privilege escalation exploits, stealth persistence, bypass of UAC/Defender/anti-cheat, password harvesting, attacking or scanning third-party infrastructure without authority, 'hack back', malware creation or attempts to supersede Windows security kernel by default.

Guardian may suggest **authorized defensive penetration testing** of devices the owner controls, in a sandbox or carefully scoped lab, to validate protection. No unattended exploit deployment.

## 3. Finance Intelligence / Personal CFO (proposed)

Consolidate personal financial guidance, Money Hunter-style savings opportunities and cost optimization while keeping sensitive data local.
- P0 offline via manual CSV/OFX export, deterministic category rules, explicit manual income/expense/debt schedules; no account credentials or screen scraping.
- P1 opt-in bank account data using a suitably authorized PSD2 account-information provider and narrow **read-only** consent, verifying legal/provider status and integration security. Do not confuse account-information access with permission to initiate payments. Display last synchronization timestamp; no 'current balance' claim when offline.
- Automatic read-only insights: income vs expenditure, committed costs, upcoming bills/renewals, cash runway, budget variance, contract end dates, unusual transactions, savings targets, expense/provider comparison, forecast scenarios, debt-rate watch, cash-flow timing and negotiation reminders.
- Data minimization: explicit bank/account selection, local encrypted persistence, token handling via OS Keychain / Windows secret store, revocation, export and deletion, short retention and separate cloud consent. Mask balances, merchants, account numbers and transaction details on overlay and lockscreen.
- Investment/tax decisions: show assumptions and cite sources, label estimates, distinguish educational analysis from regulated investment/tax advice; never claim guaranteed return or recommend a transaction solely from model inference. No payments, transfer initiation, trades or provider cancellations without separate permissions, confirmed details and audit.

## 4. Timing & Action Intelligence / Personal Chief of Staff (proposed)

Take input from authorized calendars, bills, project tasks, device alerts, commitments and user-declared goals to propose **the next useful action**, offline when cached.
- Proactive triage: actionable recommendation with reason, evidence/source, benefit, confidence, deadline, urgency, effort, dependencies, risk, privacy level and whether connected services are available. Clearly separate observed facts from inferred priorities.
- Categories: finance (renewals, comparison windows, cost controls), time (meeting preparation, travel buffers, deadlines), career and income opportunities, personal/project reminders, security remediation and device maintenance.
- Scheduling: no silent calendar edits/messages/purchases; propose schedule blocks, queue reviewable actions, respect DND/quiet hours, fatigue, user availability and meeting constraints; avoid nagging and spurious claims of urgency.
- Deterministic scheduler and event store for hard deadlines with timezone/DST support, missed-event reconciliation, idempotency and offline alerts. The LLM writes explanations and suggestions, not trusted deadlines or privileged tool calls.
- Prioritization function should be explainable and user-adjustable, e.g. due-date exposure + expected verified benefit + risk reduction − cost/effort/uncertainty. Avoid an opaque score; never rank a dubious financial offer above a critical security incident solely based on speculative gain.
- Notifications on phone/desktop show generic text when locked, with sensitive data visible only after authentication. Sync selective data; preserve "source" and "last updated".

## 5. Unified action record

Each proposal should have a typed record:
`id, origin, subject, category, priority, evidence, confidence, estimated_benefit, cost, due_at, freshness, sensitivity, required_permissions, available_on_device, state, expiry, approval, rollback_plan, result`.

Transitions: `detected -> verified -> proposed -> approved/rejected -> executed -> checked -> archived`. Expire stale advice; support cancellation. No agent-initiated move to approved.

Example: “Your Internet contract renews in 21 days (document dated X, source Y). Comparable offer appears cheaper by ~€N/year (estimated, pricing last verified Z). Review and contact provider before deadline.” Never auto-transfer funds or silently cancel service.

## 6. Acceptance criteria
- Offline PC and standalone iPhone independently produce safe reminders and cash-flow estimates based on current cached local data, marked as offline/stale; no outbound traffic.
- Synthetic bank datasets are sufficient to test all calculations, forecast and sensitive overlay/notification exclusion. Never use real user banking data in CI.
- Guardian tests with synthetic attack events: denial of privileged requests, refusal when identity missing, replay attack, malicious document injection, safe emergency stop, service down, corrupted logs and rollbacks. Test real Defender and offline recovery only in separately approved VM/physical tests.
- Elevation is short-lived, action-scoped and independently authorized; model output is *never* proof of permission. No stealth/no escalation workarounds.
- All recommendations carry evidence, assumptions, freshness, reversibility and a human approval boundary. No action performed by this document.

## 7. Delivery recommendation
Foundation security audit and working core -> offline BrainOS + deterministic planner -> finance via local CSV and approved calendar import -> native offline mobile -> selective secure sync -> Guardian OS telemetry and optional scoped service -> advanced finance/API integrations and reversible host response. Add the smart action engine early in design but keep it read-only until safety gates pass.

## Primary references (as of 2026-11-21)
- Windows Administrator protection: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/administrator-protection/
- Windows UAC: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works
- Microsoft Defender Offline: https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-offline
- Windows Defender tamper protection: https://learn.microsoft.com/defender-endpoint/tamper-protection-overview
- Apple App Intents: https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework
- Apple ScreenCaptureKit: https://developer.apple.com/documentation/ScreenCaptureKit
- European Central Bank PSD2: https://www.ecb.europa.eu/press/intro/mip-online/2018/html/1803_revisedpsd.en.html
- European Banking Authority consent: https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2018_4309
- OWASP AI runtime security: https://github.com/owasp/www-project-ai-security-and-privacy-guide
