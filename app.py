from flask import Flask
from flask import request 
# 建立 Application 物件，設定靜態檔案路徑處理
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案資料夾名稱
    # static_url_path = "/abc" # 127.0.0.1:82/abc/test.txt
    static_url_path="/" # 對應路徑 # 127.0.0.1:82/abc/test.txt
)
# 所有在 static 資料夾底下的檔案，都c對應到網址路徑 / 名稱

# 建立路徑 / 對應的處理函式
@app.route("/")
def index(): # 用來回應路徑 / 處理函式
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址",request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    # print("語言偏好", request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Flask"
    else:
        return "你好 Flask"
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

