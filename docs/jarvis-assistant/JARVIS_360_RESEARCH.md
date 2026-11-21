# Jarvis 360 — study and candidate requirements
**Date:** 2026-11-21  
**Status:** RESEARCH / PROPOSED. No new feature or technology selection approved; no code changes in this document.  
**Current code:** Foundation security branch, not validated for installation or private data.  
**Goal:** a Stark-inspired, realistic, local-first personal intelligence platform that remains useful offline, on Windows PC alone or iPhone alone, and cooperates securely when available.

## 1. Non-negotiable architecture
- Each participating device is independently useful, not a remote control for a single central computer. **PC runtime:** local OS diagnostics, user-approved resources, local model and private memory. **iPhone runtime:** platform-sanctioned native local inference, private cache, local voice and supported phone capabilities. **Optional LAN sync:** authenticated peer discovery, encrypted transport and conflict resolution. **Optional cloud:** opt-in and purpose-specific.
- Use *capability detection*, not assumed device features. Offline mode needs pre-provisioned models, documentation, policy data, voices and a configured local identity. Outdated security intelligence is explicitly marked stale.
- **Deterministic Reflex Engine:** a tiny rule/policy executor handles immediate reversible, pre-authorized actions; the LLM can explain and recommend but cannot grant access or authorize execution. No shell/script execution from model text.
- **Security Core:** mandatory across modules, distinct from advanced optional Guardian dashboard. **BrainOS:** independently portable private memory. **Context:** controlled perception. **Managers:** device/network/system/home/gaming/energy/storage adapters.
- Existing upstream OpenJarvis access surfaces must first pass audit; no production deployment until all required gates pass. Preserve the main branch.

## 2. Operating mode requirements

| ID | Mode | Minimum functional capability | Boundary |
|---|---|---|---|
| O-1 | Windows with WAN | Local core plus separate approved Internet providers | Never automatic cloud transfer of private context |
| O-2 | Windows without WAN | Preinstalled local LLM, cached BrainOS, rules, offline voice, system health checks and local compatible devices | Cannot update cloud knowledge / AV signatures while disconnected |
| O-3 | Windows + iPhone on isolated LAN | Authenticated local API and encrypted subset synchronization with conflict resolution; no WAN dependency in established LAN mode | PC must be on; LAN connectivity and permissions needed |
| O-4 | iPhone with WAN, PC off | Native local chat/memory/voice, approved external providers if explicitly enabled | No access to uncached PC-only state |
| O-5 | iPhone offline, PC off | Native on-device model, cached memory, built-in knowledge packs and supported local device functions | iOS sandbox/background limits; no general Windows or system-wide iOS inspection |
| O-6 | Network/OS degraded | Health signal, local diagnostics, clear “stale” labels, safe rollback and backup restore | An unavailable or unverified dependency must fail safely |

## 3. Feature register — proposals

**Foundation / P0 before usable pilot**
- J360-01 Device-local runtime and offline capability negotiation; no assumption that PWA alone provides phone-only AI.
- J360-02 Capability permissions: verified identity, resource-specific grants, user/device/session scope, expiry, revocation, private audit metadata; default deny.
- J360-03 Reflex Engine and risk tiers: immediate protective refusal inside Jarvis, approved reversible local actions, OS actions requiring separate confirmation, and prohibited operations.
- J360-04 BrainOS versioned local-first memory: user-controlled provenance, confidence, retention, selective sync/export/delete, data classification and stale-state markers.
- J360-05 Data Protection Gate: capture off by default; allowlisted sources and explicit session, strict no-cloud policy for screen raw/derived data, no default clipboard/keystroke access, fail closed.
- J360-06 Recovery and integrity: safe mode, kill switch, signed updates, backups and tested restore, component heartbeat, bounded restart policy.
- J360-07 Offline diagnostics: distinguish OS security events and sensor measurements from AI inferences; no fabricated device observability.
- J360-08 Evidence-driven testing: fake secrets, attack simulations in isolated VM, egress and storage traces, OS and dependency scans, all alternate tool paths.

**Near-term / P1**
- J360-09 Windows text chat/local model plus iPhone native local model adapter with model availability checks.
- J360-10 Push-to-talk voice first; local speech recognition and synthesis, opt-in local wake word later.
- J360-11 Cross-device transport: pairing QR/out-of-band trust, mutual auth, E2EE, encrypted local subset sync, append-only operation IDs, safe conflict resolution, lost device and revocation flows.
- J360-12 Context cards, explainable relevance decisions, Windows selected-window capture and visibility controls; no indiscriminate full-screen scan.
- J360-13 Guardian read-only Defender status/firewall/event monitoring; risk correlation, local incident explanations, recommendations and generic mobile alerts.
- J360-14 User-approved typed device adapters and inventory, compatible local protocols, stale telemetry detection and safe defaults.
- J360-15 Offline knowledge packs: manuals, troubleshooting procedures, asset inventory, signed update metadata and exportable recovery guide.

