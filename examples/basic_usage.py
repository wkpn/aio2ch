from aio2ch.api import Api
import asyncio


async def main():
    api = Api()

    # we can get board threads with this method
    _, threads = await api.get_board_threads(board='test')

    # search for threads with keywords
    _, keywords_threads = await api.get_board_threads(board='test', keywords=['keywords', 'to', 'search', 'for'])

    # ok, we know for sure that this thread (https://2ch.hk/test/res/30972.html) has some media in it, lets get it
    _, thread_media = await api.get_thread_media(30972, 'test')

    # thread_media is a list of Files, lets save them to our folder (make sure it exists first)
    await api.download_thread_media(thread_media, save_to='./downloads/')

# if python3.7 you can use asyncio.run() instead of get_event_loop() etc
asyncio.get_event_loop().run_until_complete(main())
