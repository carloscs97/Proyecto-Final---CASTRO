Bienvenidos a mi código!

Con este código he creado mi primera página web utilizando DJANGO para entrega del proyecto final del curso de PYTHON.

Con el archivo manage.py lo utilizamos para correr el servidor local. Con el archivo db.sqlite3 se encuentran nuestras tablas con la información.

En la carpeta AppCoder/ encontramos los archivos de Python para que funcione nuestra App. 
Models.py -- Clases que utilizamos en la página. (Avatar, Cursos, Entregables y Profesores) 
Views.py -- Las funciones que utilizamos para que se muestren en cada vista. 
Url.py -- Las rutas que utilizamos que cambian según la vista que se encuentra. 
Forms.py -- Los formularios que hemos creado para que se registre la información de cada clase. 
Admin.py -- Los modelos creados para que se visualicen en la ruta de ADMIN.

Adicional hay una carpeta importante "Templates/AppCoder/": En esta se encuentran los HTML de cada vista.

Hay un archivo padre.html que se creó en base al código de una plantilla y los diferentes archivos HTML (Curso.html, entregables.html, about.html, inicio.html, profesores.html) donde con una herencia se trae la información de padre.html y se modifican según los BLOCK en el archivo de padre.html

En la carpeta "ProyectoCoder/" tenemos el archivo urls.html que utilizamos para agregar en la ruta del servidor un "AppCoder".
