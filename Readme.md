# Flask Course

A comprehensive, text-based, industry-level course curriculum that takes a frontend React developer with general programming knowledge from beginner to expert in backend development using Flask.

The course will cover all critical topics including API development, SQL and NoSQL databases, testing, security, deployment (backend and databases), performance optimization, and include hands-on projects and capstone assignments.

# Flask Backend Mastery Course

## Module 1: Introduction to Flask + First API

---

## 🎯 Learning Objectives

By the end of this module, you will:

- Understand what Flask is and why it's popular in backend development
- Know how the **client-server model** works for web APIs
- Set up a Flask environment and install dependencies
- Create your **first API endpoint**
- Learn about **HTTP methods** and how to handle them in Flask
- Use **JSON responses** — the backbone of API communication
- Understand Flask's **development server** and how to run it

---

## Table of Contents

1. [What is Flask?](#what-is-flask)
2. [How Web Backends Work](#how-web-backends-work)
3. [Setting Up Flask](#setting-up-flask)
4. [Your First API Endpoint](#your-first-api-endpoint)
5. [Handling Multiple HTTP Methods](#handling-multiple-http-methods)
6. [Best Practices](#best-practices)
7. [Exercises](#exercises)
8. [Checkpoint](#checkpoint)

---

## What is Flask?

Flask is a **lightweight, Python-based web framework**. It's called a **microframework** because it provides only the essentials — routing, request handling, and templating — and lets you choose extra tools.

### Why developers love Flask:

- **Minimal and flexible** — no unnecessary bloat
- Easy to learn but can scale to complex apps
- Large ecosystem of extensions (auth, DB, caching, etc.)
- Perfect for **REST APIs** that React/Vue/Angular frontends can consume

> 📌 **Real-world usage**: Flask powers APIs for platforms like Netflix internal tools, Pinterest's API, and Uber's services.

---

## How Web Backends Work

Understanding the **Client-Server Model**:

### Flow:
1. **Client** (React frontend, mobile app, Postman) sends an **HTTP request** to the server
2. **Server** (Flask app) receives it, processes data (maybe queries a DB)
3. Server sends back an **HTTP response** (JSON or HTML)
4. Client renders the data or handles it

### Example:
```
React App → GET https://api.example.com/users → Flask → Database → Flask → JSON → React renders list
```

---

## Setting Up Flask

### Prerequisites
- Python 3.8+ installed on your system

### Step 1: Verify Python Installation
```bash
python3 --version
```

### Step 2: Create Project Folder
```bash
mkdir flask_course
cd flask_course
```

### Step 3: Create Virtual Environment
```bash
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### Step 4: Install Flask
```bash
pip install flask
```

### Step 5: Create `app.py`
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

### Step 6: Run Flask Server
```bash
python app.py
```

Visit: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** — you should see `"Hello, Flask!"`

---

## Your First API Endpoint

Let's create a **JSON API** instead of HTML — since JSON is the standard for API communication.

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/greet", methods=["GET"])
def greet():
    data = {
        "message": "Hello from Flask API!",
        "status": "success"
    }
    return jsonify(data), 200  # 200 = OK

if __name__ == "__main__":
    app.run(debug=True)
```

### What's happening:
- `/api/greet` is the **route** (URL path)
- `methods=["GET"]` means it only accepts GET requests
- `jsonify()` converts Python dict → JSON automatically
- The `, 200` sets the **HTTP status code**

---

## Handling Multiple HTTP Methods

Example: A route that supports both **GET** and **POST**.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/user", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        return jsonify({"message": "Send a POST request to create a user."})
    
    if request.method == "POST":
        data = request.get_json()
        return jsonify({"message": f"User {data['name']} created successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
```

### Testing POST Request in Postman:
- **URL**: `http://127.0.0.1:5000/api/user`
- **Method**: POST
- **Body** → Raw → JSON:
```json
{
    "name": "Alice"
}
```

---

## Best Practices

Follow these practices from day one:

- ✅ **Always** return JSON for APIs (not HTML strings)
- ✅ Use **descriptive route names** (`/api/users` instead of `/api/u`)
- ✅ Keep `debug=True` only in development, never in production
- ✅ Organize routes logically — later we'll use **Blueprints**
- ✅ Use **environment variables** for secrets (coming in Module 2)

---

## Exercises

Complete these exercises to reinforce your learning:

### Exercise 1: Status Endpoint
Create a `/api/status` route that returns:
```json
{
    "service": "Flask API",
    "status": "running",
    "version": "1.0.0"
}
```

### Exercise 2: Addition Endpoint
Create a `/api/add` route that accepts POST with two numbers and returns their sum.

**Expected Input:**
```json
{
    "num1": 5,
    "num2": 3
}
```

**Expected Output:**
```json
{
    "result": 8,
    "operation": "addition"
}
```

### Exercise 3: Time Endpoint
Create a `/api/time` route that returns current server time in JSON format.

**Hint:** Use Python's `datetime` module.

---

## ✅ Checkpoint

You're ready for **Module 2** if you can:

- [x] Run a Flask app locally
- [x] Create GET & POST routes
- [x] Return JSON responses
- [x] Handle request data (via `request.get_json()`)

---

## What's Next?

**Module 2: Project Structure, Environment Management & App Factory Pattern**

In the next module, we'll cover:
- Professional project structure
- Environment configurations
- Making Flask scalable from the start
- App factory pattern implementation

---

## Resources

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [HTTP Status Codes Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Postman Download](https://www.postman.com/downloads/)

---

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

---

## License

This course material is provided under the MIT License. See LICENSE file for details.