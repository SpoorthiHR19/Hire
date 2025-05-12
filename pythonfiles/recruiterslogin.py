from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
@app.route('/recruiter_login', methods=['POST'])
def recruiter_login():
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')

    return check_recruiter_login(username, password)

@app.route('/recruiter_login')
def recruiter_login_page():
    return render_template('recruiter_login.html')

def check_recruiter_login(username, password):
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM recruiters WHERE username = ? AND password = ?', (username, password))
    recruiter = cursor.fetchone()

    conn.close()

    if recruiter:
        return jsonify({'redirected': True, 'url': '/recruiter_home'})
    else:
        return jsonify({'redirected': False})
 