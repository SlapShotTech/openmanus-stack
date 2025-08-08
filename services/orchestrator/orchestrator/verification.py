class Verifier:
    """Verify the output of an execution step.

    In a full system, the verifier can run an LLM to check correctness.
    """

    async def verify(self, result: str) -> bool:
        # Placeholder: always return True for demonstration
        return True