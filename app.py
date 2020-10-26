from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
# debug set to true for auto restarting server or use app.run(debug = True)
app.debug = True
#@app.route("/", methods=['GET'])
#def homePage():
    #msg = jsonify({'message':'My msg'})
   # return render_template('home.html')
@app.route("/", methods=['GET', 'POST'])
def getDataString():
    if request.method == 'POST':
        dataStr = request.form.get('data-string')
    else:
        dataStr = ""
        #return "Your data is: "+dataStr
    return render_template('home.html', data=dataStr)

if __name__ == '__main__':
    app.run()
