import locale
from lector import *
from main import *
from variablesGlobales import *

class unPago(lector):
    def __init__(self, unPago):
        self._unPago = unPago

    sumaUnPago = 0

    @property
    def unPago(self):
        return self.unPago

    @unPago.setter
    def unPago(self, unPago):
        self._unPago = unPago

    locale.setlocale(locale.LC_ALL, '')

    def formatoUnPago():
        try:
            escribir = open(variablesGlobales.salidaResumen, 'a', encoding='utf8')
            cabecera = ' LISTADO TRANSACCIONES EN UN PAGO '
            # print('*'.center(72, '*'))
            # print(cabecera.center(72, '*'))
            # print('*'.center(72, '*'))
            escribir.writelines('*'.center(72, '*') + '\n')
            escribir.writelines(cabecera.center(72, '*') + '\n')
            escribir.writelines('*'.center(72, '*') + '\n')

            sumaUnPago = 0
            for separoUnPago in listadoRegistrosUnPago:
                # print(separoUnPago)
                escribir.writelines(separoUnPago + '\n')
                monto = separoUnPago[62:].lstrip()
                # Llama a la clase locale para poder convertir a float el string de ese registro

                nvoMonto = locale.atof(monto)
                sumaUnPago = sumaUnPago + nvoMonto
                #print(sumaUnPago)
            unPago.sumaUnPago = sumaUnPago
            mensaje = 'El monto total de la suma de cosas en un pago de este mes es: $' + formatoNumero(sumaUnPago)
            # print('\n' + mensaje)
            escribir.writelines('\n' + mensaje + '\n')
            escribir.close()
        except Exception as e:
            print(f'Se produjo un error en formatoUnPago: {e}')

    def renombrar():
        try:
            escribir = open(variablesGlobales.salidaResumen, 'a', encoding='utf8')
            cabecera = ' RENOMBRADO DE REGISTROS '
            # print(cabecera.center(72, '*'))
            escribir.writelines(cabecera.center(72, '*') + '\n')
            marca = 'N'
            marquita = 'N'
            while True:
                modificarSON = input('Desea renombrar un pago (S/N)? ')

                if modificarSON == 'S':
                    nmbResumen = input('Ingresar el valor como aparece en el resumen (todo con mayusculas y respetando los caracteres que figuran en el reumen): ')
                    nmbNuevo = input('Ingresar el nuevo nombre: ')
                    for separoUnPago in listadoRegistrosUnPago:
                        nombreEnResumen = '{:<21}'.format(nmbResumen)
                        nombreModificado = '{:<21}'.format(nmbNuevo)
                        if nombreEnResumen == separoUnPago[:21]:
                            nvoReg = nombreModificado + separoUnPago[21:]
                            listadoRegistrosUnPago.remove(separoUnPago)
                            listadoRegistrosUnPago.append(nvoReg)
                            marquita = 'S'
                    if marquita == 'S':
                        print('Registro modificado')
                        marquita = 'N'
                    else:
                        print('No existe tal registro. Por favor ingresar el nombre correctamente')
                    # for registros in listadoRegistrosUnPago:
                    #     print(registros)
                    #     escribir.writelines(registros + '\n')
                    marca = 'S'
                elif modificarSON == 'N':
                    if marca == 'S':
                        for registros in listadoRegistrosUnPago:
                            # print(registros)
                            escribir.writelines(registros + '\n')
                    break
                else:
                    print('Por favor ingresar un valor correcto')

            escribir.close()
        except Exception as e:
            print(f'Se produjo un error en Renombrar: {e}')
    def agrupar():
        try:
            escribir = open(variablesGlobales.salidaResumen, 'a', encoding='utf8')
            cabecera = ' AGRUPAR REGISTROS '
            # print(cabecera.center(72, '*'))
            escribir.writelines(cabecera.center(72, '*') + '\n')

            while True:
                agrupar = input('Desea agrupar los mismos registros y que se muestre el total de los mismos (S/N)? ')
                if agrupar == 'S':

                    for separoUnPago in listadoRegistrosUnPago:
                        buscarNombre = separoUnPago[:21]
                        sumaUnPago = 0
                        for buscarReg in listadoRegistrosUnPago:
                            if buscarNombre == buscarReg[:21]:
                                locale.setlocale(locale.LC_ALL, '')
                                monto = buscarReg[62:].lstrip()
                                nvoMonto = locale.atof(monto)
                                sumaUnPago = sumaUnPago + nvoMonto

                        sumaUnPago = '{:.2f}'.format(sumaUnPago)
                        nvoReg = f'{buscarNombre} {sumaUnPago:>51}'
                        if nvoReg not in listadoUnPagoRenombrado:
                            listadoUnPagoRenombrado.append(nvoReg)

                    for registros in listadoUnPagoRenombrado:
                        # print(registros)
                        escribir.writelines(registros + '\n')
                    print('Se agruparon los registros')
                    break
                elif agrupar == 'N':
                    print('No se agruparan los registros')
                    break
                else:
                    print('Por favor ingresar un valor correcto')
            escribir.close()
        except Exception as e:
            print(f'Se produjo un error en Agrupar: {e}')

if __name__ == '__main__':
    # nombreArchivoTXT =
    # salidaResumen = 'Resumen final.txt'
    # nvoPDF = iniciarPDF.abrirPDF(nombreArchivoPDF, nombreArchivoTXT)
    lector.pasarTXT()
    unPago.formatoUnPago()
    # unPago.renombrar()
    # unPago.agrupar()
