"""Jarvis Assistant: direct host file access remains disabled."""

from unittest.mock import patch

import pytest

from openjarvis.tools.file_write import FileWriteTool


@pytest.mark.parametrize("explicit_allowlist", [False, True])
def test_denied_even_with_allowlist(tmp_path, explicit_allowlist):
    target = tmp_path / "canary.txt"
    target.write_text("SYNTHETIC_SECRET_CANARY", encoding="utf-8")
    absent = tmp_path / "new.txt"
    kwargs = {"allowed_dirs": [str(tmp_path)]} if explicit_allowlist else {}
    tool = FileWriteTool(**kwargs)
    with patch("openjarvis._rust_bridge.get_rust_module") as native:
        for path in (str(target), str(absent), "", "../private.txt"):
            result = tool.execute(path=path, content="REPLACEMENT_CANARY")
            assert not result.success
            assert result.content == "Direct host file access is disabled in Jarvis Assistant."
        native.assert_not_called()
    assert target.read_text(encoding="utf-8") == "SYNTHETIC_SECRET_CANARY"
    assert not absent.exists()
    assert tool.spec.name == "file_write"
