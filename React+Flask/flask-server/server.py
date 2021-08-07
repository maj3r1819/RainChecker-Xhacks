from flask import Flask
app = Flask(__name__)
#Members APi route
@app.route("/members")
def members():
    return {"members": ['Sagar', 'Steven', 'Frank', 'George']}

if __name__ == "__main__":
    app.run(debug=True)