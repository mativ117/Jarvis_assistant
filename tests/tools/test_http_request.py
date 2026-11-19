"""Jarvis Assistant: direct HTTP denial regression tests."""

from unittest.mock import patch

import pytest

from openjarvis.tools.http_request import HttpRequestTool


@pytest.mark.parametrize(
    "params",
    [
        {},
        {"url": "https://example.invalid/SECRET_CANARY"},
        {"url": "http://127.0.0.1:9999", "method": "GET"},
        {"url": "https://example.invalid", "method": "POST", "body": "PRIVATE_CANARY"},
        {"url": "https://example.invalid", "headers": {"Authorization": "${SECRET_CANARY}"}},
    ],
)
def test_direct_http_denies_before_io(params):
    with (
        patch("socket.getaddrinfo") as dns,
        patch("socket.socket") as socket_create,
        patch("httpx.request") as request,
        patch("openjarvis._rust_bridge.get_rust_module") as native,
    ):
        result = HttpRequestTool().execute(**params)
    assert not result.success
    assert result.content == "Direct HTTP requests are disabled in Jarvis Assistant."
    for mocked in (dns, socket_create, request, native):
        mocked.assert_not_called()


def test_disabled_http_retains_contract():
    tool = HttpRequestTool()
    assert tool.spec.name == "http_request"
    assert tool.spec.requires_confirmation
    assert "network:fetch" in tool.spec.required_capabilities
