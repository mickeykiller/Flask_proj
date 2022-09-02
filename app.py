from flask import Flask
import request
import render_template

app = Flask(__name__)

@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
                          #  利用request取得表單欄位值
        return 'Hello ' + request.values['username']
    
    #  非POST的時候就會回傳一個空白的模板
    return render_template('login.html')

if __name__ == '__main__':
    #app.debug = True
    app.run() 