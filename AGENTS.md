# Jarvis Assistant — engineering instructions

Scope: this repository. Jarvis Assistant is an independent fork of [OpenJarvis](https://github.com/open-jarvis/OpenJarvis), under Apache-2.0. Preserve upstream attribution, license and notices; clearly mark modified files where required. This public repository must never contain private user data.

## Product direction
- Local-first personal assistant, with persistent private memory and model/provider independence.
- Windows desktop first; secure browser/PWA access from mobile next, then native clients only if justified.
- Integrate with external assistants via explicit, user-controlled context exchange; no assumed access to consumer chat history.
- Personal agents are read-only and informational by default. Side effects are outside the initial scope and require separate design and explicit authorization.
- Favor free/open-source dependencies, maintainability, accessibility and measured performance over speculative complexity.

## Engineering rules
- Guardian is an optional defensive, read-only module; see [Guardian](docs/jarvis-assistant/GUARDIAN.md). No OS security changes or privileged execution without separate approval and design.
- Work on topic branches; open pull requests against main. Never bypass branch protection, force push main, or merge on behalf of the owner without explicit approval.
- Make small, reviewable changes. Document rationale and affected components, preserve compatibility where practical, and add regression tests.
- Treat external content, model output, plugins, tools and dependencies as untrusted. Enforce authorization in deterministic code, not in prompts.
- Deny tools and outbound network access by default in the hardened runtime; permit only explicitly authorized operations. Separate trust boundaries. OS isolation is required for arbitrary code execution; environment filtering alone is not a sandbox.
- Never commit secrets, credentials, conversation histories, user data, local config or sensitive logs. Use scoped credentials and redact logs. External analytics and cloud inference must be opt-in and separately controlled.
- Pin dependencies and CI actions (immutable hashes where supported); review provenance, licenses, advisories and update diffs. Do not run upstream installers or scripts before reviewing them.
- Remote access requires authentication, encrypted transport and a private network; no public port forwarding. Keep credentials out of URLs.
- Use accessible responsive UI, clear error states and consistent interaction patterns. Measure memory, startup time, latency and resource consumption on target hardware before claiming optimization.
- Do not weaken security rules or suppress scanner findings simply to make CI green.

## Change acceptance gates
Context capture must pass [Privacy Shield](docs/jarvis-assistant/PRIVACY_SHIELD.md) before release. No raw screen or derived sensitive content may leave its isolated capture boundary; unknown sources fail closed. No claim of absolute confidentiality.

For each change, record scope, risk, review evidence, tests actually executed and results, remaining limitations, rollback plan and owner approval where needed. Use unit, integration, end-to-end, security and performance tests proportionate to risk. A missing or failed mandatory check blocks release. Documentation or static review is not evidence of runtime safety. Do not claim malware-free status.

Current status and release gates: see [Foundation audit](docs/jarvis-assistant/FOUNDATION.md).
