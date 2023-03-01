sp = 67836.43
rj = 36678.66
mg =  29229.88
es = 27165.48
outros = 19849.53
total = sp + rj + mg + es + outros
print(f'O valor total mensal da distribuidora é: {total}')
porcentagem_rj = (rj/total)*100
porcentagem_sp = (sp/total)*100
porcentagem_mg = (mg/total)*100
porcentagem_es = (es/total)*100
porcentagem_outros = (outros/total)*100
print(f'Porcentagem do RJ(Rio de Janeiro): {porcentagem_rj:.2f}%')
print(f'Porcentagem de SP(São Paulo): {porcentagem_sp:.2f}%')
print(f'Porcentagem de MG(Minas Gerais): {porcentagem_mg:.2f}%')
print(f'Porcentagem do ES(Espírito Santo): {porcentagem_es:.2f}%')
print(f'Porcentagem dos outros estados: {porcentagem_outros:.2f}%')