import ast
import re
import PyPDF2
from os import remove
from variablesGlobales import *
import locale

locale.setlocale(locale.LC_NUMERIC, '')

class lector:


    def __init__(self, salidaPDF, txtSalida):
        self._salidaPDF = salidaPDF
        self._txtSalida = txtSalida

    sumaTotal = 0

    @property
    def salidaPDF(self):
       return self.salidaPDF

    @salidaPDF.setter
    def salidaPDF(self, salidaPDF):
        self._salidaPDF = salidaPDF

    @property
    def txtSalida(self):
        return self.txtSalida

    @txtSalida.setter
    def txtSalida(self, txtSalida):
        self._txtSalida = txtSalida

    marca = 0

    def pasarTXT():
        try:
            ListaRegistros = []
            lineafinal = ''
            with open(variablesGlobales.nombreArchivoTXT, 'r', encoding='utf8') as ObjFichero:

                it = (linea for i, linea in enumerate(ObjFichero) if i >= 0)
                # Formato a cada registro
                for linea in it:

                    formAsterisco = re.compile(r'\d\d\d\d\d\d\*')
                    mo = formAsterisco.search(linea)
                    if mo:
                    # Acá tendria que hacer unir las dos lineas y una vez unidas todas las lineas, separar e imprimir
                        lineafinal = lineafinal + linea
                if lineafinal:
                    ListaRegi = re.split('\d\d\d\d\d\d\*', lineafinal)
                    for reg in ListaRegi:
                        ListaRegistros.append(reg[:76])


                    escribir = open(variablesGlobales.salidaResumen, 'w', encoding='utf8')
                    cabecera = ' MOVIMIENTOS DE ESTE MES '
                    # print('*'.center(72, '*'))
                    # print(cabecera.center(72, '*'))
                    # print('*'.center(72, '*'))
                    escribir.writelines('*'.center(72, '*') + '\n')
                    escribir.writelines(cabecera.center(72, '*') + '\n')
                    escribir.writelines('*'.center(72, '*') + '\n')
                    # Elimina el primer registro que no sirve
                    ListaRegistros.pop(0)
                    for registro in ListaRegistros:
                        # print(registro)
                        registroForma = registro[4:76]
                        listadoRegistrosCompleto.append(registroForma)
                        # Arma un listado con las cuotas
                        if registroForma[29:34] == 'Cuota':
                            listadoRegistrosCuotas.append(registroForma)
                        else:
                            listadoRegistrosUnPago.append(registroForma)
                        #Escribe cada registro dentro del txt
                        escribir.writelines(registroForma + '\n')
                    if listadoRegistrosCuotas:
                        pass
                    else:
                        # print('No se registraron cuotas')
                        escribir.writelines('No se registraron cuotas')
                    if listadoRegistrosUnPago:
                        pass
                    else:
                        # print('No se registraron pagos en un pago')
                        escribir.writelines('No se registraron pagos en un pago')
                    lector.sumaTotal()
                    mensaje = 'El total de la tarjeta es: ' + '{:>45}'.format('$'+lector.sumaTotales)
                    # print('\n' + mensaje)
                    escribir.writelines('\n' + mensaje + '\n')
                    lector.marca = 1
                    escribir.close()
                else:
                    pass

        except Exception as e:
            print(e)
            escribir.writelines(e)

    def sumaTotal():
        try:
            sumaTotal = 0
            # Recorre la lista completa para tomar el total
            for registro in listadoRegistrosCompleto:
                # Dejo que se muestr un listado de todos los pagos
                print(registro)
                # Le saca los espacios en blanco al monto
                mo = registro[60:].lstrip()
                # Lo convierte a float
                nvoMonto = locale.atof(mo)
                sumaTotal = sumaTotal + nvoMonto
            lector.sumaTotales = formatoNumero(sumaTotal)
        except Exception as e:
            print(f'Se produjo un error en sumaTotal: {e}')


if __name__ == '__main__':
    variablesGlobales.nombreArchivoPDF = 'resumen_cuenta_visa_May_2021.pdf'
    variablesGlobales.nombreArchivoTXT = 'Resumen completo.txt'
    variablesGlobales.salidaResumen = 'Resumen final.txt'
    # nvoPDF = iniciarPDF.abrirPDF(nombreArchivoPDF, nombreArchivoTXT)
    lector.pasarTXT()
    # lector.sumaTotal()

    #print(listadoRegistrosCuotas)
