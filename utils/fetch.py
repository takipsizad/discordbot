import aiohttp
from . import _http as http
run = 0
class BadMethod(Exception):
  pass
class NotFound(Exception):
    pass

async def fetch(url, method="GET", **kwargs):
    if run is 0:
        session = await http.sessions()
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
