from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/sendMessage', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        Mood=request.form['mood']
        num1=str(request.form['message'])
        if(Mood=='happy'):
            msg= 'Developer"s mood is'+str(num1)+' and Message is '+ num1
        if (Mood == 'excited'):
            msg = 'Developer"s mood is' + str(num1) + ' and Message is ' + num1
        if (Mood == 'inspired'):
            msg = 'Developer"s mood is' + str(num1) + ' and Message is ' + num1

        return render_template('Message.html',msg=msg,classname=Mood)




if __name__ == '__main__':
    app.run(debug=True)
