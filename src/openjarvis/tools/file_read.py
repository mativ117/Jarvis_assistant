"""Disabled direct host file_read tool (Jarvis Assistant)."""

from __future__ import annotations

from typing import Any, List, Optional

from openjarvis.core.registry import ToolRegistry
from openjarvis.core.types import ToolResult
from openjarvis.tools._stubs import BaseTool, ToolSpec

@ToolRegistry.register("file_read")
class FileReadTool(BaseTool):
    """Direct host file access is disabled."""

    tool_id = "file_read"

    def __init__(
        self,
        allowed_dirs: Optional[List[str]] = None,
    ) -> None:
        # Retain the constructor contract; even an allowlist cannot enable this tool.
        del allowed_dirs

    @property
    def spec(self) -> ToolSpec:
        return ToolSpec(
            name="file_read",
            description="Direct host file access is disabled in Jarvis Assistant.",
            parameters={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file to read.",
                    },
                    "max_lines": {
                        "type": "integer",
                        "description": ("Max lines to return (default: all)."),
                    },
                },
                "required": ["path"],
            },
            category="filesystem",
            required_capabilities=["file:read"],
        )

    def execute(self, **params: Any) -> ToolResult:
        # Deny before resolving a path or accessing the native backend.
        return ToolResult(
            tool_name="file_read",
            content="Direct host file access is disabled in Jarvis Assistant.",
            success=False,
        )


__all__ = ["FileReadTool"]
