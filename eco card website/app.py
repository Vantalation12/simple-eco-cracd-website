from flask import Flask, render_template
app = Flask(__name__)
#Anasayfa
@app.route(("/"))
def index():
    title="Hoşgeldiniz!"
    description = "Bu benim ilk websitem!!"
    return render_template("index.html", title=title, description=description)
@app.route("/eco_card")
def eco_card():
    card_data = {
        "title": "Işıklar açık unutulduğunda bildirim gönderen uygulama",
        "description": "Denemelisiniz!",
        "image_url": "https://github.com/Vantalation12/test/blob/cba4da553ceb7bd8ef61351686914ae5b5858b51/leaf.png",
        "value":"85/100" 
    }
    return render_template("eco_card.html",
    card=card_data)
if __name__== "__main__":
    app.run(debug=True)