import split_img as spi
from instabot import *

bot = Bot()

# Credentials for insta account
user = "test_py2002"
passw = "testpy"

bot.login(username=user, password=passw)

# Tile images
img = spi.split('launch.jpeg', 6, 3)

# Upload loop
for i in range(17, -1, -1):
    img = "Images/launch_{}.jpeg".format(i)
    bot.upload_photo(img, caption="test")
    i -= 1
