---
title: Async Websocket Client
order: 10
nav:
  title: Python
  order: 1
group:
  title: 实战
  order: 1
---

```bash
pip install websockets
```

`Code`

```python
import asyncio

import websockets


async def websocket_handler(websocket_url):
    connection = websockets.connect(uri=websocket_url)

    # The client is also as an asynchronous context manager.
    async with connection as websocket:
        # await websocket.send(data)

        # resp = await websocket.recv()

        # Receives the replies.
        async for message in websocket:
            print(message)


async def main():

    websocket_url = "wss://<your websocket url>"

    task = asyncio.create_task(websocket_handler(websocket_url))

    try:
        await asyncio.wait([task])
    except KeyboardInterrupt:
        task.cancel()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
```