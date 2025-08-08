import os
import httpx


class ModelRouter:
    """Route prompts to different LLM providers based on MODEL_PROVIDER environment variable."""

    def __init__(self) -> None:
        self.provider = os.getenv("MODEL_PROVIDER", "openai")
        self.openai_key = os.getenv("OPENAI_API_KEY", "")
        self.ollama_host = os.getenv("OLLAMA_HOST", "")
        self.vllm_host = os.getenv("VLLM_HOST", "")
        self.lmstudio_host = os.getenv("LM_STUDIO_HOST", "")

    async def chat(self, messages: list[dict]) -> str:
        if self.provider == "openai":
            return await self._call_openai(messages)
        elif self.provider == "ollama":
            return await self._call_ollama(messages)
        elif self.provider == "vllm":
            return await self._call_vllm(messages)
        elif self.provider == "lmstudio":
            return await self._call_lmstudio(messages)
        else:
            raise ValueError(f"Unknown model provider {self.provider}")

    async def _call_openai(self, messages: list[dict]) -> str:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.openai_key}"}
        data = {
            "model": "gpt-3.5-turbo",
            "messages": messages,
            "max_tokens": 500,
        }
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json=data, headers=headers, timeout=30)
            resp.raise_for_status()
            content = resp.json()
            return content["choices"][0]["message"]["content"]

    async def _call_ollama(self, messages: list[dict]) -> str:
        url = f"http://{self.ollama_host}/api/generate"
        prompt = "\n".join([m["content"] for m in messages])
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json={"model": "llama3", "prompt": prompt})
            resp.raise_for_status()
            data = resp.json()
            return data.get("response", "")

    async def _call_vllm(self, messages: list[dict]) -> str:
        url = f"http://{self.vllm_host}/v1/chat/completions"
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json={"messages": messages})
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]

    async def _call_lmstudio(self, messages: list[dict]) -> str:
        url = f"http://{self.lmstudio_host}/v1/chat/completions"
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json={"messages": messages})
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"]