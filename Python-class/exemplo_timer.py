dia =input('Me informe o dia da semana: ')
if(dia == 'segunda' or dia == 'terça' or dia == 'quarta' or dia == 'quinta' or dia == 'sexta' or dia == 'sabado' or dia == 'domingo'):
    hA = int(input('Me informe a hora do alarme: '))
    mA = int(input('O minuto do alarme: '))
    sA = int(input('O sengundo do alarme: '))
    h = 0
    while (h < 24):
        m = 0
        while (m < 60):
            s = 0
            while (s < 60):
                print(f'{h:02}:{m:02}:{s:02}')
                if(h == hA and m == mA and s == sA):
                    print(f'ALARME! Agora sáo {h:02}h:{m:02}m:{s:02}s, da {dia}-feira.')
                    break
                s += 1
            if (h == hA and m == mA):
                break     
            m += 1
        if(h == hA):
            break
        h += 1
else:
   print('Informe dados válidos!')