**Later / P2**
- J360-16 Local predictive maintenance and “personal systems digital twin”: dependency map, measured telemetry, what-if impact simulation.
- J360-17 Sim-racing telemetry and ergonomic overlay, without game process injection or anti-cheat interference; authorized game APIs only.
- J360-18 Optional OS actions/containment through dedicated least-privilege broker, allowlisted reversible operations, strong approvals and rollback, not a general admin agent.
- J360-19 Home protocols and energy models on truly local-capable devices; platform/provider compatibility verification.
- J360-20 Guided self-improvement: Jarvis suggests policies and code changes but changes require tests, PR review, no autonomous self-modification of privileged production code.

## 4. Cybersecurity control register

| Control | Mandatory behavior |
|---|---|
| Threat model | OS malware, physical loss, hostile LAN, malicious websites/docs/screens, compromised dependency/plugin/model, rogue agents, poisoned memory, user mistakes |
| Zero trust & device identity | Mutual authentication, least privilege, segmentation, token rotation/revocation, no implicit local-network trust |
| Secrets | OS Keychain/Secure Enclave on iOS, credential manager/DPAPI or platform hardware-backed storage on Windows; no plaintext repo/env/logs/screens |
| Data lifecycle | Classification, purpose and consent, minimized collection, encrypted storage, retention limits, deletion/export, encrypted backups and recovery-key procedure |
| Tool execution | Deterministic policy gate before IO, scoped action broker, typed resources, no arbitrary shell, injection-safe parsing, user confirmations |
| Capture & overlay | Explicit user-selected source, visible status, stop/pause; deny uncertain sensitive windows; don't assume automatic redaction is perfect |
| Network egress | OS-enforced outbound restrictions where feasible, service allowlists, no unapproved cloud inference or telemetry, DNS/redirect/SSRF and exfiltration tests |
| Agent & model threats | Prompt injection, tool misuse, rogue skills, context poisoning, privilege escalation, spoofed device data, cascade failure and untrusted output |
| Software supply chain | Dependency and license inventory/SBOM, pin and attest releases, SAST/DAST, secret/history scans, reproducible build, signed rollback |
| Incident defense | Govern/identify/protect/detect/respond/recover, uncertainty-aware triage, minimal alerts and after-action evidence |
| Reliability | Bounded queues, local durable events, idempotent commands, fail-safe degraded mode, backups, restore testing, resource budgets |
| Human safety | No unattended firewall/AV disable, file deletion, firmware flashing, high-torque wheel profile change or irreversible device action; never retaliate |

## 5. Autonomous response tiers
1. **Always allowed inside Jarvis:** reject unauthorized API/tool calls; immediately stop its capture, block its own outbound task and isolate/restart a suspicious sandboxed component. Deterministic rules, not model approval.
2. **Opt-in standing authorization:** small predeclared reversible Jarvis-internal actions with TTL, safety constraints, rate limiting and auditable rollback (e.g., pause a connector on anomalous traffic).
3. **Per-action user authorization:** OS-level antivirus scan, changing host firewall rules, quarantining a real file, modifying a device configuration; execute through OS/vendor APIs and show before/after.
4. **Prohibited by default:** disabling security products, broad deletion, credential harvesting, hidden capture, arbitrary shell, unapproved firmware changes, attack-back, actions on third-party systems.

Offline “instant response” is practical only for Tier 1/previously preapproved deterministic Tier 2 within already-running processes and available local permissions. No guarantee against compromised OS or powered-off host.

## 6. UI and user experience
One conceptual system, multiple surfaces: Windows desktop + optional contextual overlay; iPhone native home/voice/offline dashboard; responsive PWA as transitional companion, not the sole phone-only backend. Always display runtime (“on-device”, “LAN”, “cloud”), data provenance/freshness, active permissions, connected devices and action history. A single kill switch closes sessions. Push-to-talk is default; always-on mic and screen analysis opt-in only. Accessibility, minimal battery drain and nonintrusive notifications are release criteria.

