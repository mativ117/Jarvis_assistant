# Jarvis Context — cross-device contextual assistant

Status: accepted product direction, reserved for discovery after the secure local MVP. No implementation or platform compatibility claim. Gaming Hub becomes one optional domain adapter, not a separate contextual platform.

## Product vision
A single assistant with an adaptive, user-controlled interface that can display useful information, answer questions about explicitly shared content and react to authorized context events. Available on Windows and iPhone, with platform-specific presentation rather than identical OS privileges.

Examples: document explanation or summary; coding/error guidance; shopping comparisons; personal reminders; game telemetry and permitted coaching. Use structured sources (app APIs, selected text/files, telemetry) when possible; visual analysis is a fallback, not a requirement for every interaction.

## Interaction model
- On demand: manual shortcut/share action, selected text, file or screenshot; no passive capture.
- Session: explicitly start sharing a selected window/screen using supported OS APIs, with visible indicator, pause/stop, timeout and source controls. No hidden or continuous system-wide monitoring.
- Proactive: separately enabled, read-only rules based on selected event sources, scoped notification frequency and quiet hours; no arbitrary actions.
- Presentation: movable desktop side panel or optional always-on-top widget, full portal, phone companion dashboard and permitted notifications; user controls density and visibility.

## Proposed modular boundaries
Authorized context adapters -> consent/permission gate -> normalized typed events -> context resolver and local analysis -> domain-specific cards/voice/notifications.
Keep the capture agent, UI, models, telemetry pipeline and memory separate; use bounded queues, staleness markers and cancellation. Avoid reprocessing unchanged frames; sample on demand or at a measured rate. Prioritize local deterministic processing for structured data, local OCR/vision where viable, and optional cloud analysis only with explicit permission; never send screen contents to cloud by default. Context is untrusted data, not executable instructions. Domain adapters cannot grant permissions. Keep short-lived context in memory by default; any persistence needs explicit opt-in, purpose and deletion controls.

## Platform constraints
- Windows: use sanctioned window/display capture with user selection (Windows.Graphics.Capture); separate overlay window, no process injection. Some protected windows, exclusive fullscreen games and capture-restricted apps may be unavailable. Verify target OS and input/pass-through behavior.
- iPhone: initial responsive PWA and system share/manual screenshot workflows. A PWA cannot silently inspect other apps or show arbitrary system-wide overlays. A future native app may use user-initiated platform screen sharing where supported (Apple ScreenCaptureKit or ReplayKit depending on OS/SDK), subject to permissions and technical feasibility. Use in-app cards or permitted notifications/widgets rather than promising arbitrary overlay above other apps. Native distribution/signing and costs require separate review.
- PC and phone share only authorized session context over authenticated private encrypted transport. A PC-hosted assistant requires an available PC; local phone inference is a future option, not assumed.
- Gaming: see [GAMING_HUB.md](GAMING_HUB.md). Use official permitted data, no anti-cheat evasion.

## Security and privacy gates
Off by default; allowlist sources, user-visible capture status, one-step stop, bounded sessions and default ephemeral processing. Never capture password/sensitive windows intentionally, and warn that automatic redaction is imperfect. No capture of work/client or third-party confidential data absent authorization. No background microphone by default; no automatic clipboard monitoring. No automatic tool execution, messages, purchases or changes from observed content. Enforce model/tool/network boundaries in deterministic code; reject malicious instructions embedded in screens or files. No secret or sensitive data in logs, repository, analytics or default notifications. Authenticate clients, support revocation and minimize shared data. Test permission denial, cancellation, leakage, malicious content, replay, staleness, battery/RAM/CPU and accessibility.

## Discovery sequence
1. Build a secure local assistant and authenticated mobile portal first.
2. Prototype manual screenshot/text sharing and adaptive context cards using synthetic data.
3. Add Windows selected-window sessions and measure local performance; test protected windows and capture lifecycle.
4. Validate mobile share and companion workflows; investigate native screen sharing only as a separate optional feature.
5. Add independent adapters (gaming/telemetry, development, personal productivity, shopping) and proactive notifications after policy review.

## Platform references (reviewed 2026-11-18)
- Microsoft: https://learn.microsoft.com/en-us/windows/apps/develop/media-authoring-processing/screen-capture
- Apple: https://developer.apple.com/documentation/ScreenCaptureKit
- Apple ReplayKit security: https://support.apple.com/en-gb/guide/security/seca5fc039dd/web

No platform stack, capture frequency, native distribution route, paid services or implementation selected. No code executed and no release authorized by this document.
