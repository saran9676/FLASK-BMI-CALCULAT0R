from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    weight=request.form["1"]
    height=request.form["2"]

    weight=float(weight)
    height=float(height)

    height=height/100     # converting centimeters to meters

    BMI=weight/(height*height)

    BMI=round(BMI,2)      # rounded off to 2 decimals


    if BMI>0:
        if BMI<=16:
            return render_template("result.html", pred=f"Your Body Mass Index is {BMI}.You are severly under weight")
        elif BMI<=18.5:
            return render_template("result.html", pred=f"Your Body Mass Index is {BMI}.You are under weight")
        elif BMI<=25:
            return render_template("result.html", pred=f"Your Body Mass Index is {BMI}.You are Healthy")
        elif BMI<=30:
            return render_template("result.html", pred=f"Your Body Mass Index is {BMI}.You are over weight")
        else:
            return render_template("result.html", pred=f"Your Body Mass Index is {BMI}.You are severly over weight")
    else:
        return render_template("result.html", pred ="Enter correct details of weight and height")
if __name__ =="__main__":
    app.run(debug=True)