//! Jarvis Assistant: fail-closed direct HTTP tool.

use crate::traits::BaseTool;
use openjarvis_core::{OpenJarvisError, ToolResult, ToolSpec};
use once_cell::sync::Lazy;
use serde_json::Value;
use std::collections::HashMap;

static SPEC: Lazy<ToolSpec> = Lazy::new(|| ToolSpec {
    name: "http_request".into(),
    description: "Direct HTTP requests are disabled in Jarvis Assistant.".into(),
    parameters: serde_json::json!({
        "type": "object",
        "properties": {
            "url": { "type": "string", "description": "URL to request" },
            "method": { "type": "string", "description": "HTTP method (GET, POST, etc.)" },
            "body": { "type": "string", "description": "Request body (optional)" },
            "headers": { "type": "object", "description": "HTTP headers (optional)" }
        },
        "required": ["url"]
    }),
    category: "network".into(),
    cost_estimate: 0.0,
    latency_estimate: 0.0,
    requires_confirmation: true,
    timeout_seconds: 30.0,
    required_capabilities: vec!["network:fetch".into()],
    metadata: HashMap::new(),
});

pub struct HttpRequestTool;

impl BaseTool for HttpRequestTool {
    fn tool_id(&self) -> &str {
        "http_request"
    }
    fn spec(&self) -> &ToolSpec {
        &SPEC
    }
    fn execute(&self, _params: &Value) -> Result<ToolResult, OpenJarvisError> {
        Ok(ToolResult::failure(
            "http_request",
            "Direct HTTP requests are disabled in Jarvis Assistant.",
        ))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn direct_http_denies_without_echoing_inputs() {
        let params = serde_json::json!({
            "url": "https://example.invalid/SECRET_CANARY",
            "method": "POST",
            "body": "PRIVATE_CANARY",
            "headers": {"Authorization": "SECRET_CANARY"}
        });
        let result = HttpRequestTool.execute(&params).unwrap();
        assert!(!result.success);
        assert_eq!(result.content, "Direct HTTP requests are disabled in Jarvis Assistant.");
    }
}
