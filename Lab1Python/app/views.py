from flask import request, make_response, jsonify, abort
from app import app
from app.models import Date
import json

schedule = [
    Date('2019-03-26', 'water roses').as_json(),
    Date('2019-03-27', 'water tulips').as_json(),
    Date('2019-03-28', 'water daisies').as_json()
]


@app.route('/')
def index():
    return jsonify({'page': 'index'})


@app.route('/schedule', methods=['GET'])
def get_schedule():
    return jsonify({'schedule': schedule})


@app.route('/schedule/<int:date_id>', methods=['GET'])
def get_date(date_id):
    date = list(filter(lambda t: t['id'] == date_id, schedule))
    if len(date) == 0:
        abort(404)
    return jsonify({'date': date[0]})


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/schedule', methods=['POST'])
def create_date():
    if not request.json \
            or 'date' not in request.json \
            or 'description' not in request.json:
        abort(400)

    date = Date(
        request.json['date'],
        request.json['description']
    ).as_json()
    schedule.append(date)

    return jsonify({'date': date}), 201


@app.route('/schedule/<int:date_id>', methods=['PUT'])
def update_task(date_id):
    date = list(filter(lambda t: t['id'] == date_id, schedule))
    if len(date) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'date' in request.json and type(request.json['date']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'is_done' in request.json and type(request.json['is_done']) is not bool:
        abort(400)

    date = Date(
        request.json.get('date', date[0]['date']),
        request.json.get('description', date[0]['description']),
        request.json.get('is_done', date[0]['is_done']),
        date[0]['id']
    ).as_json()

    for i,item in enumerate(schedule):
        if item['id'] == date['id']:
            schedule.remove(item)
            schedule.insert(i, date)

    return jsonify({'date': date})


@app.route('/schedule/<int:date_id>', methods=['DELETE'])
def delete_date(date_id):
    date = list(filter(lambda t: t['id'] == date_id, schedule))
    if len(date) == 0:
        abort(404)
    schedule.remove(date[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

