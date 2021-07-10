from telethon import TelegramClient
from flask import Flask, jsonify, request, abort, redirect
import asyncio

app = Flask(__name__)
loop = asyncio.get_event_loop()
api_id = 1966275
api_hash = "be3ea29c2db2031f83e121ac2b6ffaac"
client = TelegramClient("uoplioi", api_id, api_hash)
client.start()

async def getusername(nam):
    a = await client.get_entity(nam)
    return(str(a.id))
    

@app.route("/user/<string:nam>", methods=["GET"])
def sendCode(nam):
    return loop.run_until_complete(getusername(nam))
    
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host="0.0.0.0", debug=False, port=8080, )
