import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    champion_1 = asyncio.create_task(start_strongman('GREG', 5))
    champion_2 = asyncio.create_task(start_strongman('ALEX', 3))
    champion_3 = asyncio.create_task(start_strongman('NICK', 2))
    await champion_1
    await champion_2
    await champion_3


asyncio.run(start_tournament())
