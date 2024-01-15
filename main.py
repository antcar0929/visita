import asyncio
import os
from dotenv import load_dotenv
from roblox import Client

load_dotenv()

client = Client(os.getenv("TOKEN"))
placeid = os.getenv("PLACEID")

async def main():
    user = await client.get_authenticated_user()
    print("Successfully logged in as " + user.name)
    print("Visita Place ID: " + placeid)

asyncio.get_event_loop().run_until_complete(main())