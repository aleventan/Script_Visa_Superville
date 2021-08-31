#import ast
import locale
from lector import *
from variablesGlobales import *

locale.setlocale(locale.LC_ALL, '')

class cuotas(lector):
    def __init__(self, cuota):
        self._cuota = cuota

    sumaCuotas = 0
    sumaCuotasVencen = 0
    sumaCuotasVencenDespues1 = 0
    sumaCuotasVencenDespues2 = 0
    sumaCuotasVencenDespues3 = 0
    sumaCuotasVencenDespues4 = 0
    sumaCuotasVencenDespues5 = 0
    sumaCuotasVencenDespues6 = 0


    @property
    def cuota(self):
        return self.cuota

    @cuota.setter
    def cuota(self, cuota):
        self._cuota = cuota


    def formatoCuotas():
        try:
            escribir = open(variablesGlobales.salidaResumen, 'a', encoding='utf8')

            cabecera = ' LISTADO DE CUOTAS '
            escribir.writelines('*'.center(72, '*') + '\n')
            escribir.writelines(cabecera.center(72, '*') + '\n')
            escribir.writelines('*'.center(72, '*') + '\n')
            # print('*'.center(72, '*'))
            # print(cabecera.center(72, '*'))
            # print('*'.center(72, '*'))
            sumaCuotas = 0

            for separoCuota in listadoRegistrosCuotas:
                # print(separoCuota)
                escribir.writelines(separoCuota + '\n')
                monto = separoCuota[62:].lstrip()
                # Llama a la clase locale para poder convertir a float el string de ese registro
                nvoMonto = locale.atof(monto)
                sumaCuotas = sumaCuotas + nvoMonto
            cuotas.sumaCuotas = sumaCuotas
            mensaje = 'El monto total de la suma de las cuotas de este mes es: $' + formatoNumero(sumaCuotas)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje + '\n')
            escribir.close()
        except Exception as e:
            print(f'Se produjo un error en FormatoCuotas: {e}')

    def cuotasVencenAhora():
        try:
            escribir = open(variablesGlobales.salidaResumen, 'a', encoding='utf8')
            cabecera = ' LISTADO DE CUOTAS QUE VENCEN ESTE MES '
            escribir.writelines('*'.center(72, '*') + '\n')
            escribir.writelines(cabecera.center(72, '*')+ '\n')
            escribir.writelines('*'.center(72, '*') + '\n')
            # print('*'.center(72, '*'))
            # print(cabecera.center(72, '*'))
            # print('*'.center(72, '*'))
            sumaCuotasVencen = 0
            for separoCuota in listadoRegistrosCuotas:
                cuotaVence = separoCuota[36:38]
                cuotaTotales = separoCuota[39:41]
                monto = separoCuota[62:].lstrip()
                nvoMonto = locale.atof(monto)
                if cuotaVence == cuotaTotales:
                    # print(separoCuota)
                    escribir.writelines(separoCuota + '\n')
                    sumaCuotasVencen += nvoMonto
            cuotas.sumaCuotasVencen = sumaCuotasVencen
            mensaje = 'El monto total de la suma de las cuotas que vencen este mes es: $' + formatoNumero(
                sumaCuotasVencen)
            escribir.writelines('\n' + mensaje + '\n')
            # print('\n' + mensaje)
        except Exception as e:
            print(f'Se produjo un error en CuotasVencenAhora: {e}')
    
    def cuotasVencenDespues():
        try:
            escribir = open(variablesGlobales.salidaResumen, 'a', encoding='utf8')
            cabecera = ' LISTADO DE CUOTAS QUE VENCEN.. '
            # print('*'.center(72, '*'))
            # print(cabecera.center(72, '*'))
            # print('*'.center(72, '*'))
            escribir.writelines('*'.center(72, '*') + '\n')
            escribir.writelines(cabecera.center(72, '*')+ '\n')
            escribir.writelines('*'.center(72, '*')+ '\n')
            sumaCuotasVencenDespues1 = 0
            sumaCuotasVencenDespues2 = 0
            sumaCuotasVencenDespues3 = 0
            sumaCuotasVencenDespues4 = 0
            sumaCuotasVencenDespues5 = 0
            sumaCuotasVencenDespues6 = 0
            listaFalta1 = []
            listaFalta2 = []
            listaFalta3 = []
            listaFalta4 = []
            listaFalta5 = []
            listaFalta6 = []
            for separoCuota in listadoRegistrosCuotas:
                cuotaVence = locale.atof(separoCuota[36:38])
                cuotaTotales = locale.atof(separoCuota[39:41])
                monto = separoCuota[62:].lstrip()
                nvoMonto = locale.atof(monto)
                resultado = cuotaTotales - cuotaVence
                if resultado == 1:
                    listaFalta1.append(separoCuota)
                    sumaCuotasVencenDespues1 += nvoMonto
                    cuotas.sumaCuotasVencenDespues1 = sumaCuotasVencenDespues1
                elif resultado == 2:
                    listaFalta2.append(separoCuota)
                    sumaCuotasVencenDespues2 += nvoMonto
                    cuotas.sumaCuotasVencenDespues2 = sumaCuotasVencenDespues2
                elif resultado == 3:
                    listaFalta3.append(separoCuota)
                    sumaCuotasVencenDespues3 += nvoMonto
                    cuotas.sumaCuotasVencenDespues3 = sumaCuotasVencenDespues3
                elif resultado == 4:
                    listaFalta4.append(separoCuota)
                    sumaCuotasVencenDespues4 += nvoMonto
                    cuotas.sumaCuotasVencenDespues4 = sumaCuotasVencenDespues4
                elif resultado == 5:
                    listaFalta5.append(separoCuota)
                    sumaCuotasVencenDespues5 += nvoMonto
                    cuotas.sumaCuotasVencenDespues5 = sumaCuotasVencenDespues5
                elif resultado == 6:
                    listaFalta6.append(separoCuota)
                    sumaCuotasVencenDespues6 += nvoMonto
                    cuotas.sumaCuotasVencenDespues6 = sumaCuotasVencenDespues6

            # print('El próximo mes'.center(72, '-'))
            escribir.writelines('El próximo mes'.center(72, '-') + '\n')
            for reg in listaFalta1:
                # print(reg)
                escribir.writelines(reg + '\n')
            mensaje = 'El monto total de la suma de las cuotas que vencen el próximo mes es: $' + formatoNumero(
                sumaCuotasVencenDespues1)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje + '\n')

            # print('En 2 meses'.center(72, '-'))
            escribir.writelines('En 2 meses'.center(72, '-')+ '\n')
            for reg in listaFalta2:
                # print(reg)
                escribir.writelines(reg+ '\n')
            mensaje = 'El monto total de la suma de las cuotas que vencen en 2 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues2)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje+ '\n')

            # print('En 3 meses'.center(72, '-'))
            escribir.writelines('En 3 meses'.center(72, '-')+ '\n')
            for reg in listaFalta3:
                # print(reg)
                escribir.writelines(reg+ '\n')
            mensaje = 'El monto total de la suma de las cuotas que vencen en 3 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues3)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje+ '\n')

            # print('En 4 meses'.center(72, '-'))
            escribir.writelines('En 4 meses'.center(72, '-')+ '\n')
            for reg in listaFalta4:
                # print(reg)
                escribir.writelines(reg+ '\n')

            mensaje = 'El monto total de la suma de las cuotas que vencen en 4 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues4)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje+ '\n')

            escribir.writelines('En 5 meses'.center(72, '-')+ '\n')
            # print('En 5 meses'.center(72, '-'))
            for reg in listaFalta5:
                escribir.writelines(reg+ '\n')
                # print(reg)
            mensaje = 'El monto total de la suma de las cuotas que vencen en 5 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues5)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje+ '\n')

            escribir.writelines('En 6 meses'.center(72, '-')+ '\n')
            # print('En 6 meses'.center(72, '-'))
            for reg in listaFalta6:
                escribir.writelines(reg+ '\n')
                # print(reg)
            mensaje = 'El monto total de la suma de las cuotas que vencen en 6 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues6)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje+ '\n')
        except Exception as e:
            print(f'Se produjo un error en CuotasVencenDespues: {e}')
    def montosPagar():
        try:
            escribir = open(variablesGlobales.salidaResumen, 'a', encoding='utf8')
            cabecera = ' MONTOS A PAGAR DE CUOTAS EN LOS PRÓXIMOS MESES '
            # print('*'.center(72, '*'))
            # print(cabecera.center(72, '*'))
            # print('*'.center(72, '*'))
            escribir.writelines('*'.center(72, '*')+ '\n')
            escribir.writelines(cabecera.center(72, '*')+ '\n')
            escribir.writelines('*'.center(72, '*')+ '\n')
            sumaCuotasVencenDespues1 = 0
            sumaCuotasVencenDespues2 = 0
            sumaCuotasVencenDespues3 = 0
            sumaCuotasVencenDespues4 = 0
            sumaCuotasVencenDespues5 = 0
            sumaCuotasVencenDespues6 = 0
            listaFalta1 = []
            listaFalta2 = []
            listaFalta3 = []
            listaFalta4 = []
            listaFalta5 = []
            listaFalta6 = []
            for separoCuota in listadoRegistrosCuotas:
                cuotaVence = locale.atof(separoCuota[36:38])
                cuotaTotales = locale.atof(separoCuota[39:41])
                monto = separoCuota[62:].lstrip()
                nvoMonto = locale.atof(monto)
                resultado = cuotaTotales - cuotaVence
                if resultado >= 1:
                    listaFalta1.append(separoCuota)
                    sumaCuotasVencenDespues1 += nvoMonto
                    cuotas.sumaCuotasVencenDespues1 = sumaCuotasVencenDespues1
                if resultado >= 2:
                    listaFalta2.append(separoCuota)
                    sumaCuotasVencenDespues2 += nvoMonto
                    cuotas.sumaCuotasVencenDespues2 = sumaCuotasVencenDespues2
                if resultado >= 3:
                    listaFalta3.append(separoCuota)
                    sumaCuotasVencenDespues3 += nvoMonto
                    cuotas.sumaCuotasVencenDespues3 = sumaCuotasVencenDespues3
                if resultado >= 4:
                    listaFalta4.append(separoCuota)
                    sumaCuotasVencenDespues4 += nvoMonto
                    cuotas.sumaCuotasVencenDespues4 = sumaCuotasVencenDespues4
                if resultado >= 5:
                    listaFalta5.append(separoCuota)
                    sumaCuotasVencenDespues5 += nvoMonto
                    cuotas.sumaCuotasVencenDespues5 = sumaCuotasVencenDespues5
                if resultado >= 6:
                    listaFalta6.append(separoCuota)
                    sumaCuotasVencenDespues6 += nvoMonto
                    cuotas.sumaCuotasVencenDespues6 = sumaCuotasVencenDespues6

            # print('El próximo mes'.center(72, '-'))
            escribir.writelines('El próximo mes'.center(72, '-') + '\n')
            for reg in listaFalta1:
                # print(reg)
                escribir.writelines(reg + '\n')
            mensaje = 'El monto total de la suma de las cuotas que se abonan el próximo mes es: $' + formatoNumero(
                sumaCuotasVencenDespues1)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje + '\n')

            # print('En 2 meses'.center(72, '-'))
            escribir.writelines('En 2 meses'.center(72, '-') + '\n')
            for reg in listaFalta2:
                # print(reg)
                escribir.writelines(reg + '\n')
            mensaje = 'El monto total de la suma de las cuotas que se abonan en 2 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues2)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje + '\n')

            # print('En 3 meses'.center(72, '-'))
            escribir.writelines('En 3 meses'.center(72, '-') + '\n')
            for reg in listaFalta3:
                # print(reg)
                escribir.writelines(reg + '\n')
            mensaje = 'El monto total de la suma de las cuotas que se abonan en 3 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues3)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje + '\n')

            # print('En 4 meses'.center(72, '-'))
            escribir.writelines('En 4 meses'.center(72, '-') + '\n')
            for reg in listaFalta4:
                # print(reg)
                escribir.writelines(reg + '\n')

            mensaje = 'El monto total de la suma de las cuotas que se abonan en 4 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues4)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje + '\n')

            escribir.writelines('En 5 meses'.center(72, '-') + '\n')
            # print('En 5 meses'.center(72, '-'))
            for reg in listaFalta5:
                escribir.writelines(reg+ '\n')
                # print(reg)
            mensaje = 'El monto total de la suma de las cuotas que se abonan en 5 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues5)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje + '\n')

            escribir.writelines('En 6 meses'.center(72, '-') + '\n')
            # print('En 6 meses'.center(72, '-'))
            for reg in listaFalta6:
                escribir.writelines(reg + '\n')
                # print(reg)
            mensaje = 'El monto total de la suma de las cuotas que se abonan en 6 meses es: $' + formatoNumero(
                sumaCuotasVencenDespues6)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje + '\n')
        except Exception as e:
            print(f'Se produjo un error en MontosPagar: {e}')

        
if __name__ == '__main__':

    nombreArchivoTXT = 'Resumen completo.txt'
    salidaResumen = 'Resumen final.txt'
    # nvoPDF = iniciarPDF.abrirPDF(nombreArchivoPDF, nombreArchivoTXT)
    resumen = lector.pasarTXT(nombreArchivoTXT, salidaResumen)
    cuotas.formatoCuotas()
    cuotas.cuotasVencenAhora()
    cuotas.cuotasVencenDespues()
    cuotas.montosPagar()



