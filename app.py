import sys, subprocess
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "secure_vision_2026"

# Basic User Management
users = {"test@user.com": "1234"}

@app.route('/')
def index():
    return render_template('auth.html')

@app.route('/auth', methods=['POST'])
def auth():
    email = request.form.get('email')
    password = request.form.get('password')
    users[email] = password # Simple registration/login logic
    session['user'] = email
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('index'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/launch_ai', methods=['POST'])
def launch_ai():
    try:
        # Runs vision_engine.py as a separate window
        subprocess.Popen([sys.executable, "vision_engine.py"])
        return jsonify({"status": "Vision Engine Started Successfully"})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)