from flask import Flask, jsonify, request

app = Flask(__name__)

def add_numbers(*args) :
    res = 0;
    for arg in args :
        res += arg
    return res    

@app.route("/api/add" , methods=["GET","POST"])
def add_route() :
    
    if request.method == "GET":
        num1 = request.args.get("num1",type=float)
        num2 = request.args.get("num2",type=float)
        
        if num1 is None or num2 is None:
            return jsonify({"Error" : "Please provide num1 and num2 as query params"}), 400
        
        return jsonify({"sum":add_numbers(num1,num2)})
    
    if request.method == "POST" : 
        data = request.get_json()
        if not data or "num1" not in data or "num2" not in data:
            return jsonify({"error" : "Please provide num1 and num2 in JSON body"}), 400
        num1 = data["num1"]
        num2 = data["num2"]
        
        try :
            total = add_numbers(float(num1),float(num2))
        except ValueError:
            return jsonify({"error" : "num1 and num2 must be numbers"}), 400    

        return jsonify({"Sum" : total})


if __name__ == "__main__":
    app.run(debug=True)
