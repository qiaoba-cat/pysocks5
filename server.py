import asyncio
import logging
from asyncio import StreamReader, StreamWriter
from typing import Tuple

from exceptions import AuthException, ForwardException, RequestException


class Socks5Server:
    """
    SOCKS5 server
    """

    async def start_server(self, host: str, port: int) -> None:
        server = await asyncio.start_server(self._client_connected, host, port)
        logging.info(f"Server started on: {host}:{port}")
        async with server:
            await server.serve_forever()

    async def _client_connected(self, reader: StreamReader, writer: StreamWriter) -> None:
        try:
            await self._auth(reader)
            target_reader, target_writer = await self._request(reader, writer)
            await self._forward(reader, writer, target_reader, target_writer)
        except AuthException as auth_exec:
            pass
        except RequestException as request_exec:
            pass
        except ForwardException as forward_exec:
            pass
        except Exception as e:
            logging.exception("Error occur, ignoring.", exc_info=e)
        finally:
            writer.close()
            await writer.wait_closed()

    async def _auth(self, reader: StreamReader) -> None:
        try:
            pass
        except Exception as e:
            logging.exception("Error authing client")
            raise AuthException()

    async def _request(self, reader: StreamReader, writer: StreamWriter) -> Tuple[StreamReader, StreamWriter]:
        try:
            pass
        except Exception as e:
            logging.exception("Error request")
            raise RequestException()

    async def _forward(self, reader: StreamReader, writer: StreamWriter, target_reader: StreamReader, target_writer: StreamWriter) -> None:
        try:
            pass
        except Exception as e:
            logging.exception("Error forward")
            raise ForwardException()
