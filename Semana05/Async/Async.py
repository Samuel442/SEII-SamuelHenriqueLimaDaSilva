import asyncio

async def procura_numero():
	print('starting fetching')
	await asyncio.sleep(2)
	print('finishing fetching')
	return{'data':1}

async def print_numbers():
	for i in range(20):
		print(i)
		await asyncio.sleep(1)

async def main():
	task2 = asyncio.create_task(print_numbers())
	await procura_numero()
	await task2

asyncio.run(main())