import requests


def obter_conselho_diario():
    try:
        response = requests.get('https://api.adviceslip.com/advice', timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get('slip', {}).get('advice', 'Mantenha o foco e faça hoje o seu melhor!')
    except Exception:
        return 'Mantenha o foco e faça hoje o seu melhor!'
