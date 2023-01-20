def ex_01_ola_mundo() -> str:
    """
    https://wiki.python.org.br/EstruturaSequencial
    Escreva um programa que mostre a mensagem "Olá, Mundo!"
    """
    return "Olá, Mundo!"


def ex_02_escreva_um_numero(num):
    """
    https://wiki.python.org.br/EstruturaSequencial
    Faça um Programa que peça um número e então mostre a mensagem: O número informado foi [número].
    >>> ex_02_escreva_um_numero(42)
    O número informado foi 42.
    """
    return f"O número informado foi {num}."


def ex_03_imprima_a_soma_de_dois_numeros(a, b):
    """
    https://wiki.python.org.br/EstruturaSequencial
    Faça um Programa que peça dois números inteiros e imprima a soma.
    >>> numeros = [42, 43]
    >>> ex_03_imprima_a_soma_de_dois_numeros(*numeros)
    A soma dos dois números informados é 85.
    """
    return f"A soma dos dois números informados é {a+b}."


def ex_04_calcular_media(notas):
    """
    https://wiki.python.org.br/EstruturaSequencial
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.
    >>> ex_04_calcular_media(['7', '8','9','10'])
    A média anual é 8.5.
    """
    notas_float = list(map(float, notas))
    media = sum(notas_float) / len(notas_float)
    return f"A média anual é {media}."


def ex_05_converter_metros_para_centimetros(comprimento):
    """
    https://wiki.python.org.br/EstruturaSequencial
    Faça um Programa que converta metros para centímetros.
    >>> ex_05_converter_metros_para_centimetros(1)
    'Transformando para centímetros dá 100.0 cm.'
    >>> ex_05_converter_metros_para_centimetros(3.621)
    'Transformando para centímetros dá 362.1 cm.'
    """
    return f"Transformando para centímetros dá {comprimento * 100.0} cm."


def ex_06_calcular_area_do_circulo(raio):
    """
    https://wiki.python.org.br/EstruturaSequencial
    Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. Mostrar a área com 4 casas decimais.
    Observação: Use o valor de 3.1415 para o valor da constante π
    >>> ex_06_calcular_area_do_circulo(1)
    'A área do círculo com esse raio é: 3.1415'
    >>> ex_06_calcular_area_do_circulo(2.5)
    'A área do círculo com esse raio é: 19.6344'
    """
    area = 3.1415 * (raio*raio)
    return f"A área do círculo com esse raio é: {area:.4f}"


def ex_07_calcular_area_de_quadrado():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
    Mostrar a área com 2 casas decimais.

    >>> from secao_01_estrutura_sequencial import ex_07_area_quadrado
    >>> ex_07_area_quadrado.input = lambda k: '2'
    >>> ex_07_area_quadrado.calcular_area_de_quadrado()
    A área do quadrado com esse lado é: 4.00
    O dobro da aŕea do quadrado é: 8.00
    >>> ex_07_area_quadrado.input = lambda k: '2.5'
    >>> ex_07_area_quadrado.calcular_area_de_quadrado()
    A área do quadrado com esse lado é: 6.25
    O dobro da aŕea do quadrado é: 12.50

    """
    return


def ex_08_calcular_salario():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês.
    Mostrar salário com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_08_horas_trabalhadas_mes
    >>> numeros =['80', '55.62']
    >>> ex_08_horas_trabalhadas_mes.input = lambda k: numeros.pop()
    >>> ex_08_horas_trabalhadas_mes.calcular_salario()
    Seu salário desse mês é 4449.60

    """
    return


def ex_09_transformar_para_celsius():
    """
    https://wiki.python.org.br/EstruturaSequencial
    Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9)
    Mostrar apenas valor inteiro da temperatura

    >>> from secao_01_estrutura_sequencial import ex_09_fahrenheit_para_celsius
    >>> ex_09_fahrenheit_para_celsius.input = lambda k: '0'
    >>> ex_09_fahrenheit_para_celsius.transformar_para_celsius()
    Essa temperatura é de -18 Celsius
    >>> ex_09_fahrenheit_para_celsius.input = lambda k: '70'
    >>> ex_09_fahrenheit_para_celsius.transformar_para_celsius()
    Essa temperatura é de 21 Celsius
    """
    return


def ex_10_transformar_para_fahrenheit():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
    Mostrar apenas valor inteiro da temperatura

        >>> from secao_01_estrutura_sequencial import ex_10_celsius_para_fahrenheit
        >>> ex_10_celsius_para_fahrenheit.input = lambda k: '0'
        >>> ex_10_celsius_para_fahrenheit.transformar_para_fahrenheit()
        Essa temperatura é de 32 Fahrenheit
        >>> ex_10_celsius_para_fahrenheit.input = lambda k: '21'
        >>> ex_10_celsius_para_fahrenheit.transformar_para_fahrenheit()
        Essa temperatura é de 70 Fahrenheit

    """
    return


def ex_11_calcular_formulas():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
     1) o produto do dobro do primeiro com metade do segundo;
     2) a soma do triplo do primeiro com o terceiro;
     3) o terceiro elevado ao cubo.

     Apresente os resultados com duas casas decimais

        >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
        >>> numeros = ['3.14', '43', '42']
        >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
        >>> ex_11_contas_matematicas.calcular_formulas()
        O produto do dobro do primeiro com metade do segundo é 1806.00
        A soma do triplo do primeiro com o terceiro é 129.14
        O terceiro elevado ao cubo é 30.96

    """
    return


