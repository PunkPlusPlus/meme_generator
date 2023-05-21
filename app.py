from flask import Flask, render_template, request, redirect, send_from_directory
from PIL import Image, ImageDraw, ImageFont

UPLOAD_FOLDER = './images'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    txt1 = request.form['text1']
    txt2 = request.form['text2']
    filename = 'meme4.jpeg'
    image = Image.open('./static/' + filename)
    drawer = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 14)
    drawer.text((135, 10), txt1, font=font, fill='black')
    drawer.text((135, 135), txt2, font=font, fill='black')
    image.save('./images/' + filename)
    return redirect('/images/' + filename)




if __name__ == '__main__':
    app.run()
