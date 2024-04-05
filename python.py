from flask import Flask,render_template, request #přidal jsem si i třídu request, ať můžu requestovat!

app = Flask(__name__)

@app.route("/", methods = ["get"])#něco s tím odkazem + povoluju metodu get! (už ji mám v html, tak ať s ní můžu pracovat i tady)
def prvnifunkce():
    jidlo = request.args.get("input1")
    print(jidlo)
    kolik_jidlo = request.args.get("input2")
    print(kolik_jidlo)
    piti = request.args.get("input3")
    print(piti)
    kolik_piti = request.args.get("input4")
    print(kolik_piti)
    
    vysledek ="Objednali jste si : ", jidlo, kolik_jidlo,"-krát,", piti, kolik_piti,"-krát,"
    return render_template("stranka.html",vysledek = vysledek)

if __name__ == "__main__":
    app.run(debug=True)



