import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import MagicManager2
import random

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='/' , intents=intents)


@client.event
async def on_ready():
    print(client.user.id)
    print("시작하였소")
    game = discord.Game("/도움 을 요청하시오!")

    await client.change_presence(status=discord.Status.online, activity=game)

    MagicManager2.ChangeSetting(1, 1, 30, 20, 30)
    MagicManager2.init()
    MagicManager2.RegistMagic("윙가르디움레비오우사", 10, 1, 5)
    MagicManager2.RegistMagic("루모스", 20, 3, 10)
    MagicManager2.RegistMagic("녹스", 20, 3, 10)
    MagicManager2.RegistMagic("루모스 맥시마", 30, 4, 15)
    MagicManager2.RegistMagic("루모스 솔렘", 40, 5, 20)
    MagicManager2.RegistMagic("스투페파이", 80, 20, 30)
    MagicManager2.RegistMagic("레네르바테", 80, 20, 30)
    MagicManager2.RegistMagic("붐바르다", 140, 100, 100)
    MagicManager2.RegistMagic("레파로", 1, 10, 1)
    MagicManager2.RegistMagic("리덕토", 30, 15, 15)
    MagicManager2.RegistMagic("잉고르지오", 35, 13, 15)
    MagicManager2.RegistMagic("리듀시오", 35, 13, 15)
    MagicManager2.RegistMagic("라카르눔 인플라모레", 60, 20, 20)
    MagicManager2.RegistMagic("인센디오", 30, 15, 10)
    MagicManager2.RegistMagic("모스모드레", 1000, 1000, -100000)
    MagicManager2.RegistMagic("페트리피쿠스 토탈루스", 30, 25, 20)
    MagicManager2.RegistMagic("마법추가", 0, 0, 0)
    MagicManager2.RegistMagic("서버", 0, 0, 0)
    MagicManager2.RegistMagic("프로테고", 50, 30, 0)
    MagicManager2.RegistMagic("은화", 0, 1000, 0)

    MagicManager2.RegistData("Data1", "D1", 0)
    MagicManager2.RegistData("Wand1", "W1", 0)
    MagicManager2.RegistData("Wand2", "W2", 0)
    MagicManager2.RegistData("Wnad3", "W3", 0)
    MagicManager2.RegistData("Money", "Mo", 0)


'''
@client.event
async def on_message(message):
    await client.process_commands(message)
'''


