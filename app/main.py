from app.llm import llm_model
from agents import Agent, Runner, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled(True)

def main():
    agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant", model=llm_model)

    runner = Runner.run_sync(agent, input="Hey!")

    print(runner.final_output)

if __name__ == "__main__":
    main()