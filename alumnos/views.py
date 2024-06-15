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
    print('Ingresando a createalumno...')
    print(request.method)
    if request.method == 'POST':
        print('Ingresando a POST...')
        print(request)
        print(request.POST['rut'])
        print(request.POST['nombrealumno'])
        _rut = request.POST['rut']
        _nombre = request.POST['nombrealumno']
        _aPaterno = request.POST['paterno']
        _aMaterno = request.POST['materno']
        _fechaNac = request.POST['fechaNac']
        _telefono = request.POST['telefono']
        _email = request.POST['email']
        _direccion = request.POST['direccion']
        _activo = 1
        alumno = Alumno.objects.create(
            rut=_rut,
            nombre=_nombre,
            apellido_paterno=_aPaterno,
            apellido_materno=_aMaterno,
            fecha_nacimiento=_fechaNac,
            telefono=_telefono,
            email=_email,
            direccion=_direccion,
            activo=_activo
        )
        alumno.save()
        return render(request, 'alumnos/alumnos_add.html')
    else:
        print('Ingresando a GET...')
        return render(request, 'alumnos/alumnos_add.html')
    
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
    print('Ingresando a alumnos_findEdit...')
    print(request.method)
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

       

