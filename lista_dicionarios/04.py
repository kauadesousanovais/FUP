def compare_date(date1: dict, date2: dict) -> bool:
    if date1["ano"] < date2["ano"]:
        return True
    elif date1["ano"] == date2["ano"]:
        if date1["mes"] < date2["mes"]:
            return True
        elif date1["mes"] == date2["mes"]:
            if date1["dia"] < date2["dia"]:
                return True
    return False


def compare_time(time1: dict, time2: dict) -> bool:
    if time1["hora"] < time2["hora"]:
        return True
    elif time1["hora"] == time2["hora"]:
        if time1["minuto"] < time2["minuto"]:
            return True
        elif time1["minuto"] == time2["minuto"]:
            if time1["segundo"] < time2["segundo"]:
                return True
    return False


def compare_events(event1: dict, event2: dict) -> bool:
    if compare_date(event1["data"], event2["data"]):
        return True
    elif event1["data"] == event2["data"]:
        if compare_time(event1["horario"], event2["horario"]):
            return True
    return False


def bubble_sort(events: list):
    n = len(events)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if not compare_events(events[j], events[j + 1]):
                events[j], events[j + 1] = events[j + 1], events[j]  


quant = int(input())
dicionarios = []

for _ in range(quant):
    dia = int(input())
    mes = int(input())
    ano = int(input())

    hora = int(input())
    minuto = int(input())
    segundo = int(input())

    descricao = input()

    data = {"dia": dia, "mes": mes, "ano": ano}
    horario = {"hora": hora, "minuto": minuto, "segundo": segundo}

    compromisso = {"data": data, "horario": horario, "descricao": descricao}
    dicionarios.append(compromisso)

bubble_sort(dicionarios)

print(quant)
for evento in dicionarios:
    print(f"Dia: {evento['data']['dia']}")
    print(f"Mes: {evento['data']['mes']}")
    print(f"Ano: {evento['data']['ano']}")
    print(f"Hora: {evento['horario']['hora']:02}")
    print(f"Minuto: {evento['horario']['minuto']:02}")
    print(f"Segundo: {evento['horario']['segundo']:02}")
    print(f"Descricao: {evento['descricao']}")