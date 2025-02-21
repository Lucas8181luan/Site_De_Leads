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
        input[id="data de nascimento"] {
            height: 50px;
            width: 500px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
        select[id="curso escolhido"] {
            height: 50px;
            width: 525px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
        select[id="horário de estudo"] {
            height: 50px;
            width: 525px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
        input[id="cep"] {
            height: 50px;
            width: 500px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
        select[id="bairro"] {
            height: 50px;
            width: 525px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
        input[id="cpf"] {
            height: 50px;
            width: 500px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
        select[id="sexo"] {
            height: 50px;
            width: 525px;
            font-size: 15px;
            border-radius: 10px;
            padding-left: 20px;
        }
        button[id="enviar"] {
            height: 50px;
            width: 200px;
            font-size: 25px;
            border-radius: 10px;
            background-color: blue;
            color: white;
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
            <input type="number" id="telefone" placeholder="TELEFONE (DDD)xxxxx-xxxx">
            <br><p>
            <input type="date" id="data de nascimento" placeholder="DATA DE NASCIMENTO (+18)">
            <br><p>
            <select id="curso escolhido">
                <option value=".">ESCOLHA SEU CURSO</option>
                <option value="EAD - AGENTE DE DEFESA AMBIENTAL">EAD - AGENTE DE DEFESA AMBIENTAL</option>
                <option value="HÍBRIDO - ATENDENTE DE FARMÁCIA">HÍBRIDO - ATENDENTE DE FARMÁCIA</option> 
                <option value="HÍBRIDO - AUXILIAR ADMINISTRATIVO">HÍBRIDO - AUXILIAR ADMINISTRATIVO</option> 
                <option value="HÍBRIDO - OPERADOR DE CAIXA">HÍBRIDO - OPERADOR DE CAIXA</option> 
                <option value="HÍBRIDO - DESIGNER DE SOMBRANCELHAS">HÍBRIDO - DESIGNER DE SOMBRANCELHAS</option> 
                <option value="HÍBRIDO - CUMIN">HÍBRIDO - CUMIN</option>
                <option value="HÍBRIDO - GARÇOM">HÍBRIDO - GARÇOM</option> 
                <option value="PRESENCIAL - INFORMÁTICA">PRESENCIAL - INFORMÁTICA</option> 
                <option value="PRESENCIAL - CUIDADOR DE IDOSO">PRESENCIAL - CUIDADOR DE IDOSO</option> 
            </select>
            <br><p>
            <select id="horário de estudo">
                <option value=".">ESCOLHA SEU HORÁRIO DE ESTUDO</option>
                <option value="MANHÃ">MANHÃ</option>
                <option value="TARDE">TARDE</option>]
                <option value="NOITE">NOITE</option>
            </select>
            <br><p>
            <input type="number" id="cep" placeholder="CEP">
            <br><p>
            <select id="bairro">
                <option value=".">LOCAL DE ESTUDO</option>
                <option value="PENHA - CASA NAILS BRASIL">PENHA - CASA NAILS BRASIL</option>
                <option value="MADUREIRA - IFP">MADUREIRA - IFP</option>]
                <option value="CENTRO - EMPREENDA.RIO">CENTRO - EMPREENDA.RIO</option>
            </select>
            <br><p>
            <input type="number" id="cpf" placeholder="CPF">
            <br><p>
            <select id="sexo">
                <option value=".">SEXO</option>
                <option value="M">MASCULINO</option>
                <option value="F">FEMININO</option>]
            </select>
            <br><br><p>
            <button type"submit" id="enviar"><strong>ENVIAR</strong></button>
        </div>
    </body>
    </html>
    '''
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
