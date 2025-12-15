import asyncio
import time


SLEEP_TIME = 2


async def fetch_api_data(*args, **kwargs) -> dict:
    print("Fetching data from api...")
    await asyncio.sleep(SLEEP_TIME)  # Simulate a network delay
    print("Data fetched from api")
    return {"API_Response": "Something from external API"}


async def fetch_local_data(*args, **kwargs) -> dict:
    print("Fetching data from local source...")
    await asyncio.sleep(SLEEP_TIME)  # Simulate processing time
    print("Data fetched from local source")
    return {"Local_Data": "Something from internal data source"}


async def await_couroutines():
    """Sequential execution of coroutines. No benefit from concurrency here."""
    print("\n\nStarting sequential execution of coroutines...")

    start: float = time.time()
    api_data = await fetch_api_data()  # Couroutine await is needed to start execution
    local_data = await fetch_local_data()
    end: float = time.time()

    print(
        f"\nAPI Response = {api_data}\nLocal Data = {local_data}\nSequential couroutines execution took {end - start} seconds.\n\n"
    )


async def await_tasks():
    """
    Tasks in asyncio are used to wrap coroutine objects and schedule them
    for concurrent execution on the event loop.

    When you call an `async def` function, you get a coroutine object that
    does nothing until awaited. Wrapping it with `asyncio.create_task()`
    turns it into a Task, which:

    - Immediately registers the coroutine with the event loop.
    - Allows multiple coroutines to run concurrently without blocking.
    - Provides lifecycle control (await, cancel, monitor).
    - Ensures exceptions are captured and surfaced properly.

    Use tasks when you want a coroutine to run in the background or when
    you need to manage multiple coroutines concurrently.
    """
    print("\n\nStarting execution of tasks...")
    task_1 = asyncio.create_task(fetch_api_data())
    task_2 = asyncio.create_task(fetch_local_data())

    start: float = time.time()
    # Awaiting the tasks allows other tasks to run concurrently
    # while waiting for their results.
    # This reduces overall execution time.
    # The tasks start executing immediately upon creation.
    # Here, both tasks run concurrently.
    # Awaiting them ensures we get their results once they complete.
    # This approach leverages concurrency effectively.
    # Better than awaiting coroutines sequentially.
    # Total time should be around the longest individual task time.
    # await can be replaced with asyncio.gather() for similar effect + clean code.

    # Await tasks to get their results
    # Better to use asyncio.gather() for cleaner code
    api_data = await task_1
    local_data = await task_2
    end: float = time.time()

    # Nice variation: Run some tasks simulatanously, other when the previous are done in case of dependencies
    # New task won't start until previous awaited tasks are done
    # Provides control to manage which tasks to run simiultaneously and which to wait for
    # api_data_again = await task_1

    print(
        f"\nAPI Response = {"api_data"}\nLocal Data = {"local_data"}\nTasks execution took {end - start} seconds.\n\n"
    )


async def gather_tasks():
    print("\n\nStarting execution of tasks using asyncio.gather for clean code...")
    start: float = time.time()
    results = await asyncio.gather(fetch_api_data(), fetch_local_data())
    end: float = time.time()

    print(f"\nTasks execution took {end - start} seconds.\n\n")

    for result in results:
        print(f"Result: {result}")


# asyncio.run(await_couroutines())
# asyncio.run(await_tasks())
asyncio.run(gather_tasks())
