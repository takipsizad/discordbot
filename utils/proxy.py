from functools import lru_cache
from .fetch import fetch
import random
async def randomproxy():
    random_var_that_no_need_to_read = await _getproxies()
    return random.choice(random_var_that_no_need_to_read)

async def __getproxies():
	response = await fetch("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=elite&simplified=true")
	varresponse = await response.text
	proxies = varresponse.split()
	return proxies