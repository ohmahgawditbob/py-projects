import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user: # we do not want the bot to reply to itself
        return
    #Put your code here to run on every message recieved

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("------\n")

if __name__ == "__main__":
    client.run("token")