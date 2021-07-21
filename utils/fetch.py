from . import _http as http
import asyncio
loop = asyncio.get_event_loop()
session = loop.run_until_complete(http.sessions())
class BadMethod(Exception):
    pass
class NotFound(Exception):
    pass


async def fetch(url, method="GET", **kwargs):
    if method == "GET":
        response = await session.get(url, **kwargs)
    elif method == "POST":
        response = await session.post(url, **kwargs)
    else:
        raise BadMethod("Bad method")

    if response.status == 429:
        await fetch(url, method=method,**kwargs),
    elif response.status == 404:
        print(response.text)
        raise NotFound("Not found")
    else:
        return response
