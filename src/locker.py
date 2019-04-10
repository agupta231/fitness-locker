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
    return gym.trigger_gym_geofence()

@app.route("/smart_locker/gym/reset", methods=['GET'])
def reset_gym():
    return gym.reset_box()


@app.route("/smart_locker/gym/debug", methods=['GET'])
def gym_debug():
    var_dump = {}
    var_dump['last_access'] = gym.last_trigger_time.strftime("%H:%M:%S")

    return json.dumps(var_dump)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
