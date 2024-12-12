class APIConnection:
    def connect_api(self):
        print("Conexão com a API realizada")

class TaskValidator:
    def validate_create_task(self, id: int, name: str):
        return isinstance(id, int) and isinstance(name, str)

    def validate_update_task(self, id: int):
        return isinstance(id, int)

    def validate_remove_task(self, id: int):
        return isinstance(id, int)
    
class SendNotification:
    def send(self, message):
        print(message)

class GenerateReport:
    def create_report(self):
        return("Ocorreu um erro ao executar a ação!")

class SendReport:
    def send_error(self, report):
        print(report)

class TaskHandler:
    def __init__(self, api_connection, task_validator, send_notification, generate_report, send_report):
        self.api_connection = api_connection
        self.task_validator = task_validator
        self.send_notification = send_notification
        self.generate_report = generate_report
        self.send_report = send_report

        self.api_connection.connect_api()

    def create_task(self, id: int, name: str):
        if self.task_validator.validate_create_task(id, name):
            self.send_notification.send("Task criada com sucesso")
        else:
            report = self.generate_report.create_report()
            self.send_report.send_error(report)

    def update_task(self, id: int):
        if self.task_validator.validate_update_task(id):
            self.send_notification.send(f"Task {id} atualizada com sucesso")
        else:
            report = self.generate_report.create_report()
            self.send_report.send_error(report)

    def remove_task(self, id: int):
        if self.task_validator.validate_remove_task(id):
            self.send_notification.send(f"Task {id} removida com sucesso")
        else:
            report = self.generate_report.create_report()
            self.send_report.send_error(report)

api_connection = APIConnection()
task_validator = TaskValidator()
send_notification = SendNotification()
generate_report = GenerateReport()
send_report = SendReport()
task_handler = TaskHandler(api_connection, task_validator, send_notification, generate_report, send_report)

task_handler.remove_task(30)