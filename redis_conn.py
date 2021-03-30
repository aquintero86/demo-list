import os
import json
import redis
from rq import Worker, Queue, Connection
from rq import Queue
from rq.job import Job

listen = ['default']
redis_url = os.getenv('REDISTOGO_URL', 'redis://redis:6379')
conn = redis.from_url(redis_url)

#query redis by job_id if not exist the value return None
def get_results(job_key):    
    try :
        job = Job.fetch(job_key, connection=conn)
        data_string =json.dumps(job.to_dict(), indent=2, default=str)
        result = json.loads(data_string)
    except : 
        result = None
    return result

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()