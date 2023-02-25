from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

#Vista para el About(Acerca de mi)
def about(request):


    return render(request, "AppCoder/about.html")


#Vista para Iniciar sesión
def inicioSesion(request):

    if request.method == "POST":
        form= AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user= authenticate(username= usuario, password = contraseña)
            
            if user:
                login(request, user)
                return render(request,"AppCoder/inicio.html", {"mensaje" :f"Bienvenido {user}"})
        else:
            return render(request,"AppCoder/inicio.html",{"mensaje": "Datos incorrectos."} )
    else:
        form = AuthenticationForm()

    return render (request, "AppCoder/login.html",{"formulario":form})

#Vista para registrarse
def registro(request):
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)

        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request,"AppCoder/inicio.html", {"mensaje":"Usuario creado."})
    else:
        form = UsuarioRegistro()
    return render(request,"AppCoder/registro.html",{"formulario": form}) 

#Vista para editar usuario solo al iniciar sesión.
@login_required
def editarUsuario(request):
    usuario = request.user

    if request.method == "POST":
        form=FormularioEditar(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppCoder/inicio.html")
    
    else:

        form =FormularioEditar(initial = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        })

    return render(request,"AppCoder/editarPerfil.html", {"formulario":form,"usuario":usuario})
    

#Vista página principal
def inicio(request):

    
    return render(request,"AppCoder/inicio.html")

#Vista para subir imagenes (Avatares)
@login_required
def agregarImagen(request):
    if request.method == "POST": 

        miFormulario= AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion= miFormulario.cleaned_data

            avatar= Avatar(user=informacion['user'], imagen=informacion['imagen'])
            avatar.save()

            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario=AvatarFormulario()
    
    return render(request, "AppCoder/agregarImg.html",{"form":miFormulario})


#Para agregar Cursos
@login_required
def agregarCurso(request):

    if request.method == "POST":    #despues de dar el botón enviar
            
            formulario1 = CursoFormulario(request.POST)

            if formulario1.is_valid():
                info = formulario1.cleaned_data

                curso = Curso(nombre=info["curso"],camada = info["camada"])
        
                curso.save()

                return render(request, "AppCoder/inicio.html")

    else:

            formulario1 = CursoFormulario()

    return render(request,"AppCoder/cursos.html",{"form1":formulario1})



@login_required
def agregarProfesor(request):

    if request.method == "POST":    #despues de dar el botón enviar
            
            formulario3 = ProfesorFormulario(request.POST)

            if formulario3.is_valid():
                info = formulario3.cleaned_data

                profe = Profesor(nombre=info["nombre"],apellido = info["apellido"], email = info["email"],profesion = info["profesion"])
        
                profe.save()

                return render(request, "AppCoder/inicio.html")

    else:

            formulario3 = ProfesorFormulario()

    return render(request,"AppCoder/profesores.html",{"form3":formulario3})

#para agregar entregables
@login_required
def agregarEntregable(request):

    if request.method == "POST":    #despues de dar el botón enviar
            
            formulario4 = EntregableFormulario(request.POST)

            if formulario4.is_valid():
                info = formulario4.cleaned_data

                entregable = Entregable(nombre=info["nombre"],fechaEntrega = info["fechaEntrega"])
        
                entregable.save()

                return render(request, "AppCoder/inicio.html")

    else:

            formulario4 = EntregableFormulario()

    return render(request,"AppCoder/entregables.html",{"form4":formulario4})

#Vista para buscar camada
@login_required
def busquedaCamada(request):


    return render(request, "AppCoder/inicio.html")
    
@login_required
def resultados(request):

    if request.GET["camada"]:

       camada = request.GET["camada"] 
       cursos = Curso.objects.filter(camada__iexact=camada)

       return render(request, "AppCoder/inicio.html",{"cursos": cursos, "camada":camada})
    
    else:

        respuesta = "No has enviado datos."


    return render(request, "AppCoder/inicio.html", {"resp1":respuesta})

