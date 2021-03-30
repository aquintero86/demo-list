import json
import sys
from db import init_db, db_session
from functions import query_row, query_obj
from model import User
from flask import g, Flask, request
from rq import Queue
from redis_conn import conn, get_results
from flask_expects_json import expects_json
import time
import requests_cache

app = Flask(__name__)      
queue  = Queue(connection=conn) 
#cache control
requests_cache.install_cache('cache', backend='sqlite', expire_after=180)


schema = {
    'type': 'object',
    'properties': {
        'firstName': {'type': 'string'},
        'lastName': {'type': 'string'},
        'email': {'type': 'string'},
        'id': {'type': 'number'},
        'row': {'type': 'number'},
        'num_page': {'type': 'number'}
    },
    'required': ['row', 'num_page']
}
@app.route('/', methods = ['POST'])
@expects_json(schema)
def listUsers():     
    data = request.get_json()
    json_data = get_results(str(data))
    #validate if the record exists in redis
    if json_data is not None and  json_data["description"] is not None and json_data["description"] != "":
        result = json_data["description"]
    #if the record does not exist, it makes the query and saves it in redis
    else :
        ob =  query_obj(data)
        item_list = query_row(ob)   
        result = json.dumps(item_list)
        job = queue.enqueue(
            str(json.dumps(item_list)), job_id=str(data), result_ttl=500       
        )
    return result

# This gets called after each request
@app.teardown_request
def teardown_request(response_or_exc):
    db_session.remove()

# This never gets called after requests
@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    db_session.remove()

if __name__ == '__main__': 
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
