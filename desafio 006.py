print(f"{'-' * 10} DESAFIO 006 {'-' * 10}")
print(f"{'-' * 33}")
print(f"{'':^32}")
print(f"{'-' * 33}")
frase = str(input("me de uma frase: "))
palavra = str(input("quer substituir alguma palavra [S/N]: "))
subtistua = str(input("Qual palavra você quer substituir?: "))
sub = str(input("Por qual: "))
print(f"Sua nova frase: {frase.replace(subtistua,sub)}")
