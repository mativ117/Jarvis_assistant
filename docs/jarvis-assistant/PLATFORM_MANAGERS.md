# Jarvis platform managers — product roadmap

Status: accepted direction; deferred implementation after Foundation and secure local MVP. No device discovery, real-world control or privileged action is currently authorized or performed.

## Modules
| Manager | Scope |
|---|---|
| Device | User-authorized inventory of USB, Bluetooth and Wi-Fi devices, capabilities, drivers and official/local interfaces; explicit device enrollment and revocation. |
| Network | Own authorized LAN only: inventory, Wi-Fi quality, latency, interference, router health/config review, unknown-device alerts and before/after metrics; no unauthorized scanning or access. |
| System | CPU/GPU/RAM, processes, updates, performance and maintenance recommendations; no unrestricted shell. |
| Security / Guardian | Native, cross-cutting defensive safeguards for all modules; optional advanced local security dashboard, anomaly detection, incident triage and recovery. |
| Gaming | Reuse Context/Gaming Hub; approved game telemetry, racing companion, supported force-feedback profile read/save/restore and switching for compatible wheels/games (e.g. Fanatec CSL DD, F1, ACC, Forza); Xbox compatibility must be verified. Never alter torque while driving, inject into games, bypass anti-cheat or modify firmware. |
| Home | Official vendor APIs or reviewed local integrations (e.g. Home Assistant); supported purifier controls, air-quality readings, speed/mode, filter status and trends; no unverified access methods. |
| Energy | Measured or estimated device energy, clearly labeled; trends and recommendations; only explicitly approved safe automation. |
| Storage | Capacity analysis, user-selected file inventory, backups, restore verification, recommendations; never silently delete, move or disclose files. |

## Shared architecture
Use a modular monolith initially, with adapters and a common typed device/event contract, policy gate, capability inventory, measurement service and action broker. Keep raw credentials outside models and logs; local-first and no automated external telemetry. Context and Guardian consume minimized, authorized events. Avoid duplicating integrations. No admin permissions by default. Network and device operations use supported interfaces and user-approved scopes; no access to third-party systems. Untrusted device responses cannot grant permissions.

## Action lifecycle
Discovery -> review capability and permissions -> baseline -> propose change with impact -> explicit confirmation or narrowly scoped pre-approved policy after separate review -> execute through official mechanism -> verify result -> record minimal audit metadata -> rollback/recovery if appropriate. Initial managers are read-only. Never enable high-risk actions by default. Physical safety overrides automation; no firmware flashing without separate validation. Report unsupported features and device freshness. Before/after metrics use comparable conditions.

## Cross-cutting defensive requirement
All modules must implement prevention, least privilege, input validation, isolation, monitoring/alerts, incident response and recovery proportionate to risk. Guardian should detect unknown devices, suspicious connections, malware signals and attempts to tamper with Jarvis. Initial response is informational, plus deterministic refusal inside Jarvis. Future narrowly scoped, opt-in containment may use trusted OS/router mechanisms to block suspicious connections or isolate/quarantine affected components, with false-positive handling, explicit authorization, rollback and recovery; never attack back, bypass OS controls or interfere with unrelated devices. Security remains active in every module even when Guardian's dashboard is off.

## Delivery sequence
Foundation and isolated verification -> secure core and mobile portal -> shared permissions/event interfaces -> read-only device/system/network inventory -> supported adapters and metrics -> review-based safe actions. Gaming Context and Home integrations remain independently optional. No extra paid services or technology choices committed.