@login_required
def crearProfesores(request):
    if request.method =="POST": 
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            profesor= Profesor(nombre=info["nombre"], apellido=info["apellido"],email=info["email"],profesion=info["profesion"])

            profesor.save()

            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario=ProfesorFormulario()
    return render(request, "AppCoder/profeFormulario.html", {"miFormulario":miFormulario})

@login_required
def leerProfesores(request):

    profesores= Profesor.objects.all()

    contexto= {"teachers": profesores}

    return render(request, "AppCoder/listaProfes.html", contexto)

@login_required
def eliminarProfesores(request,profeNombre):

    profesor = Profesor.objects.get(nombre=profeNombre)
    profesor.delete()

    profesores= Profesor.objects.all()

    contexto = {"teachers": profesores}

    return render(request, "AppCoder/listaProfes.html", contexto)

@login_required
def editarProfesores(request, profeNombre):

    profesor = Profesor.objects.get(nombre=profeNombre)

    if request.method == "POST":
            
            formulario3 = ProfesorFormulario(request.POST)

            if formulario3.is_valid():
                info = formulario3.cleaned_data

                profesor.nombre = info["nombre"]
                profesor.apellido = info["apellido"]
                profesor.email = info["email"]
                profesor.profesion = info["profesion"]
        
                profesor.save()

                return render(request, "AppCoder/inicio.html")

    else:

            formulario3 = ProfesorFormulario(initial={"nombre": profesor.nombre, "apellido": profesor.apellido,
            "email": profesor.email, "profesion": profesor.profesion})

    return render(request,"AppCoder/editarProfe.html",{"form3":formulario3, "nombre": profeNombre})

#vista para mostrar a los cursos usando clases
class ListaCurso(LoginRequiredMixin, ListView):
    model = Curso

class DetalleCurso(DetailView):
    model = Curso

class CrearCurso(CreateView):
    model = Curso
    success_url= "/AppCoder/curso/list"
    fields= ["nombre","camada"]

class ActualizarCurso(UpdateView):
    model = Curso
    success_url= "/AppCoder/curso/list"
    fields= ["nombre","camada"]

class BorrarCurso(DeleteView):
    model = Curso
    success_url= "/AppCoder/curso/list"


#vista para mostrar a los entregables
@login_required
def crearEntregable(request):
    if request.method =="POST": 
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            entregable= Entregable(nombre=info["nombre"], fechaEntrega=info["fechaEntrega"])

            entregable.save()

            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario=EntregableFormulario()
    return render(request, "AppCoder/entregableFormulario.html", {"miFormulario":miFormulario})

@login_required
def leerEntregable(request):

    entregables= Entregable.objects.all()

    contexto= {"deliverables": entregables}

    return render(request, "AppCoder/listaEntregables.html", contexto)

@login_required
def eliminarEntregables(request,entregableNombre):

    entregable = Entregable.objects.get(nombre=entregableNombre)
    entregable.delete()

    entregables= Entregable.objects.all()

    contexto = {"deliverables": entregables}

    return render(request, "AppCoder/listaEntregables.html", contexto)

@login_required
def editarEntregables(request, entregableNombre):

    entregable = Entregable.objects.get(nombre=entregableNombre)

    if request.method == "POST":
            
            formulario3 = EntregableFormulario(request.POST)

            if formulario3.is_valid():
                info = formulario3.cleaned_data

                entregable.nombre = info["nombre"]
                entregable.fechaEntrega = info["fechaEntrega"]
                
                entregable.save()

                return render(request, "AppCoder/inicio.html")

    else:

            formulario3 = EntregableFormulario(initial={"nombre": entregable.nombre, "fechaEntrega": entregable.fechaEntrega})

    return render(request,"AppCoder/editarEntregable.html",{"form3":formulario3, "nombre": entregableNombre})