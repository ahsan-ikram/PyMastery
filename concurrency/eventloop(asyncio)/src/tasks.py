import asyncio


async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a network delay
    print("Data fetched!")
    return {"data": "Sample data"}


async def process_data(data):
    print("Processing data...")
    await asyncio.sleep(1)  # Simulate processing time
    processed_data = data["data"].upper()
    print("Data processed!")
    return {"processed_data": processed_data}


async def main():
    data = await fetch_data()
    result = await process_data(data)
    print("Final Result:", result)


async def main1():
    task_1 = asyncio.create_task(fetch_data())
    task_2 = asyncio.create_task(process_data({"data": "Another sample"}))

    fetched_data = await task_1
    processed_result = await task_2

    print("Fetched Data:", fetched_data)
    print("Processed Result:", processed_result)


async def main2():

    task_1 = asyncio.create_task(fetch_data())
    task_2 = asyncio.create_task(process_data({"data": "Concurrent sample"}))

    done, pending = await asyncio.wait(
        {task_1, task_2},
        return_when=asyncio.ALL_COMPLETED,
    )

    for task in done:
        print("Task Result:", task.result())


asyncio.run(main2())
