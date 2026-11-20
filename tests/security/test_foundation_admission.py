"""Foundation admission must run before tool argument parsing or dispatch."""

from unittest.mock import MagicMock

from openjarvis.core.types import ToolCall
from openjarvis.tools._stubs import ToolExecutor


def test_unapproved_tool_is_not_exposed_or_executed():
    tool = MagicMock()
    tool.spec.name = "web_search"
    executor = ToolExecutor([tool], agent_id="synthetic-agent")
    assert executor.available_tools() == []
    assert executor.get_openai_tools() == []
    result = executor.execute(ToolCall(id="test", name="web_search", arguments="INVALID_PRIVATE_CANARY"))
    assert not result.success
    assert result.tool_name == "blocked_tool"
    assert "PRIVATE_CANARY" not in result.content
    tool.execute.assert_not_called()
