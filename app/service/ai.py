from openai import AsyncOpenAI


__all__ = ("AiService",)


class AiService:

    def __init__(self, config):
        self.config = config
        self.model = config.get("OPENAI_MODEL") or "gpt-5"
        args = {}
        if config.get("OPENAI_TOKEN"):
            args["api_key"] = config["OPENAI_TOKEN"]
        self.ai = AsyncOpenAI(**args)

    async def make_request(self, message: str):
        response = await self.ai.responses.create(
            model=self.model,
            input=message,
        )
        return response.output_text
