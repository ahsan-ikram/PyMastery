import asyncio
import time

"""
Future objects represent the result of an asynchronous computation. 
They are a promise of a value that will be available in the future.
Used in low-level asyncio programming to manage and coordinate asynchronous tasks.
Not expected to be used directly in high-level asyncio code.
"""


async def set_future_value(future, value) -> None:
    await asyncio.sleep(2)  # Simulate some asynchronous operation
    future.set_result(value)
    print("Future value has been set.")
    await asyncio.sleep(5)  # Simulate some further processing after setting the result
    print(
        f"This part of the task is done after setting the future. \
        It means the task is not fully complete yet. \
        But the future is already resolved."
    )


async def main():
    # Create a Future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    start: float = time.time()
    # Create a task that will set the future's value
    asyncio.create_task(set_future_value(future, "Hello, Future!"))
    # Await the future's result. Not the same as awaiting the task.
    result = await future
    end: float = time.time()
    # Should print approximately 2 seconds. Although the task takes longer to complete.
    print(f"Time taken to get future result: {end - start} seconds")
    print(f"Future result: {result}")


asyncio.run(main())
