import aiohttp
from aiohttp.resolver import AsyncResolver

async def sessions():
    resolver = AsyncResolver(
        nameservers=[
            "80.80.80.80",  # freenom
            "80.80.81.81",  # freenom
            "8.8.4.4",  # google
            "8.8.8.8",  # google
            "1.1.1.1",  # cloudflare
            "1.0.0.1",  # cloudflare
        ]
    )
    conn = aiohttp.TCPConnector(resolver=resolver)
    session = aiohttp.ClientSession() # connector=conn
    return session
