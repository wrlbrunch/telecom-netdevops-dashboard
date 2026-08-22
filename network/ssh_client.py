import ipaddress
from netmiko import ConnectHandler
from network.commands import obter_comandos

FABRICANTES_PERMITIDOS = ["cisco_ios", "mikrotik_routeros", "huawei_vrp"]

def validar_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def executar_configuracao(fabricante: str, ip: str, usuario: str, senha: str, interface: str, descricao: str) -> tuple[bool, str]:
    """
    Executa a configuração no dispositivo de rede.
    Retorna uma tupla (sucesso: bool, mensagem: str).
    """
    if not validar_ip(ip):
        return False, f"IP inválido: {ip}"

    if fabricante not in FABRICANTES_PERMITIDOS:
        return False, "Fabricante não suportado."

    comandos = obter_comandos(fabricante, interface, descricao)

    dispositivo = {
        "device_type": fabricante,
        "host": ip,
        "username": usuario,
        "password": senha,
        "port": 2222,
        "conn_timeout": 10,
    }

    net_connect = None
    try:
        net_connect = ConnectHandler(**dispositivo)

        if fabricante == "mikrotik_routeros":
            output = net_connect.send_command(comandos[0])
        else:
            output = net_connect.send_config_set(comandos)

        mensagem = (
            f"Configuração realizada com sucesso!\n\n"
            f"Equipamento: {ip}\n"
            f"Interface: {interface}\n"
            f"Descrição: {descricao}\n\n"
            f"Saída do equipamento:\n{output}"
        )
        return True, mensagem

    except Exception as e:
        mensagem = f"Falha ao configurar o equipamento.\n\nIP: {ip}\nErro: {str(e)}"
        return False, mensagem

    finally:
        if net_connect:
            net_connect.disconnect()