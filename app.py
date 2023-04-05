from flask import Flask, render_template, request
# from flask_ngrok import run_with_ngrok

import update_2 as u
import pneumonia_model as pm

app = Flask(__name__)
# run_with_ngrok(app)


@app.route("/")
def hello():
    return render_template("index.html") 

@app.route("/sub", methods = ["GET","POST"] )
def submit():
    fp= None
    hp= None
    sp= None
    pp= None

    if request.method == "POST":
        temp1 = int(request.form['temp'])
        fever_pred = u.fever_model(temp1)
        fp = fever_pred

    if request.method == "POST":
        oxygen1 = float(request.form['oxygen'])
        hypoxia_pred = u.hypoxia_model(oxygen1)
        hp = hypoxia_pred

    if request.method == "POST":
        pulse1 = int(request.form['pulse'])
        stress_pred = u.stress_model(pulse1)
        sp = stress_pred

    if request.method == 'POST':
        temp1 = int(request.form['temp'])
        oxygen1 = float(request.form['oxygen'])
        if temp1 and oxygen1:
            pneumonia_pred = pm.pneumonia_model(temp1, oxygen1)
            pp = pneumonia_pred
        
    return render_template("sub.html", fp1=fp, hp1=hp, sp1=sp, pp1=pp) 


if __name__ ==  "__main__":
    app.run()


