from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from contracts.common import Metadata
from contracts.tool import ToolCall


@dataclass
class AgentInput:
    """
    Input recebido por um agente via AgentEngine.
    """
    objective: str
    context: Dict[str, Any] = field(default_factory=dict)
    state: Dict[str, Any] = field(default_factory=dict)
    metadata: Metadata = field(default_factory=Metadata)




@dataclass
class AgentOutput:
    """
    Output produzido por um agente.
    """
    text: str
    tool_calls: List[ToolCall] = field(default_factory=list)
    metadata: Metadata = field(default_factory=Metadata)