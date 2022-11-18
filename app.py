from flask import Flask, render_template, url_for, request, redirect
from models import db, Item, app
import datetime

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_to_list', methods=['GET', 'POST'])
def add_to_list():
    list_of_items = Item.query.all()
    if request.form:
        split_date = request.form['date'].split('-')
        year = int(split_date[0])
        month = int(split_date[1])
        day = int(split_date[2])
        date_to_submit = datetime.date(year, month, day)
        new_addition = Item(title=request.form['name'], date_created=date_to_submit)
        db.session.add(new_addition)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addtolist.html', list_of_items=list_of_items)


@app.route('/view_list')
def view_list():
    the_list = Item.query.all()
    return render_template('showlist.html', the_list=the_list)



# @app.route('/list/<id>/edit', methods=['GET', 'POST'])
# def edit_list_item(id):
#     list_items = Item.query.all()
#     item = Item.query.get_or_404(id)
#     if request.form:
#         split_date = request.form['date'].split('-')
#         year = int(split_date[0])
#         month = int(split_date[1])
#         day = int(split_date[2])
#         date_to_submit = datetime.date(year, month, day)
#         item.title = request.form['title']
#         item.date_created = date_to_submit
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('editlist.html', item=item, list_items=list_items)



    
    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
    