from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/api/time",methods=["GET"])
def currTime():
    now = datetime.datetime.now().ctime()
    return jsonify({"Time":now})

if __name__ == "__main__" :
    app.run(debug=True)