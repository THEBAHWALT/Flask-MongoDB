from flask import Flask
from flask import render_template
app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
# 建立路徑 / 對應的處理函式
@app.route("/")
def index():
    return render_template("index", name = "Walter")

# 啟動伺服器
app.run(port = 82)