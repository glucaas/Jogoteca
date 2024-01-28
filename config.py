import os

SECRET_KEY = 'hadouken' ## precisa disso para poder conseguir salvar as informacoes do cookie baseada em uma paravra secreta

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'myuser',
        senha = '123',
        servidor = '172.20.0.1', #ip da minha network no WSL2
        #172.28.0.2
        #172.28.0.1
        #porta = '3306', desnecessario por enquanto
        database = 'mydatabase'
    )  

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

## __file__ give us the reference of this file on our desktop
## os.path.abspath('__file__') we get the absolute path to this file, not for the folder
## dirname returns the name of folder