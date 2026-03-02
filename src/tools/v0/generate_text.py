import os
from datetime import datetime
from typing import Dict, Any

from contracts.tool import ToolCall, ToolResult
from contracts.common import Metadata
from tools.base import Tool


class GenerateTextTool(Tool):
    """
    Tool dummy que recebe um texto e o versiona em disco.
    """

    def __init__(self, base_dir: str = "data/results/texts"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def execute(self, call: ToolCall) -> ToolResult:
        try:
            text: str = call.args.get("text", "")

            if not text:
                raise ValueError("Argumento 'text' é obrigatório.")

            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            filename = f"text_{timestamp}_{call.call_id}.txt"
            filepath = os.path.join(self.base_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)

            payload: Dict[str, Any] = {
                "content": text,
                "file_path": filepath,
                "file_name": filename,
            }

            return ToolResult(
                call_id=call.call_id,
                success=True,
                payload=payload,
                logs=None,
                metadata=Metadata(source="GenerateTextTool")
            )

        except Exception as e:
            return ToolResult(
                call_id=call.call_id,
                success=False,
                error=str(e),
                logs=None,
                metadata=Metadata(source="GenerateTextTool")
            )
