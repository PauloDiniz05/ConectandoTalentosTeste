
import entity
def test_usuario_cadastro():
    """Testa se um Usuário consegue ser inicializado corretamente"""
    nome = "Felipe Martins"
    email = "felipemartinsbn@gmail.com.br"
    area_interesse = ["Dev", "Java"]
    
    usuario = entity.Usuario(nome, email, area_interesse)
    print(usuario)
    assert usuario.nome == nome
    assert usuario.email == email
    assert usuario.area_interesse == area_interesse
    assert usuario.vagas_cadastradas == []

def test_usuario_cadastro_email_errado():
    """Verifica se o sistema bloqueia a criação com um e-mail inválido"""
    nome = "Felipe Martins"
    email = "felipemartinsbn"
    area_interesse = ["Dev", "Java"]

    try:   
        usuario = entity.Usuario(nome, email, area_interesse)
        assert False
    except Exception as e:
        assert str(e) == "Email Inválido"

def verificar_candidatar():
    """Verifica se o usuário consegue se candidatar a uma vaga"""
    estudante = entity.Usuario("Paulo", "Tusiozshi@airbus.com")
    