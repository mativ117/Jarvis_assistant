"""Host shell tool retained as a fail-closed compatibility stub."""

from __future__ import annotations

from typing import Any

from openjarvis.core.registry import ToolRegistry
from openjarvis.core.types import ToolResult
from openjarvis.tools._stubs import BaseTool, ToolSpec

@ToolRegistry.register("shell_exec")
class ShellExecTool(BaseTool):
    """Host shell execution is disabled in Jarvis Assistant."""

    tool_id = "shell_exec"

    @property
    def spec(self) -> ToolSpec:
        return ToolSpec(
            name="shell_exec",
            description="Host shell execution is disabled in Jarvis Assistant.",
            parameters={
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "Shell command to execute.",
                    },
                    "timeout": {
                        "type": "integer",
                        "description": ("Timeout in seconds (default 30, max 300)."),
                    },
                    "working_dir": {
                        "type": "string",
                        "description": (
                            "Working directory for the command."
                            " Must exist and be a directory."
                        ),
                    },
                },
                "required": ["command"],
            },
            category="system",
            requires_confirmation=True,
            timeout_seconds=60.0,
            required_capabilities=["code:execute"],
        )

    def execute(self, **params: Any) -> ToolResult:
        # Jarvis Assistant: deliberate denial before inspecting arguments,
        # importing a native backend or touching the host environment.
        return ToolResult(
            tool_name="shell_exec",
            content="Host shell execution is disabled in Jarvis Assistant.",
            success=False,
        )


__all__ = ["ShellExecTool"]
