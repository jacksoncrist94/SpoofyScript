import random
from PIL import Image, ImageDraw, ImageFont

width = 512
height = 512

suffixList=["core","step","style","gaze","punk","wave"]
prefixList=["post-","neo-","alt-","proto-"]
wordList=["sad","doom","death","crypt","grief","ghoul","creep","sorrow","dismal"]

mode=random.randint(0,1)
suffixIndex=random.randint(0,len(suffixList)-1)
prefixIndex=random.randint(0,len(prefixList)-1)
wordIndex=random.randint(0,len(wordList)-1)

if mode == 0:
    genre = wordList[wordIndex] + suffixList[suffixIndex]
else:
    genre = prefixList[prefixIndex] + wordList[wordIndex]


message = genre
font = ImageFont.truetype('CircularStd-Medium.otf',size=80)
img = Image.open(r"cemetery.jpg")
logo = Image.open(r"spoofy_logo.png")

box=(10,10)

img.paste(logo, box, logo)

imgDraw = ImageDraw.Draw(img)

imgDraw.text((10, 410), message, font=font, fill=(255))

img.save('result.png')

img.show()