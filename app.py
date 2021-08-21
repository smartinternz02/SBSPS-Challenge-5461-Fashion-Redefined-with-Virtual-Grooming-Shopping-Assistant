# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:55:05 2021

@author: user
"""

import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask , request ,render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer



'''
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
'''
app = Flask(__name__)

model = load_model("fashion.h5")

#routing the html page
#home page
@app.route('/') 
def base():
    return render_template('base.html')


#define the predicting function
@app.route('/predict',methods = ['GET','POST'])
def uploads():
    print("i am entering")
    if request.method == 'POST':
        f = request.files['image']  
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path",basepath)
        filepath = os.path.join(basepath,'uploads',f.filename)
        print("upload folder is ",filepath)
        f.save(filepath)
        img = image.load_img(filepath,target_size = (64,64))
        x = image.img_to_array(img)
        print(x)
        x = np.expand_dims(x,axis = 0)
        print(x)
        preds=model.predict_classes(x)
        print("prediction",preds)
        index = ['footwear','menswear','tshirt','watch','womenswear']
        text = "The classified clothing is : "+str(index[preds[0]])
        return text
    
if __name__=='__main__':
    app.run(debug = False,threaded =False)
