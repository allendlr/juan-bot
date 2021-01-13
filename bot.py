import discord
import j_database
from discord.ext import commands
from discord.ext.commands import CommandNotFound
token = "" #Enter bot token here
client = commands.Bot(command_prefix= "j.")
database = j_database.Database()
def get_info(user_id):
    info, inDatabase = database.query(user_id)
    return info, inDatabase
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        cont = ":exclamation: Commands: \n" \
               ":small_orange_diamond: j.do [task]\n" \
               ":small_orange_diamond: j.todo\n" \
               ":small_orange_diamond: j.done [number]\n"
        embed = discord.Embed(
            title=":cowboy:Invalid Command:x:",
            description=cont,
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('j.commands'))
@client.command()
async def commands(ctx):
    cont = ":exclamation: Commands: \n" \
           ":small_orange_diamond: j.gawa [task]\n" \
           ":small_orange_diamond: j.gawain\n" \
           ":small_orange_diamond: j.tapos [number]\n"
    embed = discord.Embed(
        title=":cowboy: Mga commands",
        description=cont,
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)
    print("Wrong Command")
@client.command()
async def gawa(message, *todo):
    author = message.author.id
    try:
        info, inDatabase = get_info(author)
    except:
        info, inDatabase = "None", False
    print(info, inDatabase)
    count = 0
    if todo:
        print("hello")
        if inDatabase == False:
            parse = ""
            for words in todo:
                if count < len(todo) - 1:
                    parse += words + " "
                else:
                    parse += words
                count += 1
            print("added")
            database.insert(str(author), parse)
            embed_message = parse
        else:
            parse = info + "323-"
            embeds = ""
            for words in todo:
                if count < len(todo) - 1:
                    parse += words + " "
                    embeds += words + " "
                else:
                    parse += words
                    embeds += words
                count += 1
            database.update(str(author), parse)
            embed_message = embeds
        embed = discord.Embed(
            title=":cowboy: Ang Idinagdag mo sa Listahan :bookmark: : ",
            description=embed_message,
            color=discord.Colour.blue()
        )
        embed_author = message.author
        embed.set_author(name=embed_author)
        await message.channel.send(embed=embed)
    else:
        cont = ":exclamation: Commands: \n" \
               ":small_orange_diamond: j.gawa [task]\n" \
               ":small_orange_diamond: j.gawain\n" \
               ":small_orange_diamond: j.tapos [number]\n"
        embed = discord.Embed(
            title=":cowboy: Maglagay ng Gawain",
            description=cont,
            color=discord.Colour.blue()
        )
        embed_author = str(message.author)
        embed.set_author(name=embed_author)
        await message.channel.send(embed=embed)
@client.command()
async def gawain(message):
    author = message.author.id
    try:
        info, inDatabase = get_info(author)
        if inDatabase:
            todo = database.get_list(str(author))
            if todo:
                todoList = todo.split("323-")
                parse = ""
                for i in range(len(todoList)):
                    parse += str(i+1) +".) " + todoList[i] + "\n"

                embed = discord.Embed(
                    title=":cowboy: Mga takdang gawain mo :bookmark: : ",
                    description=parse,
                    color=discord.Colour.blue()
                )
                embed_author = str(message.author)
                embed.set_author(name=embed_author)
                await message.channel.send(embed=embed)
            else:
                database.delete(str(author))
                cont = ":exclamation: Commands: \n" \
                       ":small_orange_diamond: j.gawa [task]\n" \
                       ":small_orange_diamond: j.gawain\n" \
                       ":small_orange_diamond: j.tapos [number]\n"
                embed = discord.Embed(
                    title=":cowboy: Wala kang takdang gawain",
                    description=cont,
                    color=discord.Colour.blue()
                )
                embed_author = str(message.author)
                embed.set_author(name=embed_author)
                await message.channel.send(embed=embed)
    except:
        cont = ":exclamation: Commands: \n" \
               ":small_orange_diamond: j.gawa [task]\n" \
               ":small_orange_diamond: j.gawain\n" \
               ":small_orange_diamond: j.tapos [number]\n"
        embed = discord.Embed(
            title=":cowboy: Wala kang takdang gawain",
            description=cont,
            color=discord.Colour.blue()
        )
        embed_author = str(message.author)
        embed.set_author(name=embed_author)
        await message.channel.send(embed=embed)
@client.command()
async def tapos(message, position):
    author = message.author.id
    try:
        info, inDatabase = get_info(str(author))
    except:
        info, inDatabase = "None", False
        cont = ":exclamation: Commands: \n" \
               ":small_orange_diamond: j.gawa [task]\n" \
               ":small_orange_diamond: j.gawain\n" \
               ":small_orange_diamond: j.tapos [number]\n"
        embed = discord.Embed(
            title=":cowboy: Wala kang takdang gawain",
            description=cont,
            color=discord.Colour.blue()
        )
        embed_author = str(message.author)
        embed.set_author(name=embed_author)
        await message.channel.send(embed=embed)
    if inDatabase:
        try:
            todo = database.get_list(str(author))
            todoList = todo.split("323-")
            if int(position) > len(todoList):
                cont = ":exclamation: Commands: \n" \
                       ":small_orange_diamond: j.gawa [task]\n" \
                       ":small_orange_diamond: j.gawain\n" \
                       ":small_orange_diamond: j.tapos [number]\n"
                embed = discord.Embed(
                    title=":cowboy: Lumagpas ka sa Listahan",
                    description=cont,
                    color=discord.Colour.blue()
                )
                embed_author = str(message.author)
                embed.set_author(name=embed_author)
                await message.channel.send(embed=embed)
            else:
                popped = todoList.pop(int(position) - 1)
                parse = ""
                count = 0
                for i in range(len(todoList)):
                    if count < len(todoList) - 1:
                        parse += todoList[i] + "323-"
                    else:
                        parse += todoList[i]
                    count += 1
                database.update(str(author), parse)
                embed = discord.Embed(
                    title=":cowboy: Tapos ka na mag:",
                    description="\"" + popped + "\"",
                    color=discord.Colour.blue()
                )
                embed_author = str(message.author)
                embed.set_author(name=embed_author)
                await message.channel.send(embed=embed)
                if parse == "":
                    database.delete(str(author))
        except:
            cont = "\"Gumamit lamang ng numero!\"\n\n"\
                   ":exclamation: Commands: \n" \
                   ":small_orange_diamond: j.gawa [task]\n" \
                   ":small_orange_diamond: j.gawain\n" \
                   ":small_orange_diamond: j.tapos [number]\n"
            embed = discord.Embed(
                title=":cowboy: Maling Argumento",
                description=cont,
                color=discord.Colour.blue()
            )
            embed_author = str(message.author)
            embed.set_author(name=embed_author)
            await message.channel.send(embed=embed)
client.run(token)
