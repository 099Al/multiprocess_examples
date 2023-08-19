# SuperFastPython.com
# example of executing a command as a subprocess with asyncio

"""
Linux
"""
import asyncio


# main coroutine
async def main():
    # start executing a command in a subprocess
    process = await asyncio.create_subprocess_exec('echo', 'Hello World')
    # report the details of the subprocess
    print(f'subprocess: {process}')


# entry point
asyncio.run(main())



#EXAMPLES

# execute a command in a subprocess
process = await asyncio.create_subprocess_exec('ls')
# execute a command with arguments in a subprocess
process = await asyncio.create_subprocess_exec('ls', '-l')

# wait for the subprocess to terminate
await process.wait()
# terminate the subprocess
process.terminate()

# start a subprocess and redirect output
process = await asyncio.create_subprocess_exec('ls', stdout=asyncio.subprocess.PIPE)

# start a subprocess and redirect input
process = await asyncio.create_subprocess_exec('ls', stdin=asyncio.subprocess.PIPE)
# send src_data to the subprocess
process.communicate(input=b'Hello\n')
"""
Behind the scenes the asyncio.subprocess.
PIPE configures the subprocess to point to a StreamReader or StreamWriter 
for sending src_data to or from the subprocess, and the communicate() 
method will read or write bytes from the configured reader.
"""


# read a line from the subprocess output stream
line = await process.stdout.readline()

#Reading Output From a Subprocess
async def main():
    # start executing a command in a subprocess
    process = await asyncio.create_subprocess_exec('echo', 'Hello World', stdout=asyncio.subprocess.PIPE)
    # report the details of the subprocess
    print(f'subprocess: {process}')
    # read a line of output from the program
    data, _ = await process.communicate()
    # report the src_data
    print(data)

#Sending Input to a Subprocess
async def main():
    # start executing a command in a subprocess
    process = await asyncio.create_subprocess_exec('cat', stdin=asyncio.subprocess.PIPE)
    # report the details of the subprocess
    print(f'subprocess: {process}')
    # write src_data to the process
    _ = await process.communicate(b'Hello World\n')