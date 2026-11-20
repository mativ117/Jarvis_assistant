"""Unit tests for exact-match permission policy (synthetic identities only)."""

import pytest

from openjarvis.security.foundation_policy import FOUNDATION_POLICY, PermissionGrant, PermissionPolicy


@pytest.mark.parametrize("tool", ["calculator", "shell_exec", "file_read", "http_request", "web_search", "unknown"])
def test_foundation_rejects_every_tool(tool):
    assert not FOUNDATION_POLICY.permits("agent-1", "tool:invoke", tool)


def test_exact_grant_only():
    policy = PermissionPolicy(frozenset({PermissionGrant("agent-1", "read", "workspace-1")}))
    assert policy.permits("agent-1", "read", "workspace-1")
    assert not policy.permits("agent-2", "read", "workspace-1")
    assert not policy.permits("agent-1", "write", "workspace-1")
    assert not policy.permits("agent-1", "read", "workspace-2")
    assert not policy.permits("Agent-1", "read", "workspace-1")


@pytest.mark.parametrize("bad", [None, "", "*", "agent*", " agent", "agent\n", "agent\x00", "a" * 257, 1])
def test_invalid_identifiers_fail_closed(bad):
    assert not FOUNDATION_POLICY.permits(bad, "read", "workspace-1")
    with pytest.raises(ValueError):
        PermissionGrant("agent-1", "read", bad)


def test_invalid_grant_collection_rejected():
    with pytest.raises(ValueError):
        PermissionPolicy({PermissionGrant("agent-1", "read", "workspace-1")})
    with pytest.raises(ValueError):
        PermissionPolicy(frozenset({"invalid"}))
