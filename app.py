from flask import Flask, render_template, url_for, request, redirect
from models import db, Todo, app
import datetime

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_to_list', methods=['GET', 'POST'])
def add_to_list():
    the_list = Todo.query.all()
    if request.form:
        split_date = request.form['date'].split('-')
        year = int(split_date[0])
        month = int(split_date[1])
        day = int(split_date[2])
        date_to_submit = datetime.date(year, month, day)
        new_addition = Todo(title=request.form['name'], date_created=date_to_submit)
        db.session.add(new_addition)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addtolist.html', the_list=the_list)



@app.route('/edit_list')
def edit_list():
    pass


@app.route('/view_list')
def view_list():
    to_do_list = Todo.query.all
    return render_template('showlist.html', to_do_list=to_do_list)
    
    
    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
    