import asyncio


async def api_call():
    print("API request sent")
    # Mock API call
    await asyncio.sleep(1)
    print("API request finished")


async def main():
    print("Executing main")
    task = asyncio.create_task(api_call())
    # Function call return a coroutine
    # await before function call to trigger coroutine
    # await task
    print("Finished main")
    # await task

# Creating event loop
asyncio.run(main())
