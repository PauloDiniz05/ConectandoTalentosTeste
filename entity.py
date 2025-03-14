import re

class Usuario:
    def __init__(self, nome: str, email: str, area_interesse: str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not (re.fullmatch(regex, email)):
            raise Exception("Email Inválido")
        self.nome = nome
        self.email = email
        self.area_interesse = area_interesse
        self.vagas_cadastradas = []

    def __repr__(self):
        return (
        f"Usuário(nome={self.nome}, email={self.email}, interesse={self.area_interesse}, "
        f"Vagas Candidatadas={self.vagas_cadastradas})"
    )

    
    def canidatar(self, vaga):
        self.vagas_cadastradas.append(vaga)

class Empresa:
    def __init__(self, nome: str, setor: str):
        self.nome = nome
        self.setor = setor
        self.vagas = []

    def criar_vaga(self, titulo: str, descricao: str, requisitos: list):
        vaga = Vaga(self, titulo, descricao, requisitos)
        self.vagas.append(vaga)
        return vaga

    def __repr__(self):
        return f"Empresa(nome={self.nome}, setor={self.setor})"


class Vaga:
    def __init__(self, empresa: Empresa, titulo: str, descricao: str, requisitos: list):
        self.empresa = empresa
        self.titulo = titulo
        self.descricao = descricao
        self.requisitos = requisitos
        self.candidatos = []

    def candidatar(self, usuario: Usuario):
        if usuario.area_interesse in self.requisitos:
            self.candidatos.append(usuario)
            return f"{usuario.nome} se candidatou para a vaga {self.titulo}."
        else:
            return f"{usuario.nome} não atende aos requisitos da vaga."

    def __repr__(self):
        return f"Vaga(titulo={self.titulo}, empresa={self.empresa.nome}, candidatos={len(self.candidatos)})"
