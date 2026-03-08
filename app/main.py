from app.prompt import SYSTEM_PROMPT
from openai.types.responses import ResponseFunctionToolCall, ResponseTextDeltaEvent
from app.tools import search_web
from app.llm import llm_model
from agents import (
    Agent,
    RawResponsesStreamEvent,
    Runner,
    set_tracing_disabled,
    RunItemStreamEvent,
)
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled(True)


async def main(input):
    agent: Agent = Agent(
        name="Assistant",
        instructions=SYSTEM_PROMPT,
        model=llm_model,
        tools=[search_web],
    )

    runner = Runner.run_streamed(agent, input=input)

    async for event in runner.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event, RawResponsesStreamEvent
        ):
            if isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)
        elif isinstance(event, RunItemStreamEvent) and event.name == "tool_called":
            if isinstance(event.item.raw_item, ResponseFunctionToolCall):
                print(f"[TOOL_CALL]: ${event.item.raw_item.name}")
                print(f"[TOOL_ARGUMENT]: ${event.item.raw_item.arguments}")


if __name__ == "__main__":
    import asyncio

    user_input = input("Enter your prompt: ")
    asyncio.run(main(user_input))
