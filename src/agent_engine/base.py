from abc import ABC, abstractmethod
from contracts.agent import AgentInput, AgentOutput


class AgentEngine(ABC):
    """
    Runtime cognitivo de um agente.
    """

    @abstractmethod
    def run(self, agent_input: AgentInput) -> AgentOutput:
        pass
