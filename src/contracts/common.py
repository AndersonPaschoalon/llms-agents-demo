from dataclasses import dataclass, field
from typing import Any, Dict
from datetime import datetime
import uuid


def generate_id() -> str:
    return str(uuid.uuid4())


@dataclass
class Metadata:
    created_at: datetime = field(default_factory=datetime.utcnow)
    source: str = "unknown"
    extra: Dict[str, Any] = field(default_factory=dict)


