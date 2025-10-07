import time
import asyncio

async def func1():
    await asyncio.sleep(1)
    print("func 1")
    return "Enemy"

async def func2():
    await asyncio.sleep(1)
    print("func 2")
    return "Enemy2"

async def func3():
    await asyncio.sleep(3)
    print("func 3")
    return "Enemy3"

async def main():
    task = await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    print(task)

# Run the asyncio event loop
asyncio.run(main())