@client.event
async def on_message(message):
    ErrorMessage = ["기(氣) 가 부족합니다\n기 회복후 다시 시도해주세요", "내공이 부족합니다\n내공을 올린 후 시도해주세요"]
    LevelUpMessage = "님이 레벨업 하셨습니다"
    if message.content.startswith('/은화지급'):
        r = MagicManager2.UseMagic(message.author.id, "은화")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            author = message.guild.get_member
            MagicManager2.ChangeImformation("Mo", 10)
            await message.channel.send("<@" + str(author.id) + ">에게 은화가 지급되었다.")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/은화지급'):
        r = MagicManager2.UseMagic(message.author.id, "은화")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            text = message.content.split(" ")
            await message.channel.purge(limit=int(text[1]))
            await message.channel.send(text[1] + "개의 은화가 ")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/밝혀라"):
        r = MagicManager2.UseMagic(message.author.id, "루모스")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("느린섬광탄.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/비춰라"):
        r = MagicManager2.UseMagic(message.author.id, "루모스 맥시마")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("섬광탄.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/빛내라"):
        r = MagicManager2.UseMagic(message.author.id, "루모스 솔렘")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("섬광.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/움직여라"):
        r = MagicManager2.UseMagic(message.author.id, "윙가르디움레비오우사")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("(근처에 날아다니던 깃털 하나가 움직였소. 내공이 늘어나면 더 큰 물건을 움직일 수 있을지도 모르오.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/깨어나라'):
        r = MagicManager2.UseMagic(message.author.id, "레네르바테")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            if MagicManager2.GetImformation(message.content[9:27], "D1") == 0:
                author = message.guild.get_member(int(message.content[9:27]))
                role = discord.utils.get(message.guild.roles, name="기절")
                await author.remove_roles(role)
                await message.channel.send("<@" + str(author.id) + ">가 깨어났소!.")
            else:
                MagicManager2.ChangeImformation(message.content[9:27], "D1", 0)
                await message.channel.send("<@" + str(message.content[9:27]) + ">가 방어했소.")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/쓰러져라'):
        r = MagicManager2.UseMagic(message.author.id, "스투페파이")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            if MagicManager2.GetImformation(message.content[9:27], "D1") == 0:
                author = message.guild.get_member(int(message.content[9:27]))
                role = discord.utils.get(message.guild.roles, name="기절")
                await author.add_roles(role)
                await message.channel.send("<@" + str(author.id) + ">가 기절했소!.")
            else:
                MagicManager2.ChangeImformation(message.content[9:27], "D1", 0)
                await message.channel.send("<@" + str(message.content[9:27]) + ">가 방어했소.")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/막아라'):
        r = MagicManager2.UseMagic(message.author.id, "프로테고")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            author = message.guild.get_member(int(message.content[8:26]))
            MagicManager2.ChangeImformation(message.content[8:26], "D1", 1)
            role = discord.utils.get(message.guild.roles, name="보호막")
            await message.channel.send(
                "<@" + str(author.id) + ">에게 보호막이 생성되었소! \n (보호막은 1회용이며 자신을 겨냥한 모든 주문으로부터 보호된다오.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/터져라'):
        r = MagicManager2.UseMagic(message.author.id, "붐바르다")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            text = message.content.split(" ")
            await message.channel.purge(limit=int(text[1]))
            await message.channel.send(text[1] + "개의 대화가 파괴되었소!")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/붙어라"):
        r = MagicManager2.UseMagic(message.author.id, "레파로")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("(우연히 근처에 망가져있었던 물체가 붙었소.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/망가져라"):
        r = MagicManager2.UseMagic(message.author.id, "리덕토")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.delete()
            await message.channel.send("(메세지 1개가 망가졌소.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/레벨업"):
        r = MagicManager2.UseMagic(message.author.id, "레벨업용")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("(내가 이런 치트도 안막아놨을거같냐 멍청아)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/부풀어라"):
        r = MagicManager2.UseMagic(message.author.id, "잉고르지오")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("(지나가던 거미가 부풀었소. 으 징그러)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/쪼그라들어라"):
        r = MagicManager2.UseMagic(message.author.id, "리듀시오")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("(날아가던 참새가 작게 쪼그라들었소.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/타올라라"):
        r = MagicManager2.UseMagic(message.author.id, "라카르눔 인플라모레")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("라카르눔 인플라모레.jpg"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/불타라"):
        r = MagicManager2.UseMagic(message.author.id, "인센디오")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("인센디오.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/테스트"):
        r = MagicManager2.UseMagic(message.author.id, "테스트")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("(.)")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/모수모두래"):
        r = MagicManager2.UseMagic(message.author.id, "모스모드레")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(file=discord.File("모스모드레.gif"))
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/도술추가"):
        r = MagicManager2.UseMagic(message.author.id, "마법추가")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("조금만 기다리시오.. 업대이두 중이요..")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/서버"):
        r = MagicManager2.UseMagic(message.author.id, "서버")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("https://discord.gg/jF6s47J")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/멈춰라'):
        r = MagicManager2.UseMagic(message.author.id, "페트리피쿠스 토탈루스")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            author = message.guild.get_member(int(message.content[15:33]))
            role = discord.utils.get(message.guild.roles, name="동작그만")
            await author.add_roles(role)
            await message.channel.send("<@" + str(author.id) + ">가 석화되었소!")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/위키"):
        r = MagicManager2.UseMagic(message.author.id, "서버")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send("https://namu.wiki/w/%ED%95%B4%EB%A6%AC%ED%8F%AC%ED%84%B0%20%EB%B4%87")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith("/지팡이"):
        r = MagicManager2.UseMagic(message.author.id, "서버")
        if r == -10:
            print("함수 이름 오류")
        if r == -1:
            await message.channel.send(ErrorMessage[0])
        if r == -2:
            await message.channel.send(ErrorMessage[1])
        if r == 1 or r == 10:
            await message.channel.send(
                "``올리밴더스 - B.C. 383부터 수준 높은 지팡이를 만들어 온 전문가``\n\n지팡이 제작을 원하시면 /제작을 입력해주세요\n가격은 100갈레온입니다.\n해외구매라 안전성은 보장하지 않습니다.")
            if message.content.startswith("/제작"):
                await message.channel.send("지팡이 제작중입니다...")
        if r == 10:
            await message.channel.send("<@" + str(message.author.id) + ">" + LevelUpMessage)
    if message.content.startswith('/정보'):
        embed = discord.Embed(title=message.guild.get_member(int(message.author.id)).name + ' 도사의 정보', description="정보",
                              color=800080)
        embed.add_field(name="내공", value=str(MagicManager2.GetImformation(message.author.id, "L")), inline=False)
        embed.add_field(name="현재 기氣", value=str(MagicManager2.GetImformation(message.author.id, "M")), inline=False)
        embed.add_field(name="최대 기氣", value=str(MagicManager2.GetImformation(message.author.id, "MM")), inline=False)
        embed.add_field(name="숙련도", value=str(MagicManager2.GetImformation(message.author.id, "PE")) + "/" + str(
            MagicManager2.GetImformation(message.author.id, "NE")), inline=False)
        embed.add_field(name="총 숙련도", value=str(MagicManager2.GetImformation(message.author.id, "TE")), inline=False)
        embed.add_field(name="보호막 개수", value=str(MagicManager2.GetImformation(message.author.id, "D1")), inline=False)
        embed.add_field(name="보유 은화", value=str(MagicManager2.GetImformation(message.author.id, "Mo")), inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/도움말"):
        embed = discord.Embed(title="도움말", description="도움말이오!", color=800080)
        embed.add_field(name="어떤 주문이 있는지 알고 싶을 땐?", value="/주문 도움말", inline=False)
        embed.add_field(name="어떤 명령어가 있는지 알고 싶을 땐?", value="/명령어 도움말", inline=False)
        embed.add_field(name="만약 서버의 관리자라면?", value="/관리자 도움말", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/주문 도움말"):
        embed = discord.Embed(title="주문 도움말", description="사용가능 주문 목록이오.", color=800080)
        embed.set_thumbnail(url="https://imgur.com/EWgY5L2")
        embed.add_field(name="1내공 사용가능 주문", value="/움직여라", inline=False)
        embed.add_field(name="3내공 사용가능 주문", value="/밝혀라", inline=False)
        embed.add_field(name="4내공 사용가능 주문", value="/비춰라", inline=False)
        embed.add_field(name="5내공 사용가능 주문", value="/빛내라", inline=False)
        embed.add_field(name="10내공 사용가능 주문", value="/붙어라", inline=False)
        embed.add_field(name="13내공 사용가능 주문", value="/부풀어라", inline=False)
        embed.add_field(name="13내공 사용가능 주문", value="/쪼그라들어라", inline=False)
        embed.add_field(name="15내공 사용가능 주문", value="/불타라", inline=False)
        embed.add_field(name="15내공 사용가능 주문", value="/망가져라", inline=False)
        embed.add_field(name="20내공 사용가능 주문", value="/타올라라", inline=False)
        embed.add_field(name="25내공 사용가능 주문", value="/멈춰라", inline=False)
        embed.add_field(name="30내공 사용가능 주문", value="/쓰러져라 , /깨어나라", inline=False)
        embed.add_field(name="30내공 사용가능 주문", value="/막아라", inline=False)
        embed.add_field(name="100내공 사용가능 주문", value="/터져라", inline=False)
        embed.add_field(name="도술 추가 방법", value="/도술추가", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/명령어 도움말"):
        embed = discord.Embed(title="명령어 도움말", description="사용가능 명령어 목록입니다.", color=800080)
        embed.set_thumbnail(url="https://imgur.com/EWgY5L2")
        embed.add_field(name="사용자 정보 확인", value="/정보", inline=False)
        embed.add_field(name="마나 정보 확인", value="/기", inline=False)
        embed.add_field(name="업데이트 확인 `beta`", value="/업데이트", inline=False)
        embed.add_field(name="공식 디스코드 서버", value="/서버", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/관리자 도움말"):
        embed = discord.Embed(title="관리자 도움말", description="초기 세팅 방법입니다.", color=800080)
        embed.set_thumbnail(url="https://imgur.com/EWgY5L2")
        embed.add_field(name="봇 역할 세팅", value="관리자 권한을 봇에게 주셔야합니다.", inline=False)
        embed.add_field(name="기절 역할 세팅", value="봇의 하위 역할로 기절 역할을 만들어주시고 메세지 쓰기 및 보기를 해제해주세요.", inline=False)
        embed.add_field(name="동작그만 역할 세팅", value="봇의 하위 역할로 동작그만 역할을 만들어주시고 메세지 쓰기를 해제해주세요.", inline=False)
        embed.add_field(name="위의 두 역할 세팅", value="모든 역할은 봇의 하위 역할로 지정해야 하며 이름이 정확해야 합니다.", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/업데이트"):
        embed = discord.Embed(title="해리포터 봇(천향학당 마법봇) 업데이트", description="~~자세한 업데이트 내용은 나무위키 참조~~", color=800080)
        embed.add_field(name="`현재 버전`", value="`beta 1.0v`", inline=False)
        embed.add_field(name="~~beta 이전 업데이트~~", value="추후 공개", inline=False)
        embed.add_field(name="해리포터 봇 beta버전 공개", value="beta 1.0v", inline=False)
        embed.add_field(name="Magicmanager 0.4v 업데이트", value="beta 1.0v", inline=False)
        embed.add_field(name="Magicmanager 0.4.1v 업데이트", value="beta 1.0v", inline=False)
        embed.add_field(name="beta 1.1v 업데이트 시작", value="beta 1.1 prerelease", inline=False)
        embed.add_field(name="Magicmanager 0.4.2v 업데이트", value="beta 1.1 prerelease", inline=False)
        embed.add_field(name="Magicmanager 0.4.3v 업데이트", value="beta 1.2 prerelease", inline=False)
        embed.add_field(name="새 버전 : 천향학당 마법봇 제작", value="천향 1.0", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("/기"):
        embed = discord.Embed(title=message.guild.get_member(int(message.author.id)).name + "님의 기", description="마나",
                              color=800080)
        embed.add_field(name="현재 기", value=str(MagicManager2.GetImformation(message.author.id, "M")), inline=False)
        embed.add_field(name="최대 기", value=str(MagicManager2.GetImformation(message.author.id, "MM")), inline=False)
        await message.channel.send(embed=embed)

client.run('Nzc2NzM1Njk2MDc3NTg2NDQy.X65NfA.0HYXE_gGZjNIuOKcUoi4e-hj_XE')