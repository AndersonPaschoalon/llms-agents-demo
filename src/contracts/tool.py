from typing import Any, Optional
from dataclasses import dataclass, field
from typing import Dict, Any

from contracts.common import generate_id
from contracts.common import Metadata


@dataclass
class ToolCall:
    """
    Solicitação de execução de uma tool.
    """
    name: str
    args: Dict[str, Any] = field(default_factory=dict)
    call_id: str = field(default_factory=generate_id)





@dataclass
class ToolResult:
    """
    Resultado da execução de uma tool.
    """
    call_id: str
    success: bool
    payload: Optional[Any] = None
    error: Optional[str] = None
    logs: Optional[str] = None
    metadata: Metadata = field(default_factory=Metadata)


