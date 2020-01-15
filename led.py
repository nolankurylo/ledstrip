import redis
from rq import Queue
from flask import *
from background_jobs import background_one, background_two




app = Flask(__name__)
r = redis.Redis()
q = Queue(connection=r)






@app.route('/rainbow')
def rainbow():
    global q
    q.empty()
    job = q.enqueue(background_one)
    job.cancel()
    return ('', 200)



        
@app.route('/rainbow_single')
def rainbow_single():
    print rainbow_single
    global q
    q.empty()
    job = q.enqueue(background_two)
    job.cancel()
    return ('', 200)

@app.route('/reset')
def reset():
    pass




@app.route('/')
def index():
    return "index"


if __name__ == "__main__":
    
    app.run(debug=True)
    # threading._start_new_thread(rainbow, ())
    # threading._start_new_thread(rainbow_single, ())
