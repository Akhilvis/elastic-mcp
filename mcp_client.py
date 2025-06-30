import pprint
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
model = ChatOllama(model="deepseek-r1:8b")
import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "elastic": {
                "url": "http://localhost:8000/mcp",  # Ensure server is running here
                "transport": "streamable_http",
            }

        }
    )


    tools=await client.get_tools()

    print("Tools available:", tools)
    agent=create_react_agent(
        model=model,
        tools=tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "which team scored most number of penalty goals in the last world cup as per elastic data"}]}
    )

    # print("Math response:", math_response['messages'][-1].content)
    for x in math_response['messages']:
        print(x.content)    
asyncio.run(main())