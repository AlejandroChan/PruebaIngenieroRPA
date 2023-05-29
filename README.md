# PruebaIngenieroRPA

## Problema

Reto 2 (Python): Una empresa nos facilita semanalmente 9 boletas de pago en
formato .txt, el área de finanzas está solicitando realizar un consolidado de
todas las boletas para luego exportarlo en formato .pdf y enviarlo por correo
(use su cuenta personal).

## Para ejecutar la solución

### El código que es un .py que se ejecuta de la siguiente manera:
python3 eviar_consolidado.py

### Como requisitos para ejecutar el código se deben instalar las siguientes librerías:
* pandas
* glob
* os
* matplotlib
* smtplib

### Se deben cambiar las rutas de las siguientes variables:
* **data_path:** Ruta de boletas de ejemplo.
* **pdf_path :** Ruta destino del consolidado pdf.

## Notas Adicionales
1. Para enviar correo electrónico remitente debe ser una cuenta gmail.
2. Se debe ingresar usuario y contraseña en las variables ***sender*** y ***password***.
3. Se debe ingresar el correo destinatario en la variable ***destination***.
4. El password no es la contraseña de la cuenta gmail.
5. Para conseguir el password se deben seguir las indicaciones de la siguiente ruta: https://www.letscodemore.com/blog/smtplib-smtpauthenticationerror-username-and-password-not-accepted/








