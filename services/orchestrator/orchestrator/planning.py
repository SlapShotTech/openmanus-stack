from typing import List


class Planner:
    """Generate a sequence of steps from a high‑level goal.

    This skeleton uses a naive implementation: it breaks the goal into sentences.
    In a real system, you might leverage LangGraph or another LLM to generate plans.
    """

    async def plan(self, goal: str) -> List[str]:
        # Simple split by period for demonstration
        steps = [s.strip() for s in goal.split(".") if s.strip()]
        if not steps:
            steps = [goal]
        return steps