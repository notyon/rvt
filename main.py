import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot import Bot, data, Database

async def reset_menfess():
    db = Database(data[0])
    x = await db.reset_menfess()
    await Bot().kirim_pesan(x=str(x))
    print('PESAN PROMOTE BERHASIL DIRESET')


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(reset_menfess, trigger="cron", hour=1, minute=0)
    scheduler.start()  

    while True:
        await asyncio.sleep(1)

Bot().run()
