"""
Thanks everyone
My GitHub: https://github.com/reachesblue
"""

import string
import random
import time

print('Gerador de senha')

quantas_senhas = int(input('Digite quantas senhas quer que seja gerada: '))
tamanho_da_senha = int(input('Digite o tamanho da senha que você quer: '))
print('Gerando... Aguarde')
time.sleep(0.5)

for x in range(quantas_senhas):
    senha = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=tamanho_da_senha))
    print(senha)
    with open('Passwords.txt','a+') as f:
        f.write(senha+"\n")