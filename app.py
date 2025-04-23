# app.py
from flask import Flask, render_template
from monitor import get_system_stats

app = Flask(__name__)

@app.route("/")
def dashboard():
    stats = get_system_stats()
    return render_template("dashboard.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
app.run(debug=True, port=5050)
@app.route('/api/stats')
def api_stats():
    stats = get_system_stats()  # reuse your existing function
    return jsonify(stats)
from flask import jsonify
