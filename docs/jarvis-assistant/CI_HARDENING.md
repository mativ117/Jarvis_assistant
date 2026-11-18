# Foundation 0.4 — CI isolation

Status: on security/foundation only. Main and repository Actions settings unchanged.

- Archived eight inherited workflows outside .github/workflows without changing their original blobs: autotag, PyPI, desktop release, Claude issues/review, traffic, issue assignment and Pages.
- Retained six validation workflows. All now declare contents: read explicitly and disable checkout credential persistence. Removed the inherited Supabase secret from frontend build; installer integration is manual-dispatch only instead of automatic PR/scheduled runs.
- No workflow or project code executed. Preliminary text checks: explicit read permissions, no secrets.* references in the six retained workflows, and one persist-credentials: false for each checkout. GitHub tree comparison verifies the eight archived blobs; confirm post-commit state separately.
- Remaining mandatory gates: verify and pin action revisions to immutable SHAs and review provenance; validate YAML and event/permission policy with actionlint or equivalent; audit all dependency install paths, artifact publishing, runner trust and external network calls; build independent secret/dependency/SAST checks; run CI in clean ephemeral runners without personal secrets after approval. The CI changes do not by themselves eliminate supply-chain risks.
- Keep Actions disabled until these gates pass. The fork still has the original workflows on main until an approved PR is merged. Do not add CI requirements before approved checks can run. Rollback by reverting on topic branch; never enable archived workflows by accident.
