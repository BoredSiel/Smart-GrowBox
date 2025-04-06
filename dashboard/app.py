# app.py
# Flask-based dashboard for real-time sensor data

from flask import Flask, render_template_string
import random  # Replace with real sensor imports

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = {
        "Temperature": round(20 + random.random() * 5, 2),
        "Humidity": round(40 + random.random() * 10, 2),
        "Soil Moisture": round(300 + random.random() * 100, 2),
        "Light": round(200 + random.random() * 400, 2),
        "pH": round(6.0 + random.random(), 2)
    }

    html = """
    <h1>GrowBox Dashboard</h1>
    <ul>
    {% for k, v in data.items() %}
      <li><b>{{ k }}:</b> {{ v }}</li>
    {% endfor %}
    </ul>
    """

    return render_template_string(html, data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
