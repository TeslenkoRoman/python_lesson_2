import requests

ip = requests.get("https://api.ipify.org").text
print('Мой ip адрес: {}'.format(ip))

