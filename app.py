from logging import debug
from flask import Flask, views, request, render_template, url_for
from numpy.lib import imag
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt 
import os 
from fer import FER
from send_email import send_email

# Initializing the Flask Application 
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'


@app.route('/predict', methods=["GET","POST"])
def api():
    if(request.method=="GET"):
        return render_template('index.html')
    if(request.method=="POST"):
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        img = plt.imread(secure_filename(f.filename))
        detector = FER(mtcnn=True)
        try:
            prediction=detector.top_emotion(img)
            send_email(f'Ujji is {prediction[1]*100}% {prediction[0]}')
            os.remove(secure_filename(f.filename))
            return render_template('index.html', prediction=prediction[0], score=prediction[1])
        except:
            os.remove(secure_filename(f.filename))
            return render_template('index.html', prediction="Action Could Not be Completed")
        
        
        
            

if __name__=="__main__":
    app.run(debug=True)