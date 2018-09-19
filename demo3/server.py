from flask import Flask
import random
import redis

r = redis.StrictRedis(host='redis', port=6379, db=0)

app = Flask(__name__)

@app.route("/")
def counter():
    rand = random.randint(1, 101)
    r.set("number", rand)
    return "the random number set into redis was %d\n" % rand

