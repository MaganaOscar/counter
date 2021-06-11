from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = b"\x9e\xe9!\xa8\xd1\x8en\xf8'\xf2\xa2\x8d\xa9O\xb6\x16"

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/inc_by_2')
def inc_by_2():
    session['count'] += 1
    return redirect('/')

# @app.route('/inc_by_x/', methods=['GET'])
# def inc_by_x():
#     print(request.form)
#     session['count'] += request.form['test'] - 1
#     return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)