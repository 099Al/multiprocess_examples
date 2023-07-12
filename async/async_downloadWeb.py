# SuperFastPython.com
# example of downloading a webpage over HTTPS in asyncio
import asyncio


# coroutine to construct a query and write to socket
async def http_get(writer, path, host):
    # define request
    query = f'GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n'
    # encode request as bytes
    query = query.encode()
    # write query to socket
    writer.write(query)
    # wait for the bytes to be written to the socket
    await writer.drain()


# coroutine to read a http block from a socket
async def http_read(reader):
    # read all data, decode and add to string
    data = ''
    async for line in reader:
        # decode into a string
        line = line.decode()
        # strip white space
        line = line.strip()
        # # check for end of block
        if not line:
            return data
        # store line
        data += line + '\n'


# main coroutine
async def main():
    # define the web page we want to download
    host = 'www.google.com'
    path = '/'
    # open the connection
    reader, writer = await asyncio.open_connection(host, 443, ssl=True)
    print(f'Connected to {host}')
    # issue the request
    await http_get(writer, path, host)
    print(f'Issued GET for {path}')
    # reader the header
    header = await http_read(reader)
    # report the header
    print(header)
    # read the body
    body = await http_read(reader)
    # report the details of the body
    print(f'Body: {len(body)} characters')
    # close writer stream
    writer.close()


# entry point
asyncio.run(main())