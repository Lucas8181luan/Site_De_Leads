from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    template = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IFP Brasil</title>
    </head>
    <style>
        div[id="inputs"] {
            text-align: center;
        }
        input[id="nome"] {
            height: 50px;
            width: 500px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
        input[id="E-mail"] {
            height: 50px;
            width: 500px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
            input[id="confrimação E-mail"] {
            height: 50px;
            width: 500px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
            input[id="telefone"] {
            height: 50px;
            width: 500px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
    </style>
    <body>
        <h1>IFP Brasil</h1>
        <div id="inputs">
            <input type="text" id="nome" placeholder="NOME COMPLETO">
            <br><p>
            <input type="text" id="E-mail" placeholder="E-MAIL">
            <br><p>
            <input type="text" id="confrimação E-mail" placeholder="CONFIRMAÇÃO E-MAIL">
            <br><p>
            <input type="number" id="telefone" placeholder="TELEFONE (xx)xxxxx-xxxx">
        </div>
    </body>
    </html>
    '''
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
