import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from apps.posts.models import Posts
from .models import Perfil
from .form import UserForm


def usuario_index(request, user_id):
    mismo_usuario = False
    user = User.objects.filter(id=user_id).first()
    perfil = Perfil.objects.filter(user__id=user_id).first()
    form_user = UserForm(instance=user)
    profile_image = True if perfil.imagen_perfil else False
    posts = Posts.objects.filter(autor=perfil)
    if request.user.is_authenticated:
        if request.user.id == user_id:
            mismo_usuario = True
            if request.method == 'POST':
                password = request.POST['password']
                if user.check_password(password):
                    form_user = UserForm(request.POST, instance=user)
                    if form_user.is_valid():
                        form_user.save()
                        success_message = 'Los cambios fueron realizados correctamente!'
                        context = {
                            'form': form_user,
                            'perfil': perfil,
                            'success_message': success_message,
                            'profile_image': profile_image,
                            'posts': posts,
                            'mismo_usuario': mismo_usuario
                        }
                        return render(request, 'perfil.html', context)
                    else:
                        messages_json = form_user.errors.as_json(escape_html=True)
                        messages = json.loads(messages_json)['username'][0]['message']
                        context = {
                            'form': form_user,
                            'perfil': perfil,
                            'messages': messages,
                            'profile_image': profile_image,
                            'posts': posts,
                            'mismo_usuario': mismo_usuario
                        }
                        return render(request, 'perfil.html', context)
                else:
                    messages = 'La contraseña introducida no es correcta'
                    context = {
                        'form': form_user,
                        'perfil': perfil,
                        'messages': messages,
                        'profile_image': profile_image,
                        'posts': posts,
                        'mismo_usuario': mismo_usuario
                    }
                    return render(request, 'perfil.html', context)
            context = {
                'form': form_user, 
                'perfil': perfil,
                'profile_image': profile_image,
                'posts': posts,
                'mismo_usuario': mismo_usuario
            }
            return render(request, 'perfil.html', context)

    context = {
        'form': form_user, 
        'perfil': perfil,
        'profile_image': profile_image,
        'posts': posts,
        'mismo_usuario': mismo_usuario
    }
    return render(request, 'perfil.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('usuario')
    
    if request.method == "POST":
        try:
            profile_image = request.FILES['profile_image']
        except:
            profile_image = None
        username = request.POST['username']
        first_name = request.POST['name']
        last_name = request.POST['surname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        username_repeated = True if User.objects.filter(username=username).first() else False

        if not username_repeated:
            if pass1 == pass2:
                if len(pass1) >= 8:
                    new_user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=pass1,
                        first_name=first_name,
                        last_name=last_name
                    )
                    new_profile = Perfil.objects.create(
                        user=new_user,
                        imagen_perfil=profile_image,
                    )
                    return redirect("signin")
                
                return render(request, 'auth/signup.html', {'message': 'La contraseña debe ser mayor o igual a 8 caracteres.'})
            return render(request, 'auth/signup.html', {'message': 'Error: las contraseñas no coinciden.'})
        return render(request, 'auth/signup.html', {'message': 'Error: ya existe un usuario con ese username.'})

    return render(request, "auth/signup.html")


def signin(request):
    if request.user.is_authenticated:
        return redirect('usuario')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'auth/signin.html', {'message': 'Su correo y/o su contraseña son incorrectas.'})

    return render(request, "auth/signin.html", {})


def sign_out(request):
    logout(request)
    return redirect("/")


def cambiar_foto(request, perfil_id):
    try:
        profile_image = request.FILES['image']
    except:
        profile_image = None

    perfil = Perfil.objects.filter(id=perfil_id).first()
    if profile_image:
        perfil.imagen_perfil = profile_image
        perfil.save()
    return redirect('usuario_index', user_id=perfil.user.id)

