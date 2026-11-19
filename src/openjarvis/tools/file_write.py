"""Disabled direct host file_write tool (Jarvis Assistant)."""

from __future__ import annotations

from typing import Any, List, Optional

from openjarvis.core.registry import ToolRegistry
from openjarvis.core.types import ToolResult
from openjarvis.tools._stubs import BaseTool, ToolSpec

@ToolRegistry.register("file_write")
class FileWriteTool(BaseTool):
    """Write content to files with optional directory restrictions."""

    tool_id = "file_write"

    def __init__(
        self,
        allowed_dirs: Optional[List[str]] = None,
    ) -> None:
        # Retain the constructor contract; even an allowlist cannot enable this tool.
        del allowed_dirs

    @property
    def spec(self) -> ToolSpec:
        return ToolSpec(
            name="file_write",
            description="Direct host file access is disabled in Jarvis Assistant.",
            parameters={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file to write.",
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to write to the file.",
                    },
                    "mode": {
                        "type": "string",
                        "description": (
                            "Write mode: 'write' (overwrite/create)"
                            " or 'append' (append to existing)."
                            " Default: 'write'."
                        ),
                    },
                    "create_dirs": {
                        "type": "boolean",
                        "description": (
                            "Create parent directories if they"
                            " don't exist. Default: false."
                        ),
                    },
                },
                "required": ["path", "content"],
            },
            category="filesystem",
            required_capabilities=["file:write"],
        )

    def execute(self, **params: Any) -> ToolResult:
        # Deny before resolving a path or accessing the native backend.
        return ToolResult(
            tool_name="file_write",
            content="Direct host file access is disabled in Jarvis Assistant.",
            success=False,
        )


__all__ = ["FileWriteTool"]
