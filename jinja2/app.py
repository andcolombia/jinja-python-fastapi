from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static", static_folder='static')

@app.route("/")
def home():
    return render_template("index.html", title = "Oidc Client")

@app.route("/index.html")
def index():
    return render_template("index.html", title = "Oidc Client")

@app.route("/callback.html")
def callback():
    return render_template("callback.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)