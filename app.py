from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# db conncetion 
client = MongoClient("mongodb://localhost:27017/")
db = client['fitness_app']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Hashing the password
        hashed_password = generate_password_hash(request.form.get('password'))

        user_info = {
            "username": request.form.get('username'),
            "password": hashed_password,
            "gender": request.form.get('gender'),
            "dob": request.form.get('dob'),
            "height": request.form.get('height'),
            "current_weight": request.form.get('current_weight')
        }
        db.users.insert_one(user_info)
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # finding user by user name 
        user = db.users.find_one({"username": username})

        if user and check_password_hash(user['password'], password):
            # auth successf
            return redirect(url_for('index'))  # Redirect to a different page after login
        else:
            # Authentication failed
            return "Invalid credentials", 401

    return render_template('signin.html')

@app.route('/nutrition-diary', methods=['GET', 'POST'])
def nutrition_diary():
    if request.method == 'POST':
        # Extract data from the form
        entry = {
            "food_item": request.form.get("food-item"),
            "calories": request.form.get("calories"),
            "date": request.form.get("date")
        }
        # data insertion 
        db.nutrition.insert_one(entry)

    # historical data from MongoDB
    entries = db.nutrition.find().sort("date", -1)  # Sort by date descending
    return render_template('nutrition-diary.html', entries=entries)


if __name__ == '__main__':
    app.run(debug=True)
