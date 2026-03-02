from abc import ABC, abstractmethod
from contracts.tool import ToolCall, ToolResult


class Tool(ABC):

    @abstractmethod
    def execute(self, call: ToolCall) -> ToolResult:
        pass
