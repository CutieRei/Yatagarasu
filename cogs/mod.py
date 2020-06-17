import discord
from discord.ext import tasks,commands

class Admin(commands.Cog):
	
	def __init__(self,bot):
		self.bot = bot
	
	
	#Give role commands
	@commands.command(aliases=["gr","give","role"])
	@commands.has_role("Admin")
	async def giverole(self,ctx, member:discord.Member,role:discord.Role):
		card = discord.Embed(
		colour=discord.Colour.from_rgb(120,255,120),
		title="Success",
		description=f"Successfully give **{role.name}** to **{member.name}**"
		)
		card.set_thumbnail(url=member.avatar_url_as(static_format='png'))
		if role.name in [i.name for i in member.roles]:
			card.title="Failed"
			card.description=f"**{member.name}** Already have that role!"
			await ctx.send(embed=card)
		else:
			await member.add_roles(role)
			await ctx.send(embed=card)
	
	#kick command
	@commands.command(aliases=["k"])
	@commands.has_role("Admin")
	async def kick(self,ctx, member: discord.Member,*,reason=None):
		card = discord.Embed(
		colour=discord.Colour.from_rgb(120,255,120),
		title=f"Successfully kicked **{member}**"
		)
		avatar = self.bot.user.avatar_url
		card.set_author(name=self.bot.user.name,icon_url=avatar)
		if member.name in [i.name for i in ctx.guild.members]:
			await member.kick(reason=reason)
			await ctx.send(embed=card)
		else:
			card.title="Failed"
			card.description=f"**{member}** Does not exist!"
			await ctx.send(embed=carf)


def setup(bot):
	bot.add_cog(Admin(bot))
			