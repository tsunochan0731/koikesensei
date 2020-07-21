#Flaskとrender_template（HTMLを表示させるための関数）をインポート
#ライブラリを使用する際のお約束
from flask import Flask,render_template, request
import cancers

#Flaskオブジェクトの生成
#Flaskのクラスをインスタンス化している
app = Flask(__name__)

#デコレーターという機能を使ったルーティングの設定
#ルーティングとは、URLと処理を対応づけること、Flaskのルーティングは、URLとfuncitonを紐付けます。ルーティングには、route() を用います。
#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    return render_template('index.html', title='health maintainance')
    # returnにtitleとnameの変数を追加。

#POSTの時の処理
#returnの前でも返せない。なぜ？
@app.route("/result", methods=['POST'])
cancers.colon_ca()
return "関数以外は大丈夫です"

#おまじない
if __name__ == "__main__":
    app.run()
