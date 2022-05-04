from flask import render_template, redirect, request, jsonify, make_response

import csv
from datetime import datetime

from app import app
from app.forms import SearchForm

dbpath = 'app/test.csv'
db = None
db_printable = None
url = 'http://127.0.0.1:5000/'

def Load():
    global db, db_printable
    db = []
    db_printable = []
    with open(dbpath, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            row_printable = row.copy()
            row_printable[1] = datetime.utcfromtimestamp(int(row_printable[1])).strftime('%Y-%m-%d %H:%M:%S')
            db_printable.append(row_printable)
            db.append(row)

@app.route('/')
@app.route('/index')
def index():
    Load()
    return make_response(render_template('index.html', title='Table', db=db_printable), 200)

@app.route('/search', methods=['GET'])
def search():
    form = SearchForm(request.args)
    if form.validate():
        startdate = form.startdate.data
        starttime = form.starttime.data
        enddate = form.enddate.data
        endtime = form.endtime.data

        db_search = []
        global db, db_printable
        Load()
        for row, row_p in zip(db, db_printable):
            db_date = int(row[1])
            #TODO check if start < db_date < end
            db_search.append(row)

        return make_response(render_template('index.html', title='Table', db=db_search), 200)
    return make_response(render_template('search.html', title='Search', form=form), 200)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': 'Method not allowed'}), 405)

@app.errorhandler(409)
def conflict(error):
    return make_response(jsonify({'error': 'Conflict'}), 409)