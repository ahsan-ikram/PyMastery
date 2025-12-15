import asyncio

shared_resource: int = 0

lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resource
    task = asyncio.current_task()

    # Lock help avoid race conditions
    async with lock:
        # Critical section starts
        print(f"\nCoroutine (sharing resource) called in task:(id={id(task)})")
        print(f"Current value of shared_resource: {shared_resource}")
        await asyncio.sleep(1)  # Simulate some processing delay
        shared_resource += 1
        print(f"Modified value of shared_resource: {shared_resource}")
        # Critical section ends


async def main():
    await asyncio.gather(*[modify_shared_resource() for _ in range(5)])


asyncio.run(main())
