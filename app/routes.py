from flask import request, jsonify, make_response
from app import app

from app import db
from app.models import  Entry


@app.route('/')
@app.route('/index')
def index():

    return {'status': 'OK'}


@app.route('/entries', methods=['POST'])
def create_entry():
    entry = Entry(body=request.json['text'])
    db.session.add(entry)
    db.session.commit()
    return make_response(jsonify(entry))


@app.route('/entries', methods=['GET'])
def get_entries():
    entries = Entry.query.all()
    return make_response(jsonify([row for row in entries]))


@app.route('/entries/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    entry = Entry.query.get(entry_id)
    return make_response(jsonify(entry))

    # result = db.session.execute('SELECT * FROM entry WHERE id = :val', {'val': entry_id})
    # return make_response(jsonify([dict(r) for r in result]))


@app.route('/execute', methods=['POST'])
def execute():
    query = request.json['query']
    result = db.engine.execute(query)
    return make_response(jsonify([dict(r) for r in result]))
