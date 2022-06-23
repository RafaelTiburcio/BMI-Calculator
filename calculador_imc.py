nome = input("Olá, me diga seu nome:")
print("Olá, {}!".format(nome))

peso = int(input("Qual é o seu peso atual?"))
altura = float(input("Agora me fala a sua altura em metros ( use ponto ):"))
IMC = peso / altura**2

if IMC < 18.5:
    print("seu IMC é: {:.2f} e você se encontra abaixo do peso.".format(IMC))

elif IMC >= 18.5 and IMC <= 24.9:
    print("seu IMC é: {:.2f} e você se encontra em seu peso normal.".format(IMC))

elif IMC > 24.9 and IMC < 30:
    print("seu IMC é: {:.2f} e você se encontra em sobrepeso.".format(IMC))

elif IMC >= 30 and IMC < 35:
    print("seu IMC é: {:.2f} e você se encontra em estado de obesidade grau I.\n" "Procure um nutricionista para melhorar sua saúde!".format(IMC))

elif IMC >= 35 and IMC < 40:
        print("seu IMC é: {:.2f} e você se encontra em estado de obesidade grau II.\n" "Procure um nutricionista para melhorar sua saúde!".format(IMC))

elif IMC >= 40:
        print("seu IMC é: {:.2f} e você se encontra em estado de obesidade Mórbida.\n" "Procure um nutricionista para melhorar sua saúde!".format(IMC))










