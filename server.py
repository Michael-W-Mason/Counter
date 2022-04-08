from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'asdjipahpiaudfhpaidosfjvnapdifuvh'

@app.route('/')         
def index():
    if 'ref' in session:
        session['ref'] +=1
    else:
        session['ref'] = 0
    if 'num' in session:
        return render_template("index.html", num = session["num"], ref = session['ref'])
    else:
        session["num"] = 0
        return render_template("index.html", num = session["num"], ref = session['ref'])

        

@app.route('/destroy_session', methods = ["POST"])
def destroy_session():
    print(request.form)
    print(request.form)
    if("click" in request.form):
        session["num"] += int(request.form["inc"])
    elif("reset" in request.form):
        session.clear()
    elif("two" in request.form):
        session["num"] += 2
    return redirect ('/')



if __name__=="__main__":   
    app.run(debug=True)    