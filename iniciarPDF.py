import PyPDF2
from os import remove
from variablesGlobales import *

class iniciarPDF:
    def __init__(self, pdf, salidaPDF):
        self._pdf = pdf
        self._salidaPDF = salidaPDF

    @property
    def pdf(self):
        return self.pdf

    @pdf.setter
    def pdf(self, pdf):
        self._pdf = pdf

    @property
    def salidaPDF(self):
        return self.salidaPDF

    @salidaPDF.setter
    def salidaPDF(self, salidaPDF):
        self._salidaPDF = salidaPDF

    @classmethod
    def abrirPDF(cls, pdf, salidaPDF):
        pdf_file = open(pdf, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        # Elimina el archivo para borrar lo anterior
        # if salidaPDF:
        #     remove(salidaPDF)
        open(salidaPDF, 'w+', encoding='utf8')
        # Recorre las hojas y lo manda al txt
        for x in range(0, number_of_pages):
            pageObj = read_pdf.getPage(x)
            texto = pageObj.extractText()
            with open(salidaPDF, 'a', encoding='utf8') as ObjPDF:
                ObjPDF.write(texto)
if __name__ == '__main__':
    nombreArchivoPDF = 'resumen_cuenta_visa_Jun_2021.pdf'
    nombreArchivoTXT = 'Resumen completo.txt'
    nvoPDF = iniciarPDF.abrirPDF(nombreArchivoPDF, nombreArchivoTXT)