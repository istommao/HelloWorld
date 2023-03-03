---
title: Asyncio queue
order: 10
nav:
  title: Python
  order: 1
group:
  title: 实战
  order: 1
---


```bash
pip install python-dotenv websockets
```

`Code`

```python
import asyncio
import websockets

from dotenv import load_dotenv

load_dotenv()

WEBSOCKET_URI = "<websocket address>"

async def consumers_handler(queue):
    while True:
        data = await queue.get()

        # handler data


async def producers_handler(queue):
    async with websockets.connect(WEBSOCKET_URI) as websocket:

        async for message in websocket:
            print(message)
            queue.put_nowait(message)
       

async def main():
    queue = asyncio.Queue()

    task1 =  asyncio.create_task(producers_handler(queue))
    task2 = asyncio.create_task(consumers_handler(queue))


    try:
        await asyncio.wait([task1, task2])

        await queue.join()
    except KeyboardInterrupt:
        task1.cancel()
        task2.cancel()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


```
