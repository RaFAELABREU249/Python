from flask import render_template, request, redirect, url_for, flash, session
from app.controllers.auth import bp
from app.controllers.common import login_obrigatorio
from app.services.auth_service import validar_credenciais, registrar_usuario


@bp.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('tasks.dashboard'))
    return redirect(url_for('auth.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '')

        if not email or not senha:
            flash('Email e senha são obrigatórios.', 'danger')
            return redirect(url_for('auth.login'))

        usuario, erro = validar_credenciais(email, senha)
        if erro:
            flash(erro, 'danger')
            return redirect(url_for('auth.login'))

        session.clear()
        session['user_id'] = usuario.id
        session['username'] = usuario.nome
        flash('Login realizado com sucesso.', 'success')
        return redirect(url_for('tasks.dashboard'))

    return render_template('login.html')


@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip().lower()
        senha = request.form.get('senha', '')
        confirma = request.form.get('confirma', '')

        usuario, erro = registrar_usuario(nome, email, senha, confirma)
        if erro:
            flash(erro, 'danger')
            return redirect(url_for('auth.registro'))

        flash('Cadastro concluído. Faça login agora.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('registro.html')


@bp.route('/logout')
@login_obrigatorio
def logout():
    session.clear()
    flash('Você saiu com sucesso.', 'info')
    return redirect(url_for('auth.login'))
