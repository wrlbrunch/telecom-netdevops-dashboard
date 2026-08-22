def obter_comandos(fabricante: str, interface: str, descricao: str) -> list[str]:
    """Retorna os comandos corretos com base no fabricante selecionado."""
    
    if fabricante == "cisco_ios":
        return [
            f"interface {interface}",
            f"description {descricao}",
            "no shutdown",
        ]
    elif fabricante == "huawei_vrp":
        return [
            f"interface {interface}",
            f"description {descricao}",
            "undo shutdown",
        ]
    elif fabricante == "mikrotik_routeros":
        return [
            f'/interface ethernet set [find name="{interface}"] comment="{descricao}"'
        ]
    
    raise ValueError("Fabricante não suportado.")