# Foundation 0.2 — supply-chain, CI and installer review

Status: **preliminary static review; NO GO for installation**.
Baseline: c3ed63f1d2a2c0c1f7dabbc69050e1968a11dc10 (2026-11-18 review).
All source paths below refer to that immutable revision. No installer, dependency, project code or binary was executed.

## CI inventory (14/14 workflow texts retrieved; targeted static review)

| Workflow | Evidence | Proposed disposition |
|---|---|---|
| autotag.yml | lines 9–10: contents/actions write; 85–86 dispatches publish | Remove from fork |
| pypi-publish.yml | 23: OIDC write; 144–157 publish token/upload | Remove |
| desktop.yml | 30: contents write; release creation and signing credentials | Replace with build-only after review |
| claude-issues.yml | 18–20: contents/PR/issues write; API key, trusted actor checks | Remove |
| claude-review.yml | 19–20: PR/issues write; API key, trusted actor checks | Remove |
| track-clones.yml | 9: contents write; 18–22 traffic token | Remove |
| take-assign.yml | 8: issues write; event interpolation | Remove |
| docs.yml | 20–21: Pages/OIDC write | Disable deployment until needed; retain docs |
| ci.yml | calls security-sast; tag-based actions; inspect optional failure at line 105 | Harden |
| security-sast.yml | Bandit, OSV/Python, Cargo Deny, Semgrep; tag-based actions | Harden and extend coverage |
| frontend.yml | tag-based actions; Supabase build input | Harden; no external leaderboard config |
| docker-validation.yml | read-only, checkout credentials disabled | Retain after review |
| installer-integration.yml | PR/schedule; installer execution tests | Retain only with isolated synthetic fixtures |
| bash-tests.yml | checkout by tag | Harden |

Before enabling CI: remove unnecessary workflows in a reviewed PR; pin remaining third-party actions to verified immutable SHAs, use read-only tokens, disable persisted checkout credentials, no secrets for PR jobs, no publishing or external AI. Confirm mandatory security checks actually run and fail closed. The current repository-level Actions setting is reported disabled by owner, not independently accessible. Do not enable it yet. The proposed dispositions are not implemented in this commit.

## Installer and runtime boundary findings

- Windows install.ps1 lines 248, 287–307, 382–387, 409–424, 556–580: remote uv script executed immediately, upstream clone/force-pull, uv sync without explicit locked flag, downloaded Ollama installer executed silently, optional scheduled-task invocation with ExecutionPolicy Bypass. No explicit integrity/signature verification is visible at the Ollama execution site. ExecutionPolicy Bypass is not an antivirus bypass; it still warrants removing unnecessary use.
- Windows jarvis-service.ps1 defaults to loopback and uses a limited task run level (40,148); retain least privilege and require an authenticated local profile.
- scripts/quickstart.sh 153–169, 201, 228, 268–280: remote installers, global npm update, dependency installation, npm install. Replace with reviewed pinned tooling and frozen/locked installs; do not auto-install prerequisites.
- scripts/install/install.sh 233,257,447,550,642: upstream repo default, optional external analytics endpoint/beacon, clone and remote Ollama installer. Explicitly disable external analytics; verify runtime network behavior. install-rust.sh uses remote shell pipeline and moving stable toolchain. Uninstaller has recursive deletion; test path guard and user-data retention before use.
- deploy/docker/docker-compose.yml publishes 8000:8000 and 11434:11434 on host interfaces; API key is mandatory for Jarvis, but Ollama's port exposure is unnecessary for a private server. Bind Jarvis host port to loopback, keep Ollama internal unless an explicit loopback-only override is needed. Test compose effective configuration, access and auth. GPU overrides expose host devices or read-only /proc and /sys; defer until justified. Sandbox Dockerfile uses digest-pinned base images but remote Rust bootstrap and unpinned uv installation; review before building.
- Windows Defender issue #1184 remains an installation blocker. Related #1275 was closed at earlier review but that is not proof of safety. Public hash search did not identify the official Rust component. Verify upstream archive checksums/signatures independently; do not restore quarantined files or disable Defender.

## Dependency inventory (not a vulnerability scan)

| Lockfile | Retrieved / inventory |
|---|---|
| uv.lock | NOT retrieved: 1,340,442 bytes, connector limit |
| rust/Cargo.lock | 329 package records |
| frontend/src-tauri/Cargo.lock | 586 package records |
| frontend/package-lock.json | 654 non-root package paths; 2 marked install scripts; no missing integrity for resolved entries |
| src/openjarvis/channels/whatsapp_baileys_bridge/package-lock.json | 99 non-root package paths; 4 marked install scripts; libsignal git+ssh pinned commit, no registry integrity |
| rust/crates/openjarvis-python/uv.lock | 1 editable package record |
| examples/cross_device_travel/Cargo.lock | 12 package records |

Counts are records/paths, not unique packages or installed dependencies. Rust lockfiles inspected list crates.io registry sources, not evidence of artifact safety. npm install hooks are not proof of malware. WhatsApp bridge is out of initial scope: do not install it; review git dependency and hooks before any later use.
The repository's scripts/security/audit_dependencies.py explicitly names only uv.lock and the two main Cargo lockfiles; extend independent scanning to npm, bridge and any shipped auxiliary lockfiles.
The 8 exceptions declared in .github/security/advisory-exceptions.json expire 2026-12-16. Includes DiskCache 5.6.3 (GHSA-w8v5-vhqr-4h9v; https://osv.dev/vulnerability/GHSA-w8v5-vhqr-4h9v), setuptools 80.10.2 (e.g. https://github.com/advisories/GHSA-h35f-9h28-mq5c), glib 0.18.5 and maintenance-only notices. Python lock presence and mitigation not independently verified because the lock could not be retrieved. Avoid DSPy/vLLM optional extras rather than forcing incompatible upgrades. Keep Ollama first; defer voice, connectors, training and extra inference backends; map mandatory imports before removing dependencies. Core currently includes PostHog and Telegram dependencies, so a local-only profile requires actual verification, not merely disabling optional extras.

## Next acceptance gates
1. Review and remove unnecessary CI; configure hardened CI with OSV/pip audit, npm audit, Cargo Deny, SAST, secret scan and SBOM, with explicit coverage.
2. Obtain a complete clean checkout and all lockfiles; verify source provenance, artifacts, advisories, licenses and history; record scan tools/versions and triage. No scanner results yet.
3. Patch Docker network defaults and installation flows, then test in a disposable VM with synthetic data, Defender active, no personal credentials or shared folders.
4. Only then start minimal local chat and scoped memory; validate authorization and denied actions before mobile access.

No runtime fixes, scanner results, complete dependency audit, binary verification or malware-free claim in this change. Rollback: revert this documentation commit on the topic branch. No merge or release authorized.
