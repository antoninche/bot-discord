from __future__ import annotations

import random

import discord
from discord.ext import commands


class FunCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="roll")
    async def roll_prefix(self, ctx: commands.Context, faces: int = 6) -> None:
        faces = max(2, min(faces, 1_000))
        value = random.randint(1, faces)
        await ctx.send(f"Résultat: {value} (1..{faces})")

    @discord.app_commands.command(name="roll", description="Lance un dé (1..N).")
    @discord.app_commands.describe(faces="Nombre de faces (2 à 1000).")
    async def roll_slash(self, interaction: discord.Interaction, faces: int = 6) -> None:
        faces = max(2, min(faces, 1_000))
        value = random.randint(1, faces)
        await interaction.response.send_message(f"Résultat: {value} (1..{faces})", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(FunCog(bot))