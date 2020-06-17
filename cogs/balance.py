import discord
from discord.ext import commands
from discord.utils import get
import json

class Balance(commands.Cog):
	
	def __init__(self,bot):
		self.bot = bot
	#verify commands
	@commands.command()
	async def verify(self,ctx):
		avatar = ctx.author.avatar_url_as(static_format='png')
		
		card = discord.Embed(
		colour=discord.Colour.from_rgb(129,255,129),
		title="Successfully Verified!",
		description=f"{ctx.author.mention} you are verified!"
		)
		card.set_thumbnail(url=avatar)
		userRoles = []
		for i in ctx.author.roles:
			userRoles.append(i.name)
		if "Member" in userRoles:
			card.title="Failed To Verify!"
			card.description=f"{ctx.author.mention} you are already verified!"
			card.colour=discord.Colour.from_rgb(175,0,0)
			await ctx.send(embed=card)
		else:
			await ctx.author.add_roles(get(ctx.guild.roles,id=721232101323571200))
			await ctx.send(embed=card)
	#End of verify command
	
	#Info command
	@commands.command(aliases=["i"])
	async def info(self,ctx):
		topRole = ctx.author.top_role
		card = discord.Embed(
		colour=ctx.author.colour,
		title="Info",
		description=f"Name: **{ctx.author.name}**\nIDs: **{ctx.author.id}**\nRole: **{str(topRole.name)}**"
		)
		card.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url_as(static_format='png'))
		await ctx.send(embed=card)
	
	#End of info command

def setup(bot):
	bot.add_cog(Balance(bot))