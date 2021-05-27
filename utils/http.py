import aiohttp
from aiohttp.resolver import AsyncResolver
async def sessions():
    resolver = AsyncResolver(
        nameservers=[
            "80.80.80.80",
            "80.80.81.81",
            "8.8.4.4",
            "8.8.8.8",
            "1.1.1.1",
            "1.0.0.1",
        ]
    )
    conn = aiohttp.TCPConnector(resolver=resolver)
    session = aiohttp.ClientSession(connector=conn)
    return session
