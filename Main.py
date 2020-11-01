import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '%', intents = intents)
client.remove_command("help")

def simpleEmbed(s):
	embed = discord.Embed(
	    color=discord.Colour.green(),
	    description=s,
	)
	return embed

@client.event
async def on_ready():
	activity = discord.Activity(name="<guild_name>", type=1)
	await client.change_presence(status=discord.Status.online, activity=activity)
	print("Bot is ready!")

@client.event
async def on_member_join(member):
	channel = client.get_channel(123456789101112131) #channel_id of the channel you want the message to be displayed

	embed = discord.Embed(title= f"WELCOME TO **{member.guild.name}**", description= f"WELCOME TO OUR SERVER {member.mention}! HOPE YOU ENJOY HERE!", colour = discord.Colour.blue())
	embed.add_field(name = f"READ ALL THE RULES FROM :", value = f"<#channel_id>", inline = False)
	embed.add_field(name = f"TO GET TO KNOW ABOUT THE SERVER :", value = f"<#channel_id>", inline = False)
	embed.set_footer(text = "<guild_name> OFFICIAL BOT")
	embed.set_thumbnail(url = member.avatar_url)#any sort of embeds can be used, I use this one

	await channel.send(embed = embed)

@client.event
async def on_member_remove(member):
	channel = client.get_channel(123456789101112131) #channel_id of the channel you want the message to be displayed
	await channel.send(f"=================================\n{member.display_name} just left the server <byebyeemoji> \nWe will miss you! \nHope to see you again soon \n=================================")

client.run("<bot_token>")