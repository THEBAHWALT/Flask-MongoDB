from flask import Flask
import json
from flask import redirect
app = Flask(
    __name__
)
# response 字串
@app.route("/string")   #response 字串
def res_string():
    return "Hello Flask~"
@app.route("/google")   #導向到google
def res_google():
    return redirect("https://www.google.com")
@app.route("/")
# json 字串
def index():
    return json.dumps({
        "mood" : "開心",
        "speed" : "好想過年"
    }, ensure_ascii=False)
app.run(port = 82) # 啟動伺服器