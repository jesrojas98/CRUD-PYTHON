from django.shortcuts import render

from .models import Alumno
 # Create your views here.

def listar(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/index.html', context)


def alumnosAdd(request):
    if request.method is not "POST":
        alumnos=Alumno.objects.all()
        context={"alumnos":alumnos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        obj=Alumno.objects.create(rut=rut,
                                  nombre=nombre,
                                  apellido_paterno=aPaterno,
                                  apellido_materno=aMaterno,
                                  fecha_nacimiento=fechaNac,
                                  telefono=telefono,
                                  email=email,
                                  direccion=direccion,
                                  activo=1)
        
        obj.save()
        context={'mensaje':"ok, Datos Guardados..."}
        return render(request, 'alumnos/alumnos_add.html', context)
    

def alumnos_del(request,pk):
    context={}
    try:
        alumno=Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje="Bien, datos elimindados..."
        alumnos= Alumno.objects.all()
        context={'alumnos':alumnos, 'mensaje':mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        alumnos = Alumno.objects.all()
        context={'alumnos':alumnos, 'mensaje':mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    
def alumnos_findEdit(request,pk):
    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
       
        context={'alumno':alumno}
        if alumno:
            return render(request, 'alumnos/alumnos_edit.html', context)
        else:
            context={'mensaje':'Error: Rut no existe...'}
            return render(request, 'alumnos/alumnos_edit.html', context)
        
def alumnosUpdate(request):
        if request.method=="POST":
            rut=request.POST["rut"]
            nombre=request.POST["nombre"]
            aPaterno=request.POST["paterno"]
            aMaterno=request.POST["materno"]
            fechaNac=request.POST["fechaNac"]
            telefono=request.POST["telefono"]
            email=request.POST["email"]
            direccion=request.POST["direccion"]
            activo="1"

            alumno=Alumno()
            alumno.rut=rut
            alumno.nombre=nombre
            alumno.apellido_paterno=aPaterno
            alumno.apellido_materno=aMaterno
            alumno.fecha_nacimiento=fechaNac
            alumno.telefono=telefono
            alumno.email=email
            alumno.direccion=direccion
            alumno.activo=1
            alumno.save()
            context={"mensaje": "Ok, datos actualizados", 'alumno':alumno}
            return render(request, 'alumnos/alumnos_edit.html', context)
        else:
            alumnos=Alumno.objects.all()
            context={'alumnos':alumnos}
            return render(request, 'alumnos/alumnos_list.html', context)

       

