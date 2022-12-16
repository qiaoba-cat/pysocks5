import asyncio

from server import Socks5Server


async def main():
    socks5_server = Socks5Server()
    await socks5_server.start_server('127.0.0.1', 1080)

if __name__ == "__main__":
    asyncio.run(main())
