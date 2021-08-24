from flask import request, Flask, url_for, redirect, session
app = Flask("__name__")
app.secret_key = "testing"
@app.route("/sign-up", methods=['get'])
def index():
    if "email" in session:
        print("already logged in" + session["email"])
        return "logged in"
    else:
        print("not logged in")
        return "not logged in"

@app.route('/members')
def my_index():
    return {"members saj dflkasdjf;lask djf;laksd": ["hello"]}

@app.route('/testing', methods=['post'])
def test():
    for item in request.json:
        print(item)
    #print(request.form)
    session["email"] = request.json["email"]
    print(session["email"])
    x = request.json['password']
    print("hello "+ x)
    return {'return from test': x}
@app.route("/logout", methods=['get'])
def logout():
    session.pop("email", None)
    return "removed session"
if __name__ == "__main__":
    app.run(debug=True)