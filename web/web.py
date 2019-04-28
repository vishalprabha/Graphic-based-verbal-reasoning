from flask import Flask, request, render_template
app = Flask(__name__)

'''Constants (should be moved to another file) '''
IMAGE_PATH = '\\test_images\\'

''' Index page route '''
@app.route('/', methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        print("Hi upload POST call", request.args)
        file_path = IMAGE_PATH + str(request.args['file'])
        return file_path
    else:
        return '404'

if __name__ == '__main__':
    app.debug = True
    app.run()