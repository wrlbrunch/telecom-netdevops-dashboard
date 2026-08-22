from flask import Flask, render_template, request
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/configurar', methods=['POST'])
def configurar():
    fabricante = request.form['fabricante']
    ip_roteador = request.form['ip']
    usuario = request.form['usuario']
    senha = request.form['senha']
    interface = request.form['interface']
    descricao = request.form['descricao']

    dispositivo = {
        'device_type': fabricante,  
        'host': ip_roteador,
        'username': usuario,        
        'password': senha,
        
        'port': 22,
    }

    if fabricante == 'mikrotik_routeros':
        comandos = [
            f'/interface set [find name={interface}] comment="{descricao} - Configurado via Python Web"'
        ]
    elif fabricante == 'huawei_vrp':
        comandos = [
            f'interface {interface}',
            f'description {descricao} - Configurado via Python Web',
            'undo shutdown'
        ]
    else:  
        comandos = [
            f'interface {interface}',
            f'description {descricao} - Configurado via Python Web',
            'no shutdown'
        ]

    try:
        net_connect = ConnectHandler(**dispositivo)
        output = net_connect.send_config_set(comandos)
        net_connect.disconnect()
        
        mensagem = f"Sucesso!\n{output}"

    except NetmikoTimeoutException:
        mensagem = f"Erro de Conexão: O roteador {ip_roteador} está inacessível ou fora do ar."
    except NetmikoAuthenticationException:
        mensagem = f"Erro de Autenticação: Usuário ou senha incorretos para {ip_roteador}."
    except Exception as e:
        mensagem = f"Erro inesperado no roteador {ip_roteador}: {str(e)}"

    return render_template('index.html', resultado=mensagem)

if __name__ == '__main__':
    app.run(debug=True)