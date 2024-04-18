import os
print("Current working directory:", os.getcwd())
from flask import Flask
from flask import render_template
app = Flask(__name__,
            template_folder='D:/Python/Flask/templates', 
            static_folder="public", 
            static_url_path="/")

# 建立路徑 / 對應的處理函式
@app.route("/")
def index():
    return render_template("index.html")
# 處理路徑 / 的對應函式
@app.route("/page")
def page():
    return render_template("page.html")

# 啟動伺服器
app.run(port = 82)