#Flaskとrender_template（HTMLを表示させるための関数）をインポート
#ライブラリを使用する際のお約束
from flask import Flask,render_template, request, url_for
import cancers
import immunizations
import others

#Flaskオブジェクトの生成
#Flaskのクラスをインスタンス化している
app = Flask(__name__)

#デコレーターという機能を使ったルーティングの設定
#ルーティングとは、URLと処理を対応づけること、Flaskのルーティングは、URLとfuncitonを紐付けます。ルーティングには、route() を用います。

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    return render_template('index.html', title='health maintainance')
    # returnにtitleとnameの変数を追加。

@app.route("/")
def toppage():
    return render_template('toppage.html', title='health maintainance')

#POSTの時の処理
#returnの前でも返せない。なぜ？
@app.route("/result", methods=['POST'])
def calculation():
    age = int(request.form["age"])
    gender = request.form["gender"]
    pregnancy = int(request.form["pregnancy"])
    smoking = int(request.form["smoking"])
    number_of_smoking = int(request.form["number_of_smoking"])
    years_of_smoking = int(request.form["years_of_smoking"])
    sexual_activity = int(request.form["sex"])
    alcohol = int(request.form["alcohol"])
    height = int(request.form["height"])
    weight = int(request.form["weight"])

    smoking_hx = number_of_smoking * years_of_smoking
    BMI = weight / (height ** 2 / 10 ** 4)

    result = list()

    #以下Cancers
    if age >= 50 and age < 75:
        result.append(cancers.colon_ca())
    if age > 50:
        result.append(cancers.gastric_ca())
    if age >= 40 and age < 75 and gender == "f":
        result.append(cancers.breast_ca())
    if age >= 21 and age < 65 and gender == "f":
        result.append(cancers.cervical_ca())
    if age >= 55 and age < 80 and smoking_hx >= 30:
        result.append(cancers.lung_ca())
    if age >= 50 and age < 70 and gender == "m":
        result.append(cancers.prostate_ca())

    #以下Others
    if smoking == 1:
        result.append(others.smoking())
    if age >= 50 and gender == "f":
        result.append(others.osteopolosis())
    if age >= 18:
        result.append(others.hypertention())
    if age >= 65:
        result.append(others.falling())
    if age >= 65 and age < 75 and (smoking == 1 or smoking == 3):
        result.append(others.aneurysm())
    if age >= 40 and age < 70 and BMI > 25:
        result.append(others.diabetes())
    if age >= 40 and age < 70:
        result.append(others.hyperlipidemia())
    if age >= 12:
        result.append(others.depression())
    if gender == "f" and sexual_activity == 1:
        result.append(others.STD_1())
    if gender == "f" and sexual_activity == 1:
        result.append(others.STD_2())
    if alcohol == 1:
        result.append(others.alcohol())
    if BMI >= 25:
        result.append(others.obesity())
    if age >= 40 and age < 80:
        result.append(others.hepatitis())
    if age >= 18 and age <= 45 and gender == "f":
        result.append(others.folate())

    #以下Immunitzationns
    if age >= 65:
        result.append(immunizations.pneumococcus())
    if age > 0.5:
        result.append(immunizations.flu())
    if age >= 22:
        result.append(immunizations.tetanus())
    if age >= 12 and age <= 26 and gender == "f":
        result.append(immunizations.HPV())
    if age >= 20:
        result.append(immunizations.HBV())
    if age >= 50:
        result.append(immunizations.Zoster())

    return render_template('result.html',result=result)

#おまじない
if __name__ == '__main__':
    app.run()
