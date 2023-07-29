expressao = input('Digite uma expressão: ')
if expressao.index(')') < expressao.index('(') :
    print('A expressão NAO foi iniciado corretamente')
if expressao.count('(') != expressao.count(')'):
    print('Sua expressão não está corretamenta!!!')
if expressao.rindex(')') < expressao.rindex('(') :
    print('A expressão NÃO foi finalizada corretamente')
else:
    if expressao.rindex(')') > expressao.rindex('(') and expressao.count('(') == expressao.count(')') and expressao.index(')') > expressao.index('('):
        print('Sua expressão está em pleno funcionamento, parabéns!!!')