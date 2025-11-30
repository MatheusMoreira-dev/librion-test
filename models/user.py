# classe de usuário genérico
class User():
    def __init__(self, name: str, email: str, password: str, cep: str):
        self.name = name
        self.email = email
        self.password = password
        self.cep = cep
        self.admin = False