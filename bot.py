import discord
import j_database
from discord.ext.commands import CommandNotFound
from discord.ext import commands
token = "" #Enter your bot token here
client = commands.Bot(command_prefix= "j!")
auth = []
auth2 = []
database = j_database.Database()
database.retrieve()
class toDoApp():
    def __init__(self, todo):
        self.todo = todo
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        cont = ":exclamation: Commands: \n" \
               ":small_orange_diamond: j!do [task]\n" \
               ":small_orange_diamond: j!todo\n" \
               ":small_orange_diamond: j!done [number]\n"
        embed = discord.Embed(
            title=":cowboy:Invalid Command:x:",
            description=cont,
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed)
def retrieve():
    auth2.clear()
    auth.clear()
    with open("todo.txt", 'r') as f:
        for lines in f:
            line = lines.split("-")
            content = []
            content.append(line[0])
            author = line[1][0:-1]
            if author not in auth:
                auth.append(author)
                auth2.append(toDoApp(content))
            else:
                for i in range(len(auth)):
                    if author == auth[i]:
                        auth2[i].todo.append(line[0])
def save(pos):
    with open("todo.txt", 'a') as f:
        recent = len(auth2[pos].todo) - 1
        print(recent)
        f.write(auth2[pos].todo[recent] + "-" + auth[pos] + "\n")
def rewrite(pos):
    length = len(auth2)
    with open("todo.txt", 'w') as f:
        for i in range(length):
            for x in auth2[i].todo:
                f.write(x + "-" + auth[i] + "\n")

retrieve()
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('j!commands'))
@client.command()
async def commands(ctx):
    cont = ":exclamation: Commands: \n" \
           ":small_orange_diamond: j!do [task]\n" \
           ":small_orange_diamond: j!todo\n" \
           ":small_orange_diamond: j!done [number]\n"
    embed = discord.Embed(
        title=":cowboy: Mga commands",
        description=cont,
        color=discord.Colour.blue()
    )
    await ctx.send(embed=embed)
    print("Wrong Command")
@client.command()
async def todo(message):
    retrieve()
    author = message.author
    if str(author) not in auth:
        cont = ":exclamation: Commands: \n" \
               ":small_orange_diamond: j!do [task]\n" \
               ":small_orange_diamond: j!todo\n" \
               ":small_orange_diamond: j!done [number]\n"
        embed = discord.Embed(
            title=":cowboy: Wala kang takdang gawain",
            description=cont,
            color=discord.Colour.blue()
        )
        await message.channel.send(embed=embed)
    if str(author) in auth:
        for i in range(len(auth)):
            if str(author) == auth[i]:
                parse = ""
                for x in range(len(auth2[i].todo)):
                    parse += str(x + 1) + ".) " + auth2[i].todo[x] + "\n"
                embed = discord.Embed(
                    title=":cowboy: Mga takdang gawain mo :bookmark: : ",
                    description=parse,
                    color=discord.Colour.blue()
                )
                embed_author = auth[i][0:-5]
                embed.set_author(name=embed_author)
                await message.channel.send(embed=embed)
                print("Print Todo")

@client.command()
async def do(message, *todo):
    author = message.author
    inList = False
    parse = ""
    for x in todo:
        parse += x + " "
    if parse != "":
        todoList = [parse]
        for x in auth:
            if str(author) == x:
                inList = True
        for x in range(len(auth)):
            if str(author) == auth[x]:
                position = x
        if not inList:
            auth.append(str(author))
            auth2.append(toDoApp(todoList))
        for x in range(len(auth)):
            if str(author) == auth[x]:
                position = x
        if inList:
            todoList2 = auth2[position].todo + todoList
            auth2[position].todo = todoList2
        save(position)
        embed = discord.Embed(
            title=":cowboy: Added: ",
            description="\"" + parse + "\"" +"\n\n:small_orange_diamond: **j!todo** Para tignan ang iyong listahan",
            color=discord.Colour.blue()
        )
        await message.channel.send(embed=embed)
        print("todo Added")
    else:
            cont = ":exclamation: Commands: \n" \
                   ":small_orange_diamond: j!do [task]\n" \
                   ":small_orange_diamond: j!todo\n" \
                   ":small_orange_diamond: j!done [number]\n"
            embed = discord.Embed(
                title=":cowboy: Wala kang takdang gawain",
                description=cont,
                color=discord.Colour.blue()
            )
            await message.channel.send(embed=embed)
@client.command()
async def done(message, pos):
    author = message.author
    if str(author) not in auth:
        cont = ":exclamation: Commands: \n" \
               ":small_orange_diamond: j!do [task]\n" \
               ":small_orange_diamond: j!todo\n" \
               ":small_orange_diamond: j!done [number]\n"
        embed = discord.Embed(
            title=":cowboy: Wala kang takdang gawain",
            description=cont,
            color=discord.Colour.blue()
        )
        await message.channel.send(embed=embed)
    position = int(pos)
    if str(author) in auth:
        for i in range(len(auth)):
            if str(author) == auth[i]:
                list = auth2[i].todo
                try:
                    done = list[position - 1]
                    list.pop(position - 1)
                    auth2[i].todo = list
                    rewrite(position)
                except:
                    print("wrong")
    embed = discord.Embed(
        title=":cowboy: Natapos ka nang mag: ",
        description="\"" + done + "\"" + "\n\n:small_orange_diamond: **j!todo** Para tignan ang iyong listahan",
        color=discord.Colour.blue()
    )
    await message.channel.send(embed=embed)
    print("Done Task", str(author))
    retrieve()
client.run(token)
