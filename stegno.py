from PIL import Image
import stepic
from flask import Flask,render_template,request,flash,send_from_directory,send_file
import os

app=Flask(__name__)
app.secret_key="123"


app.config['UPLOAD_FOLDER']="/home/smart/Desktop/mini_project/"

@app.route('/')
def home():
	return render_template("home.html")

@app.route("/encode",methods=['GET','POST'])
def encode():
    if request.method=='POST':
        upload_image=request.files['upload_image']
        en_data=request.form['encode_data']

        if upload_image.filename!='':
            #filepath=os.path.join(app.config["UPLOAD_FOLDER"],upload_image.filename)
            upload_image.save(upload_image.filename)
            ##Open Image or file in which you want to hide your data
            im = Image.open(upload_image.filename)
            #Encode some text into your Image file and save it in another file
            en=bytes(en_data, 'utf-8')
            im1 = stepic.encode(im,en)
            #ex=upload_images.filename
            im1.save('test.png', 'PNG')
            os.remove(upload_image.filename)
            flash("Hide Data successfully","success")
    return render_template("encode.html")        
 
@app.route('/download')
def download_file():
	global file_name
	file_name=app.config['UPLOAD_FOLDER']+'test.png'
	return send_file(file_name,as_attachment=True)
	
@app.route('/decode',methods=['GET','POST'])		 
def decode():
    #
    if request.method=='POST':
        upload_image=request.files['upload_image']

        if upload_image.filename!='':
            #filepath=os.path.join(app.config["UPLOAD_FOLDER"],upload_image.filename)
            upload_image.save(upload_image.filename)
	        #Decode the image so as to extract the hidden data from the image
            im2 = Image.open(upload_image.filename)
            stegoImage = stepic.decode(im2)
            flash(stegoImage,"success")
    return render_template("decode.html")    
    #print(stegoImage)


if __name__ == '__main__':
    app.run(debug=True)

	
