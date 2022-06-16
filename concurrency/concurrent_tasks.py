import asyncio


async def even():
    print("Even starting ...")
    for i in range(10):
        if i % 2 == 0:
            print(i)
        print("Even sleeping now")
        await asyncio.sleep(0.25)
    print("Even numbers ended!")
    return {'status': 'even success'}


async def odd():
    print("Odd starting ...")
    for i in range(10):
        if i % 2 != 0:
            print(i)
        print("Odd sleeping now")
        await asyncio.sleep(0.25)

    print("Odd numbers ended!")
    return {'status': 'odd success'}


async def main():
    task_1 = asyncio.create_task(even())
    task_2 = asyncio.create_task(odd())

    future_1 = await task_1
    future_2 = await task_2

    # Telling program to finish all tasks before moving forward
    print(future_1)
    print(future_2)

asyncio.run(main())
