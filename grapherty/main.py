from ast import Lambda
import asyncio


async def wait_1_second():
    task = asyncio.get_event_loop().create_task(asyncio.sleep(1))

    await task
    print(1)
    await task
    print(1)
    await asyncio.sleep(1)
    await task


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.run(wait_1_second())
