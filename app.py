from flask import Flask, jsonify, request

app = Flask(__name__)

#default route 
@app.route("/")
def home():
    return "Hello, Kashan"

#/api/greet is the route
#methods["GET"] means it only accepts GET requests
@app.route("/api/greet",methods=["GET"])
def greet():
    data = {
        "message" : "Hello from kashan",
        "status" : "success"
        }
    return jsonify(data), 200

#Handling multiple requests
@app.route("/api/user",methods=["GET","POST"])
def user() :
    if request.method == "GET":
        return jsonify({
            "message" : "Send a post request to create a user" 
        })
        
    if request.method == "POST":
        data = request.get_json()
        return jsonify({
            "message" : f"User {data['name']} created successfully"
        }), 201    

#Creating a route /api/status that returns
#{ "service" : "Flask API" , status : "running" , "version" : "1.0.0"}

@app.route("/api/status")
def status() :
    return jsonify({
        "service" : "Flask API",
        "status" : "running",
        "version" : "1.0.0"
    })


if __name__ == "__main__":
    app.run(debug=True)