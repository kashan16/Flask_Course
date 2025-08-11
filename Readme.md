# Flask Backend Mastery Course

## Table of Contents
- [Module 1: Introduction to Flask + First API](#module-1-introduction-to-flask--first-api)
- [Module 2: Project Structure, Environment Management & App Factory Pattern](#module-2-project-structure-environment-management--app-factory-pattern)

---

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

- ✅ Run a Flask app locally
- ✅ Create GET & POST routes
- ✅ Return JSON responses
- ✅ Handle request data (via `request.get_json()`)

---

# Module 2: Project Structure, Environment Management & App Factory Pattern

## 🎯 Learning Objectives

By the end of this module, you will:

1. Understand why the "one `app.py` file" approach is bad for real apps
2. Create a **modular Flask project** that can grow to dozens of routes
3. Use **environment variables** for sensitive data and config
4. Implement the **App Factory Pattern** to separate setup from runtime
5. Add **request data validation** using `marshmallow` (or `pydantic`)
6. Prepare your project for testing and deployment

---

## Table of Contents - Module 2

1. [Why Project Structure Matters](#why-project-structure-matters)
2. [Recommended Project Structure](#recommended-project-structure)
3. [Environment Management](#environment-management)
4. [App Factory Pattern](#app-factory-pattern)
5. [Using Blueprints for Routes](#using-blueprints-for-routes)
6. [Entry Point](#entry-point)
7. [Request Data Validation](#request-data-validation)
8. [Best Practices](#best-practices-module-2)
9. [Exercises - Module 2](#exercises-module-2)
10. [Checkpoint - Module 2](#checkpoint-module-2)

---

## Why Project Structure Matters

The "single file" Flask app is fine for learning, but:

- It mixes routes, config, and database code in one place → hard to maintain
- Harder to test & debug
- Doesn't scale for large APIs with many endpoints

### Industry Rule:
➡ **Organize by responsibility, not by type.**

---

## Recommended Project Structure

We'll start with a **minimal professional setup**.

```
flask_course/
│
├── app/
│   ├── __init__.py        # App factory
│   ├── config.py          # Config classes
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── user_routes.py
│   │   └── status_routes.py
│   ├── models/            # DB models (later)
│   ├── services/          # Business logic (later)
│   └── validators/        # Marshmallow schemas
│
├── .env                   # Environment variables
├── run.py                 # Entry point
├── requirements.txt
└── README.md
```

---

## Environment Management

We'll use `python-dotenv` to load `.env` files.

### Install Dependencies
```bash
pip install python-dotenv
```

### Create .env File
**Important:** Don't commit this to GitHub!

```env
FLASK_ENV=development
SECRET_KEY=supersecretkey123
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
```

### Create Configuration Classes

**app/config.py**:
```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
    DATABASE_URL = os.getenv("DATABASE_URL")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
```

---

## App Factory Pattern

Instead of creating the Flask app directly in `app.py`, we create a **function** that returns an app — allowing for different configs in dev/prod/test.

**app/__init__.py**:
```python
from flask import Flask
from .config import DevelopmentConfig
from .routes.user_routes import user_bp
from .routes.status_routes import status_bp

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints (modular routes)
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(status_bp, url_prefix="/api/status")

    return app
```

---

## Using Blueprints for Routes

Instead of dumping routes in one file, we'll make **blueprints** for each domain.

### User Routes
**app/routes/user_routes.py**:
```python
from flask import Blueprint, request, jsonify

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET"])
def list_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify({"message": f"User {data['name']} created"}), 201
```

### Status Routes
**app/routes/status_routes.py**:
```python
from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__)

@status_bp.route("/", methods=["GET"])
def service_status():
    return jsonify({
        "service": "Flask API",
        "status": "running",
        "version": "2.0.0"
    })
```

---

## Entry Point

**run.py**:
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
```

### Run the Application
```bash
python run.py
```

---

## Request Data Validation

We'll use **marshmallow** for clean, declarative validation.

### Install Marshmallow
```bash
pip install marshmallow
```

### Create Validation Schema
**app/validators/user_validator.py**:
```python
from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2))
    email = fields.Email(required=True)
```

### Update User Routes with Validation
**app/routes/user_routes.py**:
```python
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.validators.user_validator import UserSchema

user_bp = Blueprint("user", __name__)
user_schema = UserSchema()

@user_bp.route("/", methods=["POST"])
def create_user():
    json_data = request.get_json()
    try:
        validated_data = user_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    return jsonify({
        "message": "User created successfully",
        "user": validated_data
    }), 201
```

### Testing Validation

**Invalid data example:**
```json
{
    "name": "A",
    "email": "invalid-email"
}
```

**Response:**
```json
{
    "errors": {
        "name": ["Length must be at least 2."],
        "email": ["Not a valid email address."]
    }
}
```

---

## Best Practices - Module 2

Follow these practices for professional Flask development:

- ✅ Use `.env` for **all secrets** — never commit them
- ✅ Keep routes **modular** using blueprints
- ✅ Always validate **incoming data** — don't trust clients
- ✅ Use App Factory for **flexible configs**
- ✅ Write configs as **classes**, not inline in `__init__.py`

---

## Exercises - Module 2

Complete these exercises to master modular Flask development:

### Exercise 1: Products Blueprint
Create a `/api/products` blueprint with GET and POST routes.

### Exercise 2: Product Validation
Validate POST data for products:
- `name` (minimum 3 characters)
- `price` (float > 0)

### Exercise 3: Production Environment
1. Create a `.env.production` file with different settings
2. Run Flask using production configuration

### Exercise 4: Debug Route
Add a `/api/debug` route that returns current app configuration in JSON (for development only).

**Hint:** Use `app.config` to access configuration values.

---

## ✅ Checkpoint - Module 2

You're ready for **Module 3** if you can:

- [x] Create a project using **App Factory Pattern**
- [x] Use **blueprints** for modular routing
- [x] Store config in `.env` files
- [x] Validate request data using marshmallow
- [x] Structure your project professionally

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