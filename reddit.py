import aiohttp
import json
import discord
import random


async def reddit(subreddit):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://www.reddit.com/r/{subreddit}/new/.json?count=25",
            headers={"User-agent": "Mozilla/5.0"},
        ) as ct:
            jsonr = json.dumps(await ct.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json["data"]
            parsed_json3 = parsed_json2["children"]
            embed = discord.Embed()
            try:
                parsed_json4 = parsed_json3[random.randint(0, 25)]
            except:
                parsed_json4 = parsed_json3[random.randint(0, 15)]
            parsed_json5 = parsed_json4["data"]
            if True == parsed_json5["over_18"]:
                return embed.add_field(name="cant send +18 things ", value=":)")
            else:
                if None == parsed_json5["removed_by_category"]:
                    embed.title = parsed_json5["title"]
                    if None == parsed_json5["media"]:
                        embed.set_image(url=parsed_json5["url"])
                    else:
                        try:
                            parsed_json6 = parsed_json5["media"]
                            parsed_json7 = parsed_json6["reddit_video"]
                            embed.add_field(
                                name="video link ", value=parsed_json7["fallback_url"]
                            )
                        except:
                            pass
                    embed.set_footer(
                        text=f"Upvote ratio : {parsed_json5['upvote_ratio']}"
                    )
                    embed.add_field(
                        name="permanent link",
                        value=f"https://reddit.com{parsed_json5['permalink']}",
                    )
                    return embed
                else:
                    return embed.add_field(
                        name="post is removed ", value="try again :)"
                    )


async def randomreddit(subreddits):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://www.reddit.com/r/{random.choice(subreddits)}/new/.json?count=25",
            headers={"User-agent": "Mozilla/5.0"},
        ) as ct:
            jsonr = json.dumps(await ct.json())
            parsed_json = json.loads(jsonr)
            parsed_json2 = parsed_json["data"]
            parsed_json3 = parsed_json2["children"]
            embed = discord.Embed()
            try:
                parsed_json4 = parsed_json3[random.randint(0, 25)]
            except:
                parsed_json4 = parsed_json3[random.randint(0, 15)]
            parsed_json5 = parsed_json4["data"]
            if True == parsed_json5["over_18"]:
                return embed.add_field(name="cant send +18 things ", value=":)")
            else:
                if None == parsed_json5["removed_by_category"]:
                    embed.title = parsed_json5["title"]
                    if None == parsed_json5["media"]:
                        embed.set_image(url=parsed_json5["url"])
                    else:
                        try:
                            parsed_json6 = parsed_json5["media"]
                            parsed_json7 = parsed_json6["reddit_video"]
                            embed.add_field(
                                name="video link ", value=parsed_json7["fallback_url"]
                            )
                        except:
                            pass
                    embed.set_footer(
                        text=f"Upvote ratio : {parsed_json5['upvote_ratio']}"
                    )
                    embed.add_field(
                        name="permanent link",
                        value=f"https://reddit.com{parsed_json5['permalink']}",
                    )
                    return embed
                else:
                    return embed.add_field(
                        name="post is removed ", value="try again :)"
                    )
