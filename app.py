from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    else:
        pass
        

@app.route("/nithya_is_awesome", methods=['GET', 'POST'])
def nithya_world():
    if request.method == "GET":
        return "<p>Hello, NITHYA!!!</p>"
    else:
        print("THIS IS POST METHOD")

if __name__ =="__main__":
    app.run(debug=True)
