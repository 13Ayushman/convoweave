import asyncio
import websockets
import json

async def test():
    uri = "ws://127.0.0.1:8000/ws"

    async with websockets.connect(uri) as websocket:
        data = {
            "engagement": 0.9,
            "confusion": 0.1,
            "stress": 0.2,
            "timestamp": 123456
        }

        await websocket.send(json.dumps(data))
        print("Sent:", data)

        response = await websocket.recv()
        print("Received:", response)

asyncio.run(test())
