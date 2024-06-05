# Analisador de Logs

Este projeto é um analisador de logs que fornece várias funcionalidades para entender melhor os dados de log.

## Descrição

O código é organizado em uma classe chamada `LogAnalyzer`. As funções foram convertidas em métodos desta classe. Além disso, a função `analisar_logs` foi renomeada para `_analyze_logs` e é chamada no construtor da classe. Isso permite que os logs sejam analisados assim que uma instância da classe é criada. As funções que manipulam os logs agora são métodos que operam nos logs armazenados na instância da classe. Isso torna o código mais organizado e fácil de entender.

## Funções

O código contém as seguintes funções:

1. `_analyze_logs(file_names)`: Esta função privada recebe uma lista de nomes de arquivos de log e retorna uma lista de logs. Cada log é uma tupla contendo data, hora, método HTTP, URI, status, tempo de resposta, IP de referência, tipo de conteúdo, mensagem, transação e usuário do sistema.

2. `daily_access_report()`: Esta função retorna um relatório dos acessos diários.

3. `average_response_time()`: Esta função retorna o tempo médio de resposta.

4. `most_active_users()`: Esta função retorna um dicionário dos usuários mais ativos.

5. `most_accessed_pages()`: Esta função retorna um dicionário das páginas mais acessadas.

6. `main_menu()`: Esta função apresenta um menu para o usuário escolher qual relatório deseja ver.

## Como usar

Primeiro, você precisa ter uma lista de arquivos de log para analisar. Em seguida, você pode criar uma instância da classe `LogAnalyzer` e chamar o método `main_menu` para ver os relatórios.

# python
if __name__ == "__main__":
    log_analyzer = LogAnalyzer(['server1__2024-05-01.txt', 'server1__2024-04-29.txt', 'server1__2024-04-30.txt'])
    log_analyzer.main_menu()

# Log Analyzer - EN Description

This project is a log analyzer that provides several functionalities to better understand log data.

## Description

The code is organized into a class called `LogAnalyzer`. The functions have been converted into methods of this class. Also, the function `analisar_logs` has been renamed to `_analyze_logs` and is called in the class constructor. This allows the logs to be analyzed as soon as an instance of the class is created. The functions that manipulate the logs are now methods that operate on the logs stored in the class instance. This makes the code more organized and easier to understand.

## Functions

The code contains the following functions:

1. `_analyze_logs(file_names)`: This private function takes a list of log file names and returns a list of logs. Each log is a tuple containing date, time, HTTP method, URI, status, response time, referrer IP, content type, message, transaction, and system user.

2. `daily_access_report()`: This function returns a report of daily accesses.

3. `average_response_time()`: This function returns the average response time.

4. `most_active_users()`: This function returns a dictionary of the most active users.

5. `most_accessed_pages()`: This function returns a dictionary of the most accessed pages.

6. `main_menu()`: This function presents a menu for the user to choose which report they want to see.

## How to use

First, you need to have a list of log files to analyze. Then, you can create an instance of the `LogAnalyzer` class and call the `main_menu` method to see the reports.

```python
if __name__ == "__main__":
    log_analyzer = LogAnalyzer(['server1__2024-05-01.txt', 'server1__2024-04-29.txt', 'server1__2024-04-30.txt'])
    log_analyzer.main_menu()

