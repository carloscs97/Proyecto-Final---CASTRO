from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",inicio,name="Inicio"),
    path("addCurso/",agregarCurso, name ="addCurso"),
    path("addProfesores/",agregarProfesor, name="addProfesores"),
    path("addEntregables/",agregarEntregable, name="addEntregables" ),
    path("addEntregables/",agregarEntregable, name = "addEntregables"),
    path("buscarCamada/",busquedaCamada, name= "BuscarCamada"),
    path("resultados/",resultados, name= "ResultadosBusqueda"),
    path("login/", inicioSesion, name = "Login"),
    path("register/", registro, name = "Signup"),
    path("logout/", LogoutView.as_view(template_name = "AppCoder/logout.html"), name = "Logout"),
    path("editar/", editarUsuario, name = "EditarUsuario"),
    path("about/",about, name = "About"),

    #CRUD de profesores 
    path("listaProfes/", leerProfesores, name= "ProfesoresLista"),
    path("leerProfes/", leerProfesores, name= "ProfesoresLista"),
    path("crearProfes/", crearProfesores, name= "ProfesoresCrear"),
    path("eliminarProfes/<profeNombre>", eliminarProfesores, name= "ProfesoresEliminar"),
    path("editarProfes/<profeNombre>", editarProfesores, name= "ProfesoresEditar"),

    path("listaEntregables/", leerEntregable, name= "EntregablesLista"),
    path("leerEntregables/", leerEntregable, name= "EntregablesLista"),
    path("crearEntregables/", crearEntregable, name= "EntregablesCrear"),
    path("eliminarEntregables/<entregableNombre>", eliminarEntregables, name= "EntregablesEliminar"),
    path("editarEntregables/<entregableNombre>", editarEntregables, name= "EntregablesEditar"),


    #CRUD de cursos usando clases
    path("curso/list", ListaCurso.as_view(), name= "CursosLeer"),
    path("curso/<int:pk>", DetalleCurso.as_view(), name= "CursosDetalle"),
    path("curso/crear", CrearCurso.as_view(), name= "CursosCrear"),
    path("curso/editar/<int:pk>", ActualizarCurso.as_view(), name= "CursosEditar"),
    path("curso/borrar/<int:pk>", BorrarCurso.as_view(), name= "CursosBorrar"),
    
   

    path("agregarImagen/", agregarImagen, name ="Subir Avatar")

    ]
