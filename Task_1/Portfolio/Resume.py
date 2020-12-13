from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/qualifications')
def qualifications():
    return render_template('qualifications.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/personalinfo')
def personalinfo():
     return render_template('/personalinfo.html')



if(__name__ == '__main__'):
    app.run(debug = True)
