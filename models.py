from jogoteca import db

class Usuarios(db.Model):
    nome = db.Column(db.String(20), nullable = False, primary_key = True )
    senha = db.Column(db.String(8), nullable = False )
    def __repr__(self):
        return '<Name %r>' % self.nome
      
class Jogos(db.Model):
    id = db.Column(db.Integer, nullable = False, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    categoria = db.Column(db.String(20), nullable = False )
    console = db.Column(db.String(20), nullable = False )
    def __repr__(self):
        return '<Name %r>' % self.nome
    