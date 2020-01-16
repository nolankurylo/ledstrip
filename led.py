from flask import *
from background_jobs import background_one, background_two
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(2)



app = Flask(__name__)







@app.route('/rainbow')
def rainbow():
    global executor
    executor.cancel()
    executor.submit(background_one)
    return ('', 200)



        
@app.route('/rainbow_single')
def rainbow_single():
    global executor
    executor.cancel()
    executor.submit(background_one)
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
