from flask import Flask, request
import db

app = Flask(__name__)

# print(db.getWatchList('a'))
# print('hi')

@app.route('/new-account', methods = ['POST'])
def addUser():
    email = request.form['email']
    password = request.form['password']
    status = db.addUser(email, password)
    return {'status': status}


@app.route('/delete-account', methods = ['POST'])
def deleteUser():
    email = request.form['email']
    status = db.removeUser(email)
    return {'status': status}


@app.route('add-item', methods = ['POST'])
def addItem():
    # user should only be adding new items 
    # updating should be done automatically everyday
    email = request.form['email']
    item_name = request.form['item_name']
    options = request.form['options']
    status = db.addItem(email, item_name, options)
    return {'status': status}

@app.route('/remove-item', methods = ['POST'])
def deleteItem():
    email = request.form['email']
    item_name = request.form['item_name']
    status = db.removeItem(email, item_name)
    return {'status': status}

@app.route('/get-watch-list', methods = ['POST'])
def getWatchList():
    email = request.form['email']
    watchList = db.getWatchList(email)
    return {'watch_list': watchList}
