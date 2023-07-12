import asyncio

#Reading Output From a Subprocess
async def main():
    # start executing a command in a subprocess
    process = await asyncio.create_subprocess_exec('echo', 'Hello World', stdout=asyncio.subprocess.PIPE)
    # report the details of the subprocess
    print(f'subprocess: {process}')
    # read a line of output from the program
    data, _ = await process.communicate()
    # report the data
    print(data)

asyncio.run(main())