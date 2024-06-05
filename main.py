class LogAnalyzer:
    def __init__(self, file_names):
        self.logs = self._analyze_logs(file_names)

    def _analyze_logs(self, file_names):
        logs = []
        for file_name in file_names:
            with open(file_name, 'r') as file:
                lines = file.readlines()

            for line in lines:
                log_data = line.split('\t')
                logs.append(tuple(log_data))
        return logs

    def daily_access_report(self):
        report = {}
        for log in self.logs:
            access_date = log[0]
            report[access_date] = report.get(access_date, 0) + 1
        return report

    def average_response_time(self):
        total_time = sum(float(log[5]) for log in self.logs)
        return total_time / len(self.logs)

    def most_active_users(self):
        users = {}
        for log in self.logs:
            user = log[6]
            users[user] = users.get(user, 0) + 1
        return users

    def most_accessed_pages(self):
        pages = {}
        for log in self.logs:
            page = log[3]
            pages[page] = pages.get(page, 0) + 1
        return pages

    def main_menu(self):
        while True:
            print("====== MENU ======")
            print("1. Relatório Diário de Acessos")
            print("2. Tempo Médio de Resposta")
            print("3. Usuários Mais Ativos")
            print("4. Páginas Mais Acessadas")
            print("5. Sair")
            option = int(input("Selecione uma opção: "))
            if option == 1:
                report = self.daily_access_report()
                for date, accesses in report.items():
                    print(f'Data: {date}, Acessos: {accesses}')
            elif option == 2:
                avg_time = self.average_response_time()
                print(f'Tempo Médio de Resposta: {avg_time}')
            elif option == 3:
                users = self.most_active_users()
                for user, accesses in users.items():
                    print(f'Usuário: {user}, Acessos: {accesses}')
            elif option == 4:
                pages = self.most_accessed_pages()
                for page, accesses in pages.items():
                    print(f'Página: {page}, Acessos: {accesses}')
            elif option == 5:
                print("Você selecionou Sair")
                print("\nFIM DO PROGRAMA")
                break
            else:
                print("Opção Inválida")
                print("FIM DO PROGRAMA")
                break


if __name__ == "__main__":
    log_analyzer = LogAnalyzer(['server1__2024-05-01.txt', 'server1__2024-04-29.txt', 'server1__2024-04-30.txt'])
    log_analyzer.main_menu()
