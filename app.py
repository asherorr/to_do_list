from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_to_list')
def add_to_list():
    pass


@app.route('/view_list')
def view_list():
    pass


@app.route('/edit_list')
def edit_list():
    pass
    
    
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
    