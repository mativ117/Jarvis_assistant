# Foundation — security audit and release gates

Status: **NO GO for installation or release**. This is a living record, not a security certification.

## Baseline
- Upstream: https://github.com/open-jarvis/OpenJarvis
- Initial fork revision: `c3ed63f1d2a2c0c1f7dabbc69050e1968a11dc10`
- Inventory: 2,492 tree entries including 2,230 blobs; full content and binary review pending.
- Main protection: active ruleset targeting default branch; pull request required, squash merges only, linear history, deletion and force push blocked. No mandatory CI check yet. GitHub Actions disabled per owner report; not independently verified.
- No project code or installer has been executed during the preliminary review.

## Initial risk register
| ID | Priority | Evidence | Remediation / acceptance |
|---|---|---|---|
| F-01 | P0 | Upstream issues [1184](https://github.com/open-jarvis/OpenJarvis/issues/1184) and [1275](https://github.com/open-jarvis/OpenJarvis/issues/1275): Defender reports involving Rustup downloads; cause unconfirmed. | Identify component and provenance, verify official signatures/checksums, scan in isolation; never bypass Defender or restore quarantined files. |
| F-02 | P0 | `src/openjarvis/tools/shell_exec.py`, `src/openjarvis/security/subprocess_sandbox.py` support shell execution; env filtering is not full OS isolation. | Disable unrestricted shell/code execution by default; verify denial across Python, Rust, API, agents and optional tools. |
| F-03 | P0 | `deploy/windows/install.ps1` downloads/executes external components. | Review all install/update paths; use pinned, verified artifacts and explicit opt-in for downloads. |
| F-04 | P0 | `src/openjarvis/server/auth_middleware.py` allows keyless loopback and checks non-loopback binding. | Require auth for hardened profile, verify HTTP/WebSocket coverage, use private TLS access only. |
| F-05 | P0 | `.github/workflows/` includes upstream release, auto-tag, AI review and CI automation. | Review every workflow, remove or disable unnecessary publishing/AI workflows, pin trusted actions, least-privilege tokens. Keep Actions disabled until approved. |
| F-06 | P1 | `.github/security/advisory-exceptions.json` includes tracked exceptions, including diskcache and setuptools. | Audit all lockfiles; distinguish installed vs optional dependencies; eliminate avoidable risks and document any narrowly scoped residual risk. |
| F-07 | P1 | External analytics documented in `docs/telemetry.md`; local telemetry is separate. | Verify actual runtime traffic and storage; deny external analytics/leaderboard by default. |
| F-08 | P0 | Agent permission, memory, connector, file, upload and network surfaces not exhaustively audited. | Threat model, fail-closed policy, path/SSRF protections, prompt-injection and data-exfiltration regression tests. |
| F-09 | P1 | Public fork cannot hold personal data or secrets. | Scan tracked content and history; use local encrypted storage, secret store, safe ignores and redacted logs. |

Priorities reflect release policy, not confirmed exploit severity. No malware or compromise has been established by this preliminary review.

## Audit sequence and exit criteria
1. Repository/CI: inventory all source, scripts, build/release paths, lockfiles, binary assets and submodules; review inherited workflows and upstream attribution.
2. Static review: run independent secret scanning, SAST, dependency/license/SBOM checks and malware scanning of artifacts in a clean environment; manually triage results and record tool versions and scope. Scan relevant history as well as working tree.
3. Hardened MVP: local chat and explicitly scoped memory only; no arbitrary shell, unapproved network, third-party plugins or write-capable agents. Deterministic policy and regression tests on all entry points.
4. Isolated runtime: test on a disposable VM with no personal credentials/shared folders; observe network, filesystem and process behavior, verify auth and denied actions. Retain AV protection. Reproducibly build and verify artifacts.
5. Windows performance and UX: functional/negative tests, recovery, RAM/latency measurements and accessibility. Only after passing, consider a limited personal-data trial.
6. Mobile: private encrypted network, authenticated responsive PWA, session/revocation tests, no public port forwarding. PC availability is required until a separate host is approved.
7. Release: report evidence and unresolved risks; require owner approval before merge/deploy. Do not label the project malware-free.

## Current evidence
Repository settings and initial targeted source review only. No full checkout, AV scan, SAST, dependency scan, build, runtime test or CI result has been independently obtained. All gates above remain pending.
