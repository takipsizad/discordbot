from . import _http as http
import asyncio
loop = asyncio.get_event_loop()
session = loop.run_until_complete(http.sessions())


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
        raise Notfound("Not found")
    return response
