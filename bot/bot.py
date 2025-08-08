import discord
from discord.ext import commands
import dotenv
import os
import asyncio
import websockets

dotenv.load_dotenv()

intents = discord.Intents.all()
app = commands.Bot(command_prefix="sudo ", intents=intents)

@app.command()
async def kill(ctx):
    try:
        async with websockets.connect("ws://127.0.0.1:3000") as websocket:
            await websocket.send("kill")
            await ctx.send("Kill command sent to WebSocket.")
    except Exception as e:
        await ctx.send(f"Error sending WebSocket message: {e}")
    
@app.command()
async def Rejoin(ctx):
    try:
        async with websockets.connect("ws://127.0.0.1:3000") as websocket:
            await websocket.send("rejoin")
            await ctx.send("rejoin command sent to WebSocket.")
    except Exception as e:
        await ctx.send(f"Error sending WebSocket message: {e}")
    

@app.command()
async def say(ctx, *, message):
    try:
        async with websockets.connect("ws://127.0.0.1:3000") as websocket:
            await websocket.send(f'say {message}')
            await ctx.send("say command sent to WebSocket.")
    except Exception as e:
        await ctx.send(f"Error sending WebSocket message: {e}")

token = os.getenv("syntaxicalisgettingmywill")

if token:
    app.run(token)
else:
    print("Bot token not found.")
