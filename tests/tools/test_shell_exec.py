"""Jarvis Assistant: host shell must deny all direct calls.

The fork deliberately replaces upstream positive host-execution tests.
Any future isolated execution feature requires a separate design and tests.
"""
from __future__ import annotations

from unittest.mock import patch

import pytest

from openjarvis.tools.shell_exec import ShellExecTool


@pytest.mark.parametrize(
    "params",
    [
        {},
        {"command": ""},
        {"command": "SYNTHETIC_SECRET_CANARY"},
        {"command": "echo ok", "working_dir": "PRIVATE_PATH_CANARY"},
        {"command": "echo ok", "env_passthrough": ["PRIVATE_ENV_CANARY"]},
    ],
)
def test_host_shell_denies_before_dispatch(params):
    with (
        patch("subprocess.run") as run,
        patch("subprocess.Popen") as popen,
        patch("openjarvis._rust_bridge.get_rust_module") as native,
    ):
        result = ShellExecTool().execute(**params)
    assert not result.success
    assert result.content == "Host shell execution is disabled in Jarvis Assistant."
    run.assert_not_called()
    popen.assert_not_called()
    native.assert_not_called()


def test_disabled_shell_retains_tool_contract():
    tool = ShellExecTool()
    assert tool.tool_id == "shell_exec"
    assert tool.spec.name == "shell_exec"
    assert tool.spec.requires_confirmation
    assert "code:execute" in tool.spec.required_capabilities
    assert "env_passthrough" not in tool.spec.parameters["properties"]
