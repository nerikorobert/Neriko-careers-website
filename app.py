from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Nairobi',
        'salary': 'Ksh 300,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Kisumu',
        'salary': 'Ksh 400,000',
    },
    {
        'id': 3,
        'title': 'FrontEnd Engineer',
        'location': 'remote',
        
    },
    {
        'id': 1,
        'title': 'Backend Engineer',
        'location': 'USA',
        'salary': '$ 120,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)     


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
