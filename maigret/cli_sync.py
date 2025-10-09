import asyncio
from .__main__ import main as async_main  # upstream main is async

def main():
    asyncio.run(async_main())
