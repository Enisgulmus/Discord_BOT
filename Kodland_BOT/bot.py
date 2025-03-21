import discord
from discord.ext import commands
from database import add_task_id, delete_task_id, get_all_tasks, complete_task_id


TOKEN = "YOUR TOKEN HERE" 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yaptım!")

@bot.command()
async def add_task(ctx, *, description: str):
    add_task_id(description)
    await ctx.send(f"✅ Görev eklendi: {description}")

@bot.command()
async def delete_task(ctx, index: int):
    tasks = get_all_tasks()
    if 0 < index <= len(tasks):
        task_id = tasks[index - 1][0]
        delete_task_id(task_id)
        await ctx.send(f"🗑️ Görev silindi: {index}")
    else:
        await ctx.send("❌ Geçersiz görev numarası!")


@bot.command()
async def show_tasks(ctx):
    tasks = get_all_tasks()
    if tasks:
        response = "\n".join([
            f"{i + 1} - {'✅' if task[2] else '❌'} {task[1]}" for i, task in enumerate(tasks)
        ])
    else:
        response = "📭 Hiç görev yok!"
    await ctx.send(response)

@bot.command()
async def complete_task(ctx, index: int):
    tasks = get_all_tasks()
    if 0 < index <= len(tasks):
        task_id = tasks[index - 1][0]
        complete_task_id(task_id)
        await ctx.send(f"✔️ Görev tamamlandı: {index}")
    else:
        await ctx.send("❌ Geçersiz görev numarası!")


bot.run(TOKEN)
