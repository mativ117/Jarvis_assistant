//! Disabled direct host file tools (Jarvis Assistant).

use crate::traits::BaseTool;
use openjarvis_core::{OpenJarvisError, ToolResult, ToolSpec};
use once_cell::sync::Lazy;
use serde_json::Value;
use std::collections::HashMap;

static READ_SPEC: Lazy<ToolSpec> = Lazy::new(|| ToolSpec {
    name: "file_read".into(),
    description: "Direct host file access is disabled in Jarvis Assistant.".into(),
    parameters: serde_json::json!({
        "type": "object",
        "properties": {
            "path": { "type": "string", "description": "File path to read" }
        },
        "required": ["path"]
    }),
    category: "filesystem".into(),
    cost_estimate: 0.0,
    latency_estimate: 0.0,
    requires_confirmation: false,
    timeout_seconds: 10.0,
    required_capabilities: vec!["file:read".into()],
    metadata: HashMap::new(),
});

static WRITE_SPEC: Lazy<ToolSpec> = Lazy::new(|| ToolSpec {
    name: "file_write".into(),
    description: "Direct host file access is disabled in Jarvis Assistant.".into(),
    parameters: serde_json::json!({
        "type": "object",
        "properties": {
            "path": { "type": "string", "description": "File path to write" },
            "content": { "type": "string", "description": "Content to write" }
        },
        "required": ["path", "content"]
    }),
    category: "filesystem".into(),
    cost_estimate: 0.0,
    latency_estimate: 0.0,
    requires_confirmation: true,
    timeout_seconds: 10.0,
    required_capabilities: vec!["file:write".into()],
    metadata: HashMap::new(),
});

pub struct FileReadTool;

impl BaseTool for FileReadTool {
    fn tool_id(&self) -> &str {
        "file_read"
    }
    fn spec(&self) -> &ToolSpec {
        &READ_SPEC
    }
    fn execute(&self, _params: &Value) -> Result<ToolResult, OpenJarvisError> {
        Ok(ToolResult::failure(
            "file_read",
            "Direct host file access is disabled in Jarvis Assistant.",
        ))
    }
}

pub struct FileWriteTool;

impl BaseTool for FileWriteTool {
    fn tool_id(&self) -> &str {
        "file_write"
    }
    fn spec(&self) -> &ToolSpec {
        &WRITE_SPEC
    }
    fn execute(&self, _params: &Value) -> Result<ToolResult, OpenJarvisError> {
        Ok(ToolResult::failure(
            "file_write",
            "Direct host file access is disabled in Jarvis Assistant.",
        ))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn direct_file_tools_deny_without_echoing_inputs() {
        let params = serde_json::json!({"path": "PRIVATE_PATH_CANARY", "content": "SECRET_CANARY"});
        for result in [FileReadTool.execute(&params), FileWriteTool.execute(&params)] {
            let result = result.unwrap();
            assert!(!result.success);
            assert_eq!(result.content, "Direct host file access is disabled in Jarvis Assistant.");
        }
    }
}
