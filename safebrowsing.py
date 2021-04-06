import aiohttp
import asyncio
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
async def lookup_urls(url):
    u = url
    data = {
        "client": {
            "clientId":  "takipsiz ad bot",
            "clientVersion": "0.1"
        },
            "threatInfo": {
                "threatTypes":
                    [
                        "MALWARE",
                        "SOCIAL_ENGINEERING",
                        "THREAT_TYPE_UNSPECIFIED",
                        "UNWANTED_SOFTWARE",
                        "POTENTIALLY_HARMFUL_APPLICATION"
                    ],
                "platformTypes": platforms,
                "threatEntryTypes": ["URL"],
                "threatEntries": [{'url': u}]
            }
    },
    key = os.getenv("google_apikey")
    async with aiohttp.ClientSession() as session:
        async with session.post(f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={key}',data=data) as response:
            if response.status == 200:
                return await response.json()
            elif response.status == 400:
                raise error()
            elif response.status == 429:
                raise ratelimited()
            elif response.status == 504 or 500:
                raise error()
            else:
                raise error()