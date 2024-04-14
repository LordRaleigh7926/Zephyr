from discord import * 
import random
from jokeapi import  Jokes
from discord.ext import commands
import art
import requests
import json

TOKEN = 'MTEzMjE1NjI1NTU3NDcwODI1NA.GCrL4z.21_s09l8FA6GY_Ik-duLiCEh-KsMcxRkZBwj10'

client = commands.Bot(intents=Intents().all(), command_prefix="!")
@client.event
async def on_ready():
    art.tprint(f"{client.user}   online")

@client.command(help="Returns kill statement of a person")
async def kill(ctx,*, name):
    
    kill_list = [
        "was killed by Lord Rama in Ramayana.",
        "tried to swim in lava.",
        "was pricked to death.",
        "experienced Kinetic Energy. Probably didn't learn Physics properly.",
        "blew up!",
        "drowned in the sink.",
        "was blown up by TNT.",
        "was killed by [Intentional Game Design].",
        "hit the ground too hard.",
        "fell from a high place.",
        "fell off a ladder.",
        "was impaled on a stalagmite.",
        "was squashed by a falling anvil.",
        "was squashed by a falling block.",
        "was skewered by a falling stalactite.",
        "went up in flames.",
        "burned to death.",
        "walked into fire whilst fighting 'INEVITABLE death'.",
        "was burnt to a crisp whilst fighting Thanos. Sad that the kiddo thought he had a chance to beat him.",
        "went off with a BANG! #SayNoToCrackers",
        "was struck by lightning.",
        "discovered the floor was lava.",
        "was killed by magic.",
        "froze to death.",
        "was stung to death.",
        "was obliterated by a sonically-charged shriek.",
        "starved to death.",
        "suffocated in a wall.",
        "was squished too much.",
        "was squashed by pet toy.",
        "was poked to death by a sweet berry bush.",
        "fell out of the world.",
        "didn't want to live in the same world as death.",
        "withered away.",
        "died from dehydration.",
        "was roasted in dragon breath.",
        "was doomed to fall.",
        "was too soft for this world.",
        "blasted",
        "died from too much caffiene",
        "ate mentos after drinking coke",
        "died from depression",
        "committed suicide"]
    
    kill_choice = random.choice(kill_list)

    await ctx.message.channel.send(f"{name} {kill_choice}")

@client.command(help="Returns kill statement of a person 10 times")
async def bulkkill(ctx,*, name):
    
    kill_list = [
        "was killed by Lord Rama in Ramayana.",
        "tried to swim in lava.",
        "was pricked to death.",
        "experienced Kinetic Energy. Probably didn't learn Physics properly.",
        "blew up!",
        "drowned in the sink.",
        "was blown up by TNT.",
        "was killed by [Intentional Game Design].",
        "hit the ground too hard.",
        "fell from a high place.",
        "fell off a ladder.",
        "was impaled on a stalagmite.",
        "was squashed by a falling anvil.",
        "was squashed by a falling block.",
        "was skewered by a falling stalactite.",
        "went up in flames.",
        "burned to death.",
        "walked into fire whilst fighting 'INEVITABLE death'.",
        "was burnt to a crisp whilst fighting Thanos. Sad that the kiddo thought he had a chance to beat him.",
        "went off with a BANG! #SayNoToCrackers",
        "was struck by lightning.",
        "discovered the floor was lava.",
        "was killed by magic.",
        "froze to death.",
        "was stung to death.",
        "was obliterated by a sonically-charged shriek.",
        "starved to death.",
        "suffocated in a wall.",
        "was squished too much.",
        "was squashed by pet toy.",
        "was poked to death by a sweet berry bush.",
        "fell out of the world.",
        "didn't want to live in the same world as death.",
        "withered away.",
        "died from dehydration.",
        "was roasted in dragon breath.",
        "was doomed to fall.",
        "was too soft for this world.",
        "blasted",
        "died from too much caffiene",
        "ate mentos after drinking coke",
        "died from depression",
        "committed suicide",
        "was blood drained",
        "'s skull was smashed",
        "didn't deserve to live"]
    
    for i in range(10):
        kill_choice = random.choice(kill_list)

        await ctx.message.channel.send(f"{name} {kill_choice}")

@client.command(name="ping", help="Gives the latency of Zephyr")
async def latency_check(ctx):
    await ctx.message.channel.send(f"Pong {round(client.latency*1000)}ms")

@client.command(name="clsmg", help="Clears the said number of messages. 🧹")
async def clear_messages(ctx, amount=6):
    await ctx.channel.purge(limit=amount)


@client.command(name="djoke", help="Gives a dark joke.")
async def jokes(ctx):
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(category=["dark"])  # Retrieve a dark joke
    if joke["type"] == "single": # Print the joke
        await ctx.message.channel.send(joke["joke"])
    else:
        await ctx.message.channel.send(f"{joke['setup']}\n{joke['delivery']}")

@client.command(name="joke", help="Gives a random joke.")
async def jokes(ctx):
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke(blacklist=["racist"])  # Retrieve a random joke
    if joke["type"] == "single": # Print the joke
        await ctx.message.channel.send(joke["joke"])
    else:
        await ctx.message.channel.send(f"{joke['setup']}\n{joke['delivery']}")

@client.command(name="quote", help="Provides a random quote. To enlighten you.")
async def famous_quote(context):

    raw_quote= requests.get('https://api.api-ninjas.com/v1/quotes?', headers={'X-Api-Key': 'QHQV2FPEoe5xGbKRT9CsBA==Q5GpB1bEY6eY11BV'}).json()
    print(raw_quote)
    raw_sentence = raw_quote[0].get("quote")
    authorQuote = raw_quote[0].get("author")
    QUOTE = f"{raw_sentence} \n\n"

    quote_embed = Embed(title=QUOTE,  description=f"- {authorQuote}", color=0x3d5884)

    await context.message.channel.send(embed=quote_embed)


client.run(TOKEN)