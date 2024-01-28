from jogoteca import app, db
from models import Jogos, Usuarios
from flask import render_template, request, redirect, session, flash, url_for, logging

@app.route('/')
def index():
    lista_jogos = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo = 'Jogos', jogos = lista_jogos)

@app.route('/novo')
def novo():
    if('usuario_logado' not in session or session['usuario_logado'] is None):
        return redirect(url_for('login',redirect_url = url_for('novo')))
        ##return redirect('/login?redirect_url=novo') antes, mas depois de deixar a url dinamica
    return render_template('novo.html', titulo = 'Cadastro de novo Jogo') 

@app.route('/criar', methods = ['POST']) ##dizendo que essa rota permite um post que é o envio do formulario
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos.query.filter_by(nome = nome).first()
    if jogo:
        flash('Jogo ja existente')
        return redirect(url_for('index'))
    
    novo_jogo = Jogos(nome = nome, categoria = categoria, console = console)
    db.session.add(novo_jogo)
    db.session.commit()
    
    arquivo = request.files['arquivo']
    arquivo.save(f'uploads/{arquivo.filename}')
    arquivo.close()
    
    return redirect(url_for('index')) 

@app.route('/editar/<int:id>')
def editar(id):
    if('usuario_logado' not in session or session['usuario_logado'] is None):
        return redirect(url_for('login',redirect_url = url_for('editar')))
        ##return redirect('/login?redirect_url=novo') antes, mas depois de deixar a url dinamica
        
    jogo = Jogos.query.filter_by(id = id).first()
    return render_template('editar.html', titulo = 'Editando Jogo', jogo = jogo) 

@app.route('/atualizar', methods = ['POST'])
def atualizar():
    id = request.form['id']
    jogo = Jogos.query.filter_by(id = id).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']
    
    db.session.add(jogo)
    db.session.commit()
    
    return redirect(url_for('index'))
    
@app.route('/deletar/<int:id>')
def deletar(id):
    if('usuario_logado' not in session or session['usuario_logado'] is None):
        return redirect(url_for('login'))
    
    jogo = Jogos.query.filter_by(id = id).first()
    
    db.session.delete(jogo)
    db.session.commit()
    
    flash(f'O jogo: {jogo.nome} deletado com sucesso')
    return redirect(url_for('index'))
    
@app.route('/login')
def login():
    redirect_url = request.args.get('redirect_url')
    return render_template('login.html', redirect_url = redirect_url)
    
@app.route('/autenticar', methods = ['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    redirect_url = request.form['redirect_url']
    usr_banco = Usuarios.query.filter_by(nome = usuario).first()
    if(usr_banco):
        if(usr_banco.senha == senha):
            session['usuario_logado'] = usuario ##trabalhando com cookie
            flash('Usuário logado com sucesso !')
            ##return redirect(f'/{redirect_url}')
            return redirect(redirect_url) ##novo formato       
    flash('Usuário inexistente. Tente novamente')
    if(redirect_url is None):
        ##return redirect('/login')
        return redirect(url_for('login'))
    
    #return redirect(f'/login?redirect_url={redirect_url}')
    return redirect(url_for('login', redirect_url = redirect_url))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index')) 
