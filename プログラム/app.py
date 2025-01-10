from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# サブ選択肢のデータとカメラのマッピング
sub_requests = {
    "価格帯から選ぶ": {
        "～5万円": {
            "カメラ": "SIGMA 30mm F1.4 DC DN | Contemporary",
            "説明": "APS-Cフォーマット対応の標準単焦点レンズで、開放F値1.4の明るさとコンパクトなデザインが特徴です。",
            "写真": "static/images/~5.jfif"
        },
        "5万円～10万円": {
            "カメラ": "SIGMA 28-70mm F2.8 DG DN | Contemporary",
            "説明": "フルサイズミラーレスカメラ向けの標準ズームレンズで、F2.8通しの明るさとコンパクトなサイズが魅力です。",
            "写真": "static/images/5~10.webp"
        }, 
        "10万円～15万円": {
            "カメラ": "SIGMA 105mm F2.8 DG DN MACRO | Art",
            "説明": "フルサイズミラーレスカメラ向けのマクロレンズで、Artシリーズならではの高い光学性能と美しいボケ味が特徴です。",
            "写真": "static/images/10~15jfif"
        },
        "15万円～": {
            "カメラ":"SIGMA 35mm F1.4 DG DN | Art",
            "説明": "フルサイズミラーレスカメラ向けの高性能単焦点レンズで、開放F1.4の明るさとArtシリーズならではの高い解像力が魅力です。",
            "写真": "static/images/15~.jfif"
        }
    },
    "撮りたい写真から選ぶ": {
        "遠くのものを撮りたい":{
            "カメラ": "SIGMA 500mm F5.6 DG DN OS | Sports", 
            "説明": "焦点距離500mmの超望遠レンズで、野鳥やスポーツなど遠距離の被写体撮影に最適です。",
            "写真":"static/images/遠く.png"
         },
        "風景を撮りたい": {
            "カメラ": "SIGMA 16-28mm F2.8 DG DN | Contemporary", 
            "説明": "広角ズームレンズで、風景や建築物の撮影に適しています。",
            "写真":"static/images/風景.jpeg"
        },
        "近くのものを撮りたい":{
             "カメラ": "SIGMA 105mm F2.8 DG DN MACRO | Art",
             "説明": "マクロレンズで、花や小物などのクローズアップ撮影に最適です。",
             "写真":"static/images/近く.webp"
        }, 
        "動くものを撮りたい": {
            "カメラ": "SIGMA 70-200mm F2.8 DG OS HSM | Sports",
            "説明": "高速なオートフォーカスと手ブレ補正機能を備え、スポーツや動物などの動体撮影に適しています。",
            "写真":"static/images/動く.jfif"
        }
    }
}

# メインページを表示
@app.route("/")
def index():
    return render_template("index.html")

# サブ選択肢を返すAPI
@app.route("/get_sub_requests", methods=["POST"])
def get_sub_requests():
    main_request = request.json.get("mainRequest")
    options = sub_requests.get(main_request, {})
    return jsonify(options)

# カメラを提案するAPI
@app.route("/get_camera_recommendation", methods=["POST"])
def get_camera_recommendation():
    main_request = request.json.get("mainRequest")
    sub_request = request.json.get("subRequest")
    
    camera_info = sub_requests.get(main_request, {}).get(sub_request, {})
    camera = camera_info.get("カメラ", "カメラが見つかりません")
    feature = camera_info.get("説明", "説明がありません")
    photo = camera_info.get("写真", "")

    
    return jsonify({"camera": camera, "feature": feature, "photo": photo})

if __name__ == "__main__":
    app.run(debug=True)
