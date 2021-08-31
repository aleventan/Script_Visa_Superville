from iniciarPDF import *
import PyPDF2
from os import remove
from lector import *
from cuotas import *
from unPago import *
from variablesGlobales import *

if __name__ == '__main__':
    print(''' 
Bienvenidos
En esta aplicación podrán renombrar transacciones de un pago y también podrán agruparlas.
Además, podrán ver las cuotas que vencieron el mes corriente, así como también las que 
vencerán en los meses venideros.
Todo esto se va a guardar en un archivo txt ubicado en la misma carpeta donde se encuentra el resumen.
IMPORTANTE: El resúmen tiene que estar en formato .pdf y ubicado en el mismo directorio donde se 
encuentra esta aplicación.
    ''')
    variablesGlobales.entradanombreArchivoPDF = input('Por favor ingresar el nombre del archivo del resumen EXACTAMENTE igual a como está '
                             'guardado en la carpeta (NO AGREGAR LA EXTENSIÓN .pdf):')
    entradanombreArchivoPDF = variablesGlobales.entradanombreArchivoPDF
    variablesGlobales.nombreArchivoPDF = entradanombreArchivoPDF + '.pdf'
    variablesGlobales.salidaResumen = entradanombreArchivoPDF + '.txt'
    # nombreArchivoTXT = entradanombreArchivoPDF + '.txt'
    nvoPDF = iniciarPDF.abrirPDF(variablesGlobales.nombreArchivoPDF, variablesGlobales.nombreArchivoTXT)
    lector.pasarTXT()
    # Si encuentra algún registro sigue con el programa, sino lo corta
    if lector.marca == 1:
        unPago.formatoUnPago()
        unPago.renombrar()
        unPago.agrupar()
        cuotas.formatoCuotas()
        cuotas.cuotasVencenAhora()
        cuotas.cuotasVencenDespues()
        cuotas.montosPagar()
        print('\n')
        print(f'Se terminó de generar el archivo {variablesGlobales.salidaResumen}')
    else:
        print('No se ha podido generar el informe ya que el formato del resumen es diferente.')
