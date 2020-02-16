from aio2ch import Api

import asyncio


async def main():
    async with Api(api_url='https://2ch.hk') as client:
        # get board threads with this method
        # pass return_status=True if you want status to be returned as well
        status, threads = await client.get_board_threads(board='b', return_status=True)
        print(status)   # should be 200 on success

        # search for threads with keywords
        keywords_threads = await client.get_board_threads(board='test', keywords=['keywords', 'to', 'search', 'for'])

        # ok, we know for sure that this thread (https://2ch.hk/test/res/30972.html) has some media in it, lets get it
        thread_media = await client.get_thread_media(30972, 'test')

        # thread_media is a list of Files, lets save them to our folder (make sure it exists first)
        await client.download_thread_media(thread_media, save_to='./downloads')

    # if python3.7 you can use asyncio.run() instead of get_event_loop() etc

asyncio.get_event_loop().run_until_complete(main())
