"""Jarvis Assistant: exact-match, deny-by-default admission policy.

A grant is not authentication. Callers must supply a trusted principal and
resource identity; this module does not issue or authenticate them.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PermissionGrant:
    principal: str
    operation: str
    resource: str

    def __post_init__(self) -> None:
        for value in (self.principal, self.operation, self.resource):
            if (
                type(value) is not str
                or not value
                or len(value) > 256
                or value != value.strip()
                or any(ord(char) < 32 or ord(char) == 127 for char in value)
                or "*" in value
            ):
                raise ValueError("Invalid permission identifier")


@dataclass(frozen=True, slots=True)
class PermissionPolicy:
    grants: frozenset[PermissionGrant] = frozenset()

    def __post_init__(self) -> None:
        if type(self.grants) is not frozenset or any(
            type(grant) is not PermissionGrant for grant in self.grants
        ):
            raise ValueError("Invalid permission grants")

    def permits(self, principal: str, operation: str, resource: str) -> bool:
        try:
            request = PermissionGrant(principal, operation, resource)
        except ValueError:
            return False
        return request in self.grants


# No agent tool is approved during Foundation. No environment override.
FOUNDATION_POLICY = PermissionPolicy()
DENIAL_MESSAGE = "Tool execution is disabled pending Jarvis Foundation validation."
