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
    
    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
        context={'alumno':alumno}
        if alumno:
            return render(request, 'alumnos/alumnos_edit.html', context)

        else:  
            context={'mensaje: '"Error rut no existe..."}
            return render(request, 'alumnos/alumnos_list.html', context)



def alumnosUpdate (request):
    if request.method == "POST":
            _rut = request.POST["rut"]
            _nombre = request.POST["nombrealumno"]
            _aPaterno = request.POST['paterno']
            _aMaterno = request.POST['materno']
            _fechaNac = request.POST['fechaNac']
            _telefono = request.POST['telefono']
            _email = request.POST['email']
            _direccion = request.POST['direccion']
            _activo = 1

            alumno=Alumno()
            alumno.nombre=_nombre
            alumno.rut=_rut
            alumno.apellido_paterno=_aPaterno
            alumno.apellido_materno=_aMaterno
            alumno.fecha_nacimiento=_fechaNac
            alumno.telefono=_telefono
            alumno.email=_email
            alumno.direccion=_direccion
            alumno.activo=1
            alumno.save()
            context={"mensaje": "Ok, datos actualizados", 'alumno':alumno}
            return render(request, 'alumnos/alumnos_edit.html', context)
    else:
        alumnos=Alumno.objects.all()
        context={'mensaje':'Error: Rut no existe...'}
        return render(request, 'alumnos/alumnos_edit.html', context)
        
