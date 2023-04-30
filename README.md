# Script para extracción de datos de resúmen de Visa Superville
## Aplicación para desglosar el resumen de la tarjeta de crédito Visa Superville.
### Contenido
- [Descripción](#descripcion)
- [Instalación](#instalacion)
- [Uso](#uso)
- [Licencia](#licencia)

### Descripción <a name="descripcion"></a>
#### Esta aplicación permite desglosar un resumen de la tarjeta de crédito Visa del banco Superville (Argentina). Al seguir las instrucciones, se generará un archivo .txt que mostrará:

- Movimientos del mes
- Transacciones en un pago
- Renombrado de registros de un pago
- Agrupación de registros de un pago
- Lista de cuotas que llegan en este resumen
- Lista de cuotas que vencen este mes y los próximos 6 meses
- Montos a pagar de cuotas en los próximos 6 meses

### Instalación <a name="instalacion"></a>
1. Clonar este repositorio en su computadora.
2. Instalar las dependencias utilizando ´pip install -r requirements.txt´ 
3. Ejecutar el archivo ´main.py´
4. Seguir las instrucciones que van a ir apareciendo por consola.

### Uso <a name="uso"></a>
Una vez instaladas las librerías necesarias, al ejecutar el archivo main.py, se pedirá que se escriba el nombre del pdf (sin la extensión) que se encuentra en el mismo directorio que la aplicación. Al ingresarlo, se desglosarán todos los consumos y posteriormente preguntará si se desea renombrar los consumos en un pago y luego si se desea agruparlos. Al terminar, se generará el archivo .txt con toda la información en el mismo directorio que la aplicación.

### Licencia <a name="licencia"></a>
Este proyecto está licenciado bajo la licencia Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).

#### ¿Qué significa esto?
Esta licencia permite a otros distribuir, remezclar y construir sobre tu trabajo, siempre y cuando se dé crédito al autor original y no se utilice con fines comerciales. Esto significa que retienes los derechos de autor de tu trabajo y puedes decidir cómo se utiliza. Al utilizar esta licencia, puedes asegurarte de que tu trabajo se comparta y se utilice de manera que esté alineada con tus valores.

#### Cómo utilizar este trabajo
Si deseas utilizar este trabajo para fines no comerciales, puedes hacerlo siempre y cuando des crédito al autor original. Si deseas utilizar este trabajo con fines comerciales, debes contactar al autor para obtener permiso.


