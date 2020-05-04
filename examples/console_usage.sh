#!/usr/bin/env bash

# download just images from a given thread url to a given directory
aio2ch --thread-url https://2ch.hk/b/res/219337088.html --download-folder ./here images

# download images and videos
aio2ch --thread-url https://2ch.hk/b/res/219337088.html --download-folder ./here images

# if download folder is not provided media will be saved to default folder (./aio2ch-downloads)
aio2ch --thread-url https://2ch.hk/b/res/219337088.html images videos

# short version
aio2ch -T https://2ch.hk/b/res/219337088.html -D ./here images videos

# help
aio2ch --help
