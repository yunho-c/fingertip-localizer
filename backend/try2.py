import uvicorn
from fastapi import FastAPI

class App:
    """ Core application to test. """

    def __init__(self):
        self.api = FastAPI()
        # register endpoints
        self.api.get("/")(self.read_root)
        self.api.on_event("shutdown")(self.close)

    async def close(self):
        """ Gracefull shutdown. """

    async def read_root(self):
        """ Read the root. """
        return {"Hello": "World"}

""" Testing part."""
from multiprocessing import Process
import asynctest
import asyncio
import aiohttp

class TestApp(asynctest.TestCase):
    """ Test the app class. """

    async def setUp(self):
        """ Bring server up. """
        app = App()
        self.proc = Process(target=uvicorn.run,
                            args=(app.api,),
                            kwargs={
                                "host": "127.0.0.1",
                                "port": 5000,
                                "log_level": "info"},
                            daemon=True)
        self.proc.start()
        await asyncio.sleep(0.1)  # time for the server to start

    async def tearDown(self):
        """ Shutdown the app. """
        self.proc.terminate()

    async def test_read_root(self):
        """ Fetch an endpoint from the app. """
        async with aiohttp.ClientSession() as session:
            async with session.get("http://127.0.0.1:5000/") as resp:
                data = await resp.json()
        self.assertEqual(data, {"Hello": "World"})