from flask import Flask, request, render_template
from tinydb import TinyDB, Query
from tinydb.operations import set

import os
app = Flask(__name__)

''' Constants (should be moved to another file) '''
IMAGE_PATH = '..\\static\\test_images\\'

''' DB COnfiguration ''' 
db = TinyDB('db/db.json')

''' DB INIT '''
    # db.insert({"image_url": "", "conversation": [{"type": "sent", "message": "Hi how are you ?"}]})

''' Index page route '''
@app.route('/', methods=["GET","POST"])
def index():
    init_data = db.all()
    print(init_data)
    return render_template("index.html", data = init_data[0])

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        print("Hi upload POST call", request.args)
        file_path = IMAGE_PATH + os.path.basename(request.args['file'])
        db_query = Query()
        db.update(set("img_url", file_path), db_query.chat_id == 1)
        return file_path
    else:
        return '404'

@app.route('/converstion', methods= ['GET', 'POST'])
def converstion():
    if request.method == 'GET':
        return

if __name__ == '__main__':
    app.debug = True
    app.run()