import random
import sys
import io
from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route("/")
def index():
    suffixList=["core","step","style","gaze","punk","wave"," metal"]
    prefixList=["post-","neo-","alt-","proto-"]
    wordList=["sad","fear","dread","crypt","grief","ghoul","creep","sorrow","dismal"]

    cemetery='cemetery.jpg'
    forest='forest.jpg'
    subway='subway.jpg'

    imageList=[cemetery,forest,subway]


    mode=random.randint(0,1)
    suffixIndex=random.randint(0,len(suffixList)-1)
    prefixIndex=random.randint(0,len(prefixList)-1)
    wordIndex=random.randint(0,len(wordList)-1)
    imageIndex=random.randint(0,len(imageList)-1)

    if mode == 0:
        genre = wordList[wordIndex] + suffixList[suffixIndex]
    else:
        genre = prefixList[prefixIndex] + wordList[wordIndex]


    message = genre
    font = ImageFont.truetype('CircularStd-Medium.otf',size=80)
    img = Image.open(imageList[imageIndex], 'r')
    logo = Image.open(r"spoofy_logo.png")

    box=(10,10)

    img.paste(logo, box, logo)

    imgDraw = ImageDraw.Draw(img)

    imgDraw.text((10, 410), message, font=font, fill="white")

    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)