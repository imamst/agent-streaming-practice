from app.prompt import SYSTEM_PROMPT
from openai.types.responses import ResponseTextDeltaEvent
from app.tools import search_web
from app.llm import llm_model
from agents import Agent, RawResponsesStreamEvent, Runner, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled(True)


async def main():
    agent: Agent = Agent(
        name="Assistant",
        instructions=SYSTEM_PROMPT,
        model=llm_model,
        tools=[search_web],
    )

    runner = Runner.run_streamed(agent, input="Hey!")

    async for event in runner.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event, RawResponsesStreamEvent
        ):
            if isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
