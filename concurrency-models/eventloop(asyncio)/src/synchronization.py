"""
Using synchronization primitives in asyncio to manage access to shared resources.
asyncio.Lock
asyncio.Semaphore
"""

import asyncio

shared_resource: int = 0

lock = asyncio.Lock()


async def modify_shared_resource():
    """Coroutine that modifies a shared resource safely using a lock.
    Access to the shared resource is synchronized. Avoid race conditions."""
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


async def access_shared_resource_simultaneously(semaphore: asyncio.Semaphore):
    """Coroutine that access a shared resource simultaneously using a semaphore.
    Access to the shared resource is limited by the semaphore."""
    global shared_resource
    task = asyncio.current_task()

    # Limit to 2 concurrent accesses to shared resource
    async with semaphore:
        task_id = id(task)
        print(f"Accesing shared resource from task_id={task_id}")
        await asyncio.sleep(2)  # Simulate some processing delay
        print(f"Releasing shared_resource from task_id=: {task_id}")


async def main_using_lock():
    await asyncio.gather(*[modify_shared_resource() for _ in range(5)])


async def main_using_semaphores():
    # Throttle access to shared resource.
    # Don't overload shared resource access
    semaphore = asyncio.Semaphore(3)  # Limit to 3 concurrent accesses
    await asyncio.gather(
        *[access_shared_resource_simultaneously(semaphore) for _ in range(9)]
    )


async def waiter(event: asyncio.Event):
    task_id = id(asyncio.current_task())
    print(f"Waiting for event to be set. Waiter task_id={task_id}")
    await event.wait()
    print(f"Event has been set. Now continue execution in Waiter task_id={task_id}")


async def setter(event: asyncio.Event):
    task_id = id(asyncio.current_task())
    await asyncio.sleep(5)
    event.set()
    print(f"Event has been set. Setter task_id={task_id}")


async def main_using_event():
    """
    Simple event, work as boolean flag to wait for something and then continoue execution
    """
    event: asyncio.Event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))


# asyncio.run(main_using_lock())
# asyncio.run(main_using_semaphores())
asyncio.run(main_using_event())
# TODO: asyncio.run(main_using_condition())
