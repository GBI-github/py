print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 26\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'MANIPULAÇÃO DE TEXTO' :^32}\033[0m")
print(f"{'LENDO FRASES':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
frase = str(input("Escreva um frase de sua escolha:)! : ")).lower().strip()
print(f"a letra 'a' foi repetida {frase.count('a')}")
print(f"A primeira letra 'a' aparece na posição {frase.find('a')+1}")
print(f"A ultima vez que aletra 'a' aparece é na posição {frase.rfind('a')+1}")
