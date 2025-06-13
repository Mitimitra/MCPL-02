from flask import Flask, render_template, request, redirect, session, url_for, flash
import psycopg2
import os

app = Flask(__name__)
#app.secret_key = os.environ.get('SECRET_KEY', 'supersecretkey')
app.secret_key = os.environ.get('SECRET_KEY', 'Mitimitra@7')

DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db_connection():
    return psycopg2.connect(database = "MCPL01", user = "postgres", password = "Mitimitra@7", host = "localhost", port = "5432")

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT "UserId", "EmpName", "OrgId" FROM "UserMaster" 
            WHERE "UserName" = %s AND "UserPwd" = %s AND "IsActive" = TRUE
        """, (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['emp_name'] = user[1]
            session['org_id'] = user[2]
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html', emp_name=session['emp_name'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 5002)))