def ex_12_calcular_peso_ideal():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte
    fórmula: (72.7*altura) - 58
    Mostrar a área com 1 casa decimal.

        >>> from secao_01_estrutura_sequencial import ex_12_peso_ideal
        >>> ex_12_peso_ideal.input = lambda k: '1.62'
        >>> ex_12_peso_ideal.calcular_peso_ideal()
        Seu peso ideal é 59.8 kg
        >>> ex_12_peso_ideal.input = lambda k: '1.80'
        >>> ex_12_peso_ideal.calcular_peso_ideal()
        Seu peso ideal é 72.9 kg

    """
    return


def ex_13_calcular_peso_ideal():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
    utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
    Mostrar a área com 1 casa decimal.

        >>> from secao_01_estrutura_sequencial import ex_13_peso_ideal_mulher_e_homem
        >>> ex_13_peso_ideal_mulher_e_homem.input = lambda k: '1.62'
        >>> ex_13_peso_ideal_mulher_e_homem.calcular_peso_ideal()
        Seu peso ideal é 55.9 kg, se você for mulher
        Seu peso ideal é 59.8 kg, se você for homem
        >>> ex_13_peso_ideal_mulher_e_homem.input = lambda k: '1.80'
        >>> ex_13_peso_ideal_mulher_e_homem.calcular_peso_ideal()
        Seu peso ideal é 67.1 kg, se você for mulher
        Seu peso ideal é 72.9 kg, se você for homem

    """
    return


def ex_14_calcular_peso_excedente_e_multa():
    """
    https://wiki.python.org.br/EstruturaSequencial

    João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
    Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
    São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
    João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
    Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá
    pagar.
    Imprima os dados do programa com as mensagens adequadas.
    Mostrar o peso e multa com duas casas decimais

        >>> from secao_01_estrutura_sequencial import ex_14_joao_papo_de_pescador
        >>> ex_14_joao_papo_de_pescador.input = lambda k: '62.35'
        >>> ex_14_joao_papo_de_pescador.calcular_peso_excedente_e_multa()
        O peso excedente de peixes é de 12.35 kg
        Por isso, a multa é de R$ 49.40
        >>> ex_14_joao_papo_de_pescador.input = lambda k: '50'
        >>> ex_14_joao_papo_de_pescador.calcular_peso_excedente_e_multa()
        O peso excedente de peixes é de 0.00 kg
        Por isso, a multa é de R$ 0.00

    """
    return


def ex_15_calcular_assalto_no_salario():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
    8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido
    Mostrar os resultados com duas casas decimais

        >>> from secao_01_estrutura_sequencial import ex_15_clt_onerosa
        >>> numeros =['80', '55.62']
        >>> ex_15_clt_onerosa.input = lambda k: numeros.pop()
        >>> ex_15_clt_onerosa.calcular_assalto_no_salario()
        + Salário Bruto : 4449.60
        - IR (11%) : R$ 489.46
        - INSS (8%) : R$ 355.97
        - Sindicato ( 5%) : R$ 222.48
        = Salário Liquido : R$ 3381.70

    """
    return


def ex_16_calcular_latas_e_preco_de_tinta():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Faça um programa para uma loja de tintas.
    O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
    18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

        >>> from secao_01_estrutura_sequencial import ex_16_loja_de_tintas_simples
        >>> ex_16_loja_de_tintas_simples.input = lambda k: '50'
        >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
        Você deve comprar 1 lata(s) tinta ao custo de R$ 80.00
        >>> ex_16_loja_de_tintas_simples.input = lambda k: '100'
        >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
        Você deve comprar 2 lata(s) tinta ao custo de R$ 160.00


    """
    return


def ex_17_calcular_latas_e_preco_de_tinta():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
    Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
    que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o custo seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

        >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
        >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
        >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
        Você deve comprar 19 litros de tinta.
        Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
        Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
        Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105.
        Vão sobrar 2.6 litro(s) de tinta.
        >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
        >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
        Você deve comprar 37 litros de tinta.
        Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
        Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
        Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185.
        Vão sobrar 2.6 litro(s) de tinta.

    """
    return


def ex_18_calcular_tempo_de_download():
    """
    https://wiki.python.org.br/EstruturaSequencial

    Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
    calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
    Arredonde o tempo em minutos

        >>> from secao_01_estrutura_sequencial import ex_18_tempo_de_download
        >>> numeros =['50', '2500']
        >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
        >>> ex_18_tempo_de_download.calcular_tempo_de_download()
        O tempo aproximado do Download é: 7 minuto(s)
        >>> numeros =['100', '2500']
        >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
        >>> ex_18_tempo_de_download.calcular_tempo_de_download()
        O tempo aproximado do Download é: 3 minuto(s)

    """
    return
