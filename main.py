def analisar_logs(nomes_arquivos):
    logs = []
    for nome_arquivo in nomes_arquivos:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            partes = linha.split('\t')
            date = partes[0]
            time = partes[1]
            http_method = partes[2]
            uri = partes[3]
            status = partes[4]
            time_taken = partes[5]
            ip_referrer = partes[6]
            content_type = partes[7]
            mensagem = partes[8]
            transacao = partes[9]
            usuario_sistema = partes[10]
            logs.append((date, time, http_method, uri, status, time_taken, ip_referrer, content_type, mensagem, transacao, usuario_sistema))
    return logs


def relatorio_diario_acessos(logs):
    relatorio = {}
    for log in logs:
        data_acesso = log[0]
        if data_acesso in relatorio:
            relatorio[data_acesso] += 1
        else:
            relatorio[data_acesso] = 1
    return relatorio

def tempo_medio_resposta(logs):
    total_tempo = 0
    total_logs = 0
    for log in logs:
        tempo_resposta = float(log[5])
        total_tempo += tempo_resposta
        total_logs += 1
    return total_tempo / total_logs

def usuarios_mais_ativos(logs):
    usuarios = {}
    for log in logs:
        usuario = log[6]
        if usuario in usuarios:
            usuarios[usuario] += 1
        else:
            usuarios[usuario] = 1
    return usuarios

def paginas_mais_acessadas(logs):
    paginas = {}
    for log in logs:
        pagina = log[3]
        if pagina in paginas:
            paginas[pagina] += 1
        else:
            paginas[pagina] = 1
    return paginas

 
def menu_principal(logs):
    menu = True
    while menu:
        print("====== MENU ======")
        print("1. Relatório Diário de Acessos")
        print("2. Tempo Médio de Resposta")
        print("3. Usuários Mais Ativos")
        print("4. Páginas Mais Acessadas")
        print("5. Sair")
        op = int(input("Selecione uma opção: "))
        if op == 1:
            relatorio = relatorio_diario_acessos(logs)
            for data, acessos in relatorio.items():
                print(f'Data: {data}, Acessos: {acessos}')
        elif op == 2:
            tempo_medio = tempo_medio_resposta(logs)
            print(f'Tempo Médio de Resposta: {tempo_medio}')
        elif op == 3:
            usuarios = usuarios_mais_ativos(logs)
            for usuario, acessos in usuarios.items():
                print(f'Usuário: {usuario}, Acessos: {acessos}')
        elif op == 4:
            paginas = paginas_mais_acessadas(logs)
            for pagina, acessos in paginas.items():
                print(f'Página: {pagina}, Acessos: {acessos}')
        elif op == 5:
            print("Você selecionou Sair")
            print("/n FIM DO PROGRAMA")
            menu = False
            break
        else:
            print("Opção Inválida")
            print("FIM DO PROGRAMA")
            menu = False

logs = analisar_logs(['server1__2024-05-01.txt', 'server1__2024-04-29.txt', 'server1__2024-04-30.txt'])

menu_principal(logs)
