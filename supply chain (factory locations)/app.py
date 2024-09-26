from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials for demonstration
USER_CREDENTIALS = {
    'username': 'admin',
    'password': 'admin123'
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/input_form', methods=['POST'])
def input_form():
    username = request.form['username']
    password = request.form['password']
    
    # Debugging statements
    print(f"Received Username: {username}")
    print(f"Received Password: {password}")
    
    if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
        print("Login successful")
        return redirect(url_for('index'))
    else:
        print("Invalid credentials")
        return "Invalid credentials. Please try again."

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
