import psycopg
print(psycopg)
class Usuario:
  def __init__(self, login, senha):
    self.login = login
    self.senha = senha

#verifica se o usuário recebido existe na base
def existe(usuario):
  #abrir uma conexão com o PostgreSQL
  #obter uma abstração do tipo "cursor"
  #executar um comando sql
  #verificar o resultado
  #devolver True ou False
  with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="20241_fatec_ipi_pbdi_login_python",
    user="postgres",
    password="123456"
  ) as conexao:
    with conexao.cursor() as cursor:
      cursor.execute(
        'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
        (usuario.login, usuario.senha)
      )
      result = cursor.fetchone()
      #return #se result for igual a None, devolvo False, senão devolvo True
      #return True if result != None else False
      return result != None
    
def inserir(usuario):
  with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="20241_fatec_ipi_pbdi_login_python",
    user="postgres",
    password="123456"
  ) as conexao:
    with conexao.cursor() as cursor:
      cursor.execute(
        'INSERT INTO tb_usuario(login, senha) VALUES (%s, %s)',
        (usuario.login, usuario.senha)
      )
      print('Inserção concluida!')
    
def menu():
  texto = '0-Sair\n1-Login\n2-Logoff\n3-Inserir Usuário\n'
  #usuário ainda não existe
  usuario = None
  op = int(input(texto))
  while op != 0:
    if op == 1:
      login = input('Digite o login: ')
      senha = input('Digite a senha: ')
      usuario = Usuario(login, senha)
      #expressão condicional de uma linha
      print('Usuário OK!' if existe(usuario) else 'Usuário NOK')
    elif op == 2:
      usuario = None
      print('Logoff realizado com sucesso')
    elif op == 3:
      login = input('Digite um usuário: ')
      senha = input('Digite uma senha: ')
      usuario = Usuario(login, senha)
      if existe(usuario) == True:
        print('Escreva um usuário novo')
      else:
        inserir(usuario)
    else:
      print('Jovem, somente valores entre 0, 1 e 2, plis!!')
    op = int(input(texto))

menu()

# def teste():
#   print(existe(Usuario('admin', 'admin')))

# teste()