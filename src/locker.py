from flask import Flask
import json
import gym

app = Flask(__name__)

@app.route("/")
def root():
    print("Hello, World!")
    return "Hello World!"

@app.route("/smart_locker/gym", methods=['GET'])
def register_gym_trigger():
    pass

@app.route("/smart_locker/gym/debug", methods=['GET'])
def gym_debug():
    var_dump = {}
    var_dump['last_access'] = gym.last_trigger_time

    return json.dumps(var_dump)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
