from . import _http as http
session = loop.run_until_complete(http.sessions())


async def fetch(url, method="GET", **kwargs):
    if method == "GET":
        response = session.get(url, **kwargs)
    elif method == "POST":
        response = session.post(url, **kwargs)
    else:
        raise BadMethod("Bad method")
    if response == 429:
        await fetch(url, method=method,)
