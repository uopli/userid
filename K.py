from telethon import TelegramClient
import asyncio

loop = asyncio.get_event_loop()
api_id = 1966275
api_hash = "be3ea29c2db2031f83e121ac2b6ffaac"
client = TelegramClient("uoplioi", api_id, api_hash)
client.start()

async def getusername(nam):
    a = await client.get_entity(nam)
    print(str(a.id))

user = str(input("Enter your user : "))
loop.run_until_complete(getusername(user))
    
