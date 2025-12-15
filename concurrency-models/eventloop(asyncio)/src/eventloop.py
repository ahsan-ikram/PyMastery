# Core Library for asynchronous programming in Python
import asyncio


async def sample_couroutine() -> None:
    print("Sample couroutine started ...")
    for i in range(5):
        print(f"Sample couroutine working on iteration {i}")
        await asyncio.sleep(1)
    print("Sample couroutine ended!")


# Event loop to run the couroutine
asyncio.run(sample_couroutine())
