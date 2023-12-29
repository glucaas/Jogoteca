SECRET_KEY = 'hadouken' ## precisa disso para poder conseguir salvar as informacoes do cookie baseada em uma paravra secreta

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'myuser',
        senha = '123',
        servidor = '172.19.0.2', #ip da minha network no WSL2
        #172.28.0.2
        #172.28.0.1
        #porta = '3306', desnecessario por enquanto
        database = 'mydatabase'
    )  