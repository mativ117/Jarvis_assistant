# Foundation 0.8 — permission admission

Status: isolated policy unit tests passed; project integration not validated. No install or release approved.

## Changes
- New immutable exact-match PermissionGrant/PermissionPolicy; no wildcard, malformed identifiers deny; no implicit or environment-based grant. No identity authentication or grant issuance is implemented.
- Canonical Python ToolExecutor enforces empty Foundation grants before parsing arguments, dispatch or event emission and filters catalog methods. Native Rust executor also denies by default and filters tool catalogs. This deliberately disables all agent tools behind these entry points, including calculator. Direct native bindings, imports, constructors, alternate operation paths and agent/model/provider code are not a complete security boundary.
- CapabilitiesConfig defaults enabled and default-deny; removed implicit wildcard agent grants, including file, network and memory access. Explicit legacy config settings are not yet locked down. Runtime identity binding and authorization of future grants are still required.
- Added Python unit and integration tests and native denial test. Upstream positive tool tests may fail because this is an intentional policy change; do not suppress failures or claim compatibility. Reconcile the test suite after full checkout.

## Verification
Isolated local test on exact new policy and unit test files copied into a minimal namespace package, using existing Python/pytest, no upstream code or dependencies imported: 17 passed. Expected Git blob SHA-1: policy d6b25e9a540c4038f4fd53293a25759b4192e88b; test c44b4e6ef220fec9bf9de58fa07cd9edf474be52. Verify uploaded hashes separately. Full clone failed due to DNS in execution environment; Rust/Cargo and Docker unavailable. Integration tests not run. No malware, SAST, dependency or runtime scan performed.

## Next gates
Wire identity/session authorization; broker approved read-only operations, scoped resources, revocation, rate limits, audit without payloads. Inventory every alternate native, plugin, scheduler, file, inference and network path; enforce OS isolation and private egress. Keep Actions disabled. Revert this topic commit for rollback only; do not deploy unrestricted upstream defaults. No merge.
