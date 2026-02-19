from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html', generated=False)

@app.route('/generate', methods=['POST'])
def generate():
    # Get form data and store in session
    cv_data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'about': request.form.get('about'),
        'degree': request.form.get('degree'),
        'institution': request.form.get('institution'),
        'year': request.form.get('year'),
        'skills': request.form.get('skills')
    }
    
    # Store in session
    session['cv_data'] = cv_data
    
    # Redirect back to home with success message
    return render_template('index.html', generated=True)

@app.route('/view-cv')
def view_cv():
    # Retrieve CV data from session
    cv_data = session.get('cv_data', {})
    if not cv_data:
        return redirect(url_for('index'))
    return render_template('view_cv.html', cv=cv_data)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)