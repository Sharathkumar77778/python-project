# pip install pysapphire

from flask import Flask,render_template,request,send_file,redirect,flash
import os
from werkzeug.utils import secure_filename
import processing
import pysapphire

f_path  = "static/uploads"


def save_file(obj):
    filename = 0
    lis = os.listdir("static/uploads")
    print(lis)
    for i in lis:
        os.remove("static/uploads/"+str(i))
    for file in obj:
        filename = secure_filename(file.filename)  
        f_path1 = f_path
        f_path1 = os.path.join(f_path1, filename)
        if not os.path.exists(f_path1):
            file.save(f_path1)
    return filename


app = Flask(__name__)           
@app.route('/',methods=["get","post"])
def en_app():
    if request.method=="GET":
        return render_template("encrypt_.html")
    else:
        img = request.files.getlist("image")
        im_name = save_file(img)
        imgPath = processing.encrypt_image(im_name)
        print(imgPath)
        return send_file( "static/uploads/"+imgPath, as_attachment=True)


@app.route('/DEC',methods=["get","post"])
def dec_app():
    if request.method=="GET":
        return render_template("decrypt_.html")
    else:
        img = request.files.getlist("image")
        im_name = save_file(img)
        imgPath = processing.decrypt_image(im_name)
        print(imgPath)
        return send_file( "static/uploads/"+imgPath, as_attachment=True)


@app.route('/form',methods=["get","post"])
def form():
    global imgPath
    try:
        if request.method == 'POST':
            img = request.files.getlist("image")
            im_name = save_file(img)
            imgPath = processing.encrypt_image(im_name)
            print(imgPath)
            return send_file( "static/uploads/"+imgPath, as_attachment=True)

    except Exception as e:
        print(e)
    return "OK"

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=5001)