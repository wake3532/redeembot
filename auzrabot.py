import discord
import asyncio
from captcha.image import ImageCaptcha
import datetime
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Starting')

@client.event
async def on_message(message):
    if message.content == "!redeem 46423hcFDLKEFSUJK":
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = "Captcha.png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        embed = discord.Embed(title="좋아요. 좋은 구매에 선택입니다", description = message.author.mention + ", 매크로가 아님을 인증해주십시오 접두사를 빼고 입력하십시오", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        await message.channel.send(embed=embed)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            embed = discord.Embed(title="완료하지 못 했습니다", description = message.author.mention + " 아직 리딤 코드가 만료돼지 않았습니다. 다시 시도하십시오 ", timestamp=message.created_at,
            colour=discord.Colour.orange()
    )
            await message.channel.send(embed=embed)

        if msg.content == a:
            embed = discord.Embed(title="즐거운 젠 돼십시오", description = message.author.mention + "인증코드를 정확히 입력하셨습니다 축하합니다 \n\n 잠시만요 젠을 사용하기전 너무 많이 뽑았다 생각하면 GENR 박탈입니다 이것에 동의하면 체크 반응을 해주십시오 ", timestamp=message.created_at,
            colour=discord.Colour.green()
    )
            m = await message.channel.send(embed=embed)
            await m.add_reaction('✅')
            await m.add_reaction('❎')
            try:
                reaction, user = await client.wait_for('reaction_add', timeout = 84, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
            except asyncio.TimeoutError:
                await m.delete()
                embeds = discord.Embed(title="다시 해주십시오", description="다시 시도하십시오 \n\nPlease try again!", color=discord.Color.red())
                await message.channel.send(f"{message.author.mention}", embed=embeds)
            else:
                if str(reaction.emoji) == "❎":
                    await m.delete()
                    noembed = discord.Embed(title="", description="알겠습니다.", color = discord.Color.red())
                    await message.channel.send(f"{message.author.mention}", embed=noembed)
                elif str(reaction.emoji) == "✅":
                    await m.delete()
                    yesembed = discord.Embed(title="규칙에 동의하여 이제 당신은 GENR입니다 ", description=f"축하드립니다", color = discord.Color.green())
                    m = await message.channel.send(f"{message.author.mention}", embed=yesembed)
                    role = discord.utils.get(message.author.guild.roles, name='genr')
                    await message.author.add_roles(role)
        
        else:
                embed = discord.Embed(title="OOPS", description = message.author.mention + "인증코드가 틀립니다", timestamp=message.created_at,
                colour=discord.Colour.red()
    )
                await message.channel.send(embed=embed)
                
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
