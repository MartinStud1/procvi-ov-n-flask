from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def prvnifunkce():
    a = "nazdar"
    return render_template("stranka.html")

if __name__ == "__main__":
    app.run()



