//! Host shell tool: fail-closed compatibility stub (Jarvis Assistant).

use crate::traits::BaseTool;
use openjarvis_core::{OpenJarvisError, ToolResult, ToolSpec};
use once_cell::sync::Lazy;
use serde_json::Value;
use std::collections::HashMap;

static SPEC: Lazy<ToolSpec> = Lazy::new(|| ToolSpec {
    name: "shell_exec".into(),
    description: "Host shell execution is disabled in Jarvis Assistant.".into(),
    parameters: serde_json::json!({
        "type": "object",
        "properties": {
            "command": { "type": "string", "description": "Shell command to execute" },
            "cwd": { "type": "string", "description": "Working directory (optional)" }
        },
        "required": ["command"]
    }),
    category: "system".into(),
    cost_estimate: 0.0,
    latency_estimate: 0.0,
    requires_confirmation: true,
    timeout_seconds: 30.0,
    required_capabilities: vec!["code:execute".into()],
    metadata: HashMap::new(),
});

pub struct ShellExecTool;

impl BaseTool for ShellExecTool {
    fn tool_id(&self) -> &str {
        "shell_exec"
    }
    fn spec(&self) -> &ToolSpec {
        &SPEC
    }
    fn execute(&self, _params: &Value) -> Result<ToolResult, OpenJarvisError> {
        // Jarvis Assistant: no process creation or environment access.
        Ok(ToolResult::failure(
            "shell_exec",
            "Host shell execution is disabled in Jarvis Assistant.",
        ))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn host_shell_denies_without_echoing_arguments() {
        let result = ShellExecTool
            .execute(&serde_json::json!({
                "command": "SYNTHETIC_SECRET_CANARY",
                "cwd": "PRIVATE_PATH_CANARY"
            }))
            .unwrap();
        assert!(!result.success);
        assert_eq!(result.content, "Host shell execution is disabled in Jarvis Assistant.");
    }
}
