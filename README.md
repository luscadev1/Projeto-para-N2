# Analisador de Logs

Este projeto é um analisador de logs que fornece várias funcionalidades para entender melhor os dados de log.

## Funções

O código contém as seguintes funções:

1. `analisar_logs(nomes_arquivos)`: Esta função recebe uma lista de nomes de arquivos de log e retorna uma lista de logs. Cada log é uma tupla contendo data, hora, método HTTP, URI, status, tempo de resposta, IP de referência, tipo de conteúdo, mensagem, transação e usuário do sistema.

2. `relatorio_diario_acessos(logs)`: Esta função recebe a lista de logs e retorna um relatório dos acessos diários.

3. `tempo_medio_resposta(logs)`: Esta função recebe a lista de logs e retorna o tempo médio de resposta.

4. `usuarios_mais_ativos(logs)`: Esta função recebe a lista de logs e retorna um dicionário dos usuários mais ativos.

5. `paginas_mais_acessadas(logs)`: Esta função recebe a lista de logs e retorna um dicionário das páginas mais acessadas.

6. `menu_principal(logs)`: Esta função recebe a lista de logs e apresenta um menu para o usuário escolher qual relatório deseja ver.

## Como usar

Primeiro, você precisa ter uma lista de arquivos de log para analisar. Em seguida, você pode chamar a função `analisar_logs` para obter a lista de logs. Finalmente, você pode chamar a função `menu_principal` para ver os relatórios.

```python
logs = analisar_logs(['server1__2024-05-01.txt', 'server1__2024-04-29.txt', 'server1__2024-04-30.txt'])
menu_principal(logs)