## 7. Candidate technologies — NOT selected
- Windows runtime: keep reviewed OpenJarvis components; potentially a modular monolith with Rust core, Python model adapters, SQLite/FTS and an accessible Tauri/WebView2 UI. Minimize rewrites; don't assume current upstream runtime is secure.
- Local PC inference: Ollama or llama.cpp, model and hardware benchmark first (16 GB system RAM target).
- iPhone: SwiftUI/native shell and Apple Foundation Models on-device when model availability permits; Core ML/Core AI or locally bundled reviewed llama.cpp backend if unsupported. Build requires macOS/Xcode. Free personal development differs from TestFlight/App Store distribution.
- Voice: whisper.cpp is a candidate for offline STT; assess platform-native speech/TTS. Original rhasspy/piper repository is archived; do not select an unmaintained upstream without checking maintained forks/licenses.
- Mobile secrets: Keychain/Secure Enclave; Windows secrets: platform credential manager/DPAPI. Encrypt sensitive datasets with reviewed cryptographic storage and test backups.
- Local device integrations: Home Assistant and documented local protocols, selected based on device support. Remote access is optional and separately secured, never needed for LAN-offline operation.
- Sync: versioned encrypted data packages, idempotency/conflict records and incremental selective replication; no cloud account or always-online central authority necessary for already-paired devices. Revocation while disconnected has fundamental limits.

## 8. Platform constraints and residual risks
- Apple permits native on-device models and Core AI, but actual hardware, OS, downloaded model and region/language availability are checked at runtime. Cloud Foundation models are not offline.
- iOS background execution is limited and not a guaranteed always-on monitoring daemon; system-wide overlay/screen/other-app control is restricted.
- Windows screen capture requires user-mediated selection/authorization; cannot promise perfect detection of sensitive pixels.
- iOS native app build requires Xcode/macOS, including Tauri mobile builds; a Windows-only PC cannot do local native iOS compilation without a macOS build environment.
- Local models and security definitions must already be provisioned before going offline. Offline presence cannot be inferred from app download alone.
- Remote services, cloud-only smart devices, unavailable radios, PC power state and OS compromise cannot be overcome by the assistant.

## 9. Acceptance suite before CodeX pilot/release
- No network and no PC: iPhone local chat, cached BrainOS, locked-device privacy and safe error messages.
- No WAN but local PC and phone: direct authenticated pairing/transport and selective sync, reconnect conflict resolution, no external DNS or unexpected traffic.
- Local PC: offline model, deterministic Defender status query, detection of disconnection, no unapproved shell/files/outbound request.
- Synthetic injected web page/document/screen instructions cannot trigger an action; generated instructions never bypass policy.
- Fake credentials/OTP/banking screen do not reach models, logs, messages, crash reports, persistent memory or another device.
- Revocation, loss of device, replayed commands, bad certificates, stale rules, corrupted backup, low disk, battery starvation, process crashes and multiple concurrent sessions.
- Measure CPU/RAM/battery, latency, crash-free operation and model reliability on actual target devices. Independent review, regression suite, and owner sign-off.

## 10. Practical design decisions for next session
Accept or amend before coding: (A) independent per-device offline runtimes; (B) deterministic Reflex Engine; (C) identity/permission broker; (D) BrainOS selective sync and data lineage; (E) critical capture/network/secret policy; (F) native iPhone eventual requirement and macOS build constraint; (G) Windows-only V0.1 vs first cross-device offline milestone. No new module is considered implemented or approved by this research document.

## Sources (official/primary, accessed 2026-11-21)
- Apple Foundation Models: https://developer.apple.com/foundation-models-framework/
- Apple Core AI: https://developer.apple.com/core-ai/
- Apple background modes: https://developer.apple.com/documentation/xcode/configuring-background-execution-modes
- Apple MultipeerConnectivity: https://developer.apple.com/documentation/MultipeerConnectivity
- Apple Keychain: https://developer.apple.com/documentation/security/keychain-services
- Tauri iOS prerequisites: https://v2.tauri.app/start/prerequisites/
- Microsoft Windows capture: https://learn.microsoft.com/en-us/windows/uwp/audio-video-camera/screen-capture
- Microsoft Defender status/scan: https://learn.microsoft.com/en-us/powershell/module/defender/get-mpcomputerstatus
- Home Assistant offline: https://www.home-assistant.io/faq/works-without-internet/
- OWASP agent security: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- OWASP MASVS: https://mas.owasp.org/MASVS/
- OWASP ASVS: https://asvs.owasp.org/
- NIST CSF 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- NIST SSDF: https://csrc.nist.gov/pubs/sp/800/218/final
- European Data Protection Board: https://www.edpb.europa.eu/topics/ai-and-technology/privacy-by-design-and-by-default_en
- whisper.cpp: https://github.com/ggml-org/whisper.cpp
- Ollama Windows: https://github.com/ollama/ollama/blob/main/docs/windows.mdx
