import asyncio
import os
import requests
from dotenv import load_dotenv
from roblox import Client
from time import sleep

load_dotenv()

client = Client(os.getenv("TOKEN"))
session = requests.Session()
session.cookies[".ROBLOSECURITY"] = os.getenv("TOKEN")

req = session.post(
    url="https://auth.roblox.com/"
)

if "X-CSRF-Token" in req.headers:  # check if token is in response headers
    session.headers["X-CSRF-Token"] = req.headers["X-CSRF-Token"]

currentvisits = 0

async def main():
    user = await client.get_authenticated_user()
    print("Successfully logged in as " + user.name)
    place = await client.get_place(os.getenv("PLACEID"))
    print("Visita using place " + place.name)

    while True:
        universe = await client.get_universe(place.universe.id)
        endpoint = "https://develop.roblox.com/v2/universes/"+str(place.universe.id)+"/configuration"
        global currentvisits
        global session
        
        if currentvisits != universe.visits:
            print("Update!")
            currentvisits = universe.visits
            finalname = "This place have exactly "+str(universe.visits)+" visits."
            session.patch(endpoint, data={"name": finalname})

        sleep(5)

asyncio.get_event_loop().run_until_complete(main())