from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    shipments = [
        {
            "job": "JOB001",
            "tank": "NPTU1234567",
            "customer": "Lubrizol",
            "origin": "Nhava Sheva",
            "destination": "Port Klang",
            "status": "Booked"
        },
        {
            "job": "JOB002",
            "tank": "NPTU7654321",
            "customer": "Firmenich",
            "origin": "Mundra",
            "destination": "Port Klang",
            "status": "In Transit"
        },
        {
            "job": "JOB003",
            "tank": "NPTU9876543",
            "customer": "Customer A",
            "origin": "Ludhiana",
            "destination": "Mundra",
            "status": "Repo"
        }
    ]

    return render_template("index.html", shipments=shipments)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
