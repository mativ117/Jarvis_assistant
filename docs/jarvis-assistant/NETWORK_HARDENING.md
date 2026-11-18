# Foundation 0.3 — Docker network defaults

Status: patch on topic branch, not merged or released. F-guard: no public host exposure by default.

## Change
- deploy/docker/docker-compose.yml: publish Jarvis as 127.0.0.1:8000:8000; remove Ollama host port publication; preserve service-name URL and required API key.
- tests/deploy/test_deploy_auth.py: parse YAML and check exact loopback mapping, no Ollama host port, unchanged internal endpoint and no extra published ports or host networking in both GPU overrides.
- docs/deployment/docker.md: update host mappings and API key examples, warn installation remains blocked.
- Gaming Hub discovery reserved independently in GAMING_HUB.md.

## Verification (2026-11-18)
GitHub file content was read back and copied into an isolated scratch directory. Git blob SHA-1 matched for all four files (base Compose, NVIDIA/ROCm override, test file). With preinstalled pytest 9.0.2 and PyYAML 6.0.3, the selected static tests ran: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/deploy/test_deploy_auth.py -k 'docker_compose or docker_gpu_overrides'`: **4 passed, 8 deselected**. No Jarvis import, installer or service ran. This is a selected static subset, not full CI. Verify PyYAML availability in the repository test environment before CI activation; do not change lockfiles without a full checkout.

## Remaining gates
Docker CLI unavailable in scratch environment. Need effective Compose config checks (CPU and both GPU overrides), runtime negative tests from LAN and peer containers, API key and WebSocket validation, firewall verification and full CI. Loopback is not a complete isolation boundary, and Ollama remains accessible to peers on the Compose network; outbound traffic has not been restricted. Other deployment paths (including systemd) still require separate hardening. Verify Docker version and network behavior. No mobile access until private authenticated HTTPS is validated.

Compatibility: clients formerly using host Ollama port must use the service name inside Compose, or a separately reviewed loopback-only override. Rollback: revert the related commits on the topic branch; do not restore an exposed configuration for personal use.
