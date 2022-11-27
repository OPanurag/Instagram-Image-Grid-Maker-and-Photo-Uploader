import split_img as spi
from instabot import *

bot = Bot()

# Credentials for insta account
user = "olauncherapp"
passw = "tanujnotes123"

# Login Command
bot.login(username=user, password=passw)

# Tile image information and command
filename = 'img1'
extension = '.jpeg'
img = spi.split(filename + extension, 6, 3)

# Upload loop
for i in range(17, -1, -1):
    img = "Images/{}_{}.jpeg".format(filename, i)
    bot.upload_photo(img, caption="____####____")
    i -= 1
