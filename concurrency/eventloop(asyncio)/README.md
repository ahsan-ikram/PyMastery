# Event Loop  Asynchronous IO

- Common in JavaScript (Node.js), Python’s asyncio, and Go’s goroutines.
- Strength: Efficient for I/O‑bound tasks, lightweight concurrency.
- Weakness: CPU‑bound tasks can block the loop unless offloaded.


# Main Concepts 

## 🧩 5 Core Concepts 
-  Event Loop → the scheduler that runs everything.
- Coroutines → async functions that can pause/resume.
- Tasks → wrappers that schedule coroutines on the loop.
- Futures → low‑level objects representing a result that isn’t ready yet.
- Synchronization Primitives → semaphores, locks, events, conditions for coordinating tasks.
### The Event Loop
A single thread runs an event loop, dispatching tasks when events occur. 

```asyncio.run(main())```

### Coroutines
A coroutine is a generalized subroutine that can pause execution and later resume from the point it left off.  



- Subroutines (Normal Functions) always returns control at the end.
- Coroutines can return control midway and resume later.
- In Python a ```generator``` with ```yield``` is a coroutine
- Function starting with ```async``` keyword that can pause/resume.
```
async def api_call():
    await asyncio.sleep(1)
    print("Done.")
 ```   
### Tasks 
→ Wrappers that schedule coroutines on the loop.
### Futures
→ Low‑level objects representing a result that isn’t ready yet. 
### Synchronization Primitives

- Semaphores
- Locks
- Events
- Conditions 
- Coordinating tasks.
