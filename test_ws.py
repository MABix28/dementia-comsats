
import asyncio
import websockets


async def main():
    url = "ws://127.0.0.1:8000/api/calls/ws/patient/2"

    try:
        async with websockets.connect(url) as ws:
            print("WEBSOCKET CONNECTED SUCCESSFULLY")
            await asyncio.sleep(5)

    except Exception as error:
        print("WEBSOCKET CONNECTION FAILED")
        print(type(error).__name__)
        print(str(error))


asyncio.run(main())
