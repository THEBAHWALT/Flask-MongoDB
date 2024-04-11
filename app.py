from flask import Flask
app = Flask(__name__)

# 建立路徑 / 對應的處理函式
@app.route("/")
def index(): # 用來回應路徑 / 處理函式
    return "Test" # 回傳網站首頁的內容
# 建立路徑 /data 對應的處理函式
@app.route("/data")
def handleData():
    return "My Data"

# 動態路徑 : 建立路徑 /user/使用者名稱 對應的處理函式
@app.route("/user/<username>")
def handleUser(username):
    if username == "Walter":
        return "Hi, Walter"
    else:
        return "You're not Walter. "+username

# 啟動網站伺服器，可透過port參數指定阜號
app.run(port=82)

