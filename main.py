# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for, session
import os

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)
app.secret_key = os.urandom(64)


# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    app.secret_key = os.urandom(64)
    return redirect('/home')

@app.route('/home')
def home():
    title = "Flask Sample"

    return render_template('index.html', title=title)




if __name__ == '__main__':
    app.debug = True  # デバッグモード有効化
    app.run(host='0.0.0.0', port=4800)  # どこからでもアクセス可能に