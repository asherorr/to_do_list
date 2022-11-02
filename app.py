from flask import Flask, render_template, url_for
from models import db, to_do_list, app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_to_list')
def add_to_list():
    return render_template('addtolist.html')


@app.route('/view_list')
def view_list():
    pass


@app.route('/edit_list')
def edit_list():
    pass
    
    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
    