salario = float(input('Digite o salário da pessoa:'))

if salario < 1001:
    novo_salario = salario*1.2
    aumento = novo_salario-salario
    print(f'Novo salario: R${novo_salario:.2f}')
    print(f'Aumento:R${aumento:.2f}')
    print('Porcentagem = 20%')
elif 1000 > salario < 3000:
    novo_salario = salario*1.15
    aumento = novo_salario-salario
    print(f'Novo salario: R${novo_salario:.2f}')
    print(f'Aumento:R${aumento:.2f}')
    print('Porcentagem = 15%')
elif 3000 > salario < 8000:
    novo_salario = salario*1.10
    aumento = novo_salario-salario
    print(f'Novo salario: R${novo_salario:.2f}')
    print(f'Aumento:R${aumento:.2f}')
    print('Porcentagem = 10%')
else:
    novo_salario = salario * 1.05
    aumento = novo_salario - salario
    print(f'Novo salario: R${novo_salario:.2f}')
    print(f'Aumento:R${aumento:.2f}')
    print('Porcentagem = 5%')
