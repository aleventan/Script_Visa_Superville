

listadoRegistrosCuotas = []
listadoRegistrosCompleto = []
listadoRegistrosUnPago = []
listadoUnPagoRenombrado = []
class variablesGlobales:
    entradanombreArchivoPDF = ''
    nombreArchivoPDF = ''
    nombreArchivoTXT = 'todojunto.txt'
    salidaResumen = ''

def formatoNumero(numeroFormatear):
    # Da formato para que cambie de lugar el punto y la coma. El resultado es de tipo String
    nvoNro = round(numeroFormatear, 2)
    nroFinal = "{:,}".format(nvoNro).replace(',', '~').replace('.', ',').replace('~', '.')
    return nroFinal

