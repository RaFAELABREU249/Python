import requests
from functools import wraps
from flask import redirect, url_for, session

STATUS_OPTIONS = ['pendente', 'em andamento', 'concluido']


def get_daily_advice():
    try:
        response = requests.get('https://api.adviceslip.com/advice', timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get('slip', {}).get('advice', 'Mantenha o foco e faça hoje o seu melhor!')
    except Exception:
        return 'Mantenha o foco e faça hoje o seu melhor!'


def login_obrigatorio(func):
    @wraps(func)
    def decorado(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return decorado
