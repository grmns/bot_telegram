from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from telethon import TelegramClient
import asyncio
from .forms import RegistroForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Tu API ID, API Hash y número de teléfono
api_id = 22818872  # Coloca tu API ID
api_hash = '9159be536fd5370b18fe3c20d591ddc3'  # Coloca tu API Hash
phone_number = '+51906741646'

# Crea el cliente de Telethon una vez y reutilízalo
client = TelegramClient('session_name', api_id, api_hash)
loop = asyncio.get_event_loop()

async def start_client():
    if not client.is_connected():
        await client.start(phone=phone_number)

# Vista principal
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')

# Hacer la vista asíncrona
def send_command(request):
    if request.method == "POST":
        dni = request.POST.get('dni')  # Capturar el DNI ingresado por el usuario
        command = f'/dni {dni}'  # Formar el comando con el DNI
        bot_username = '@ShizukaData_bot'

        try:
            # Reutilizamos el ciclo de eventos existente en lugar de crear uno nuevo
            response, profile_image = loop.run_until_complete(handle_telegram_command(command, bot_username))
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

        # Asegurarse de que los datos se actualicen correctamente para cada solicitud
        context = {
            'bot_response': response,
            'profile_image': profile_image  # Ruta de la imagen
        }

        # Renderizar la respuesta en la nueva página de resultados
        return render(request, 'resultados.html', context)

    return HttpResponse("Método no permitido", status=405)

# Función asíncrona para manejar la lógica del bot de Telegram
async def handle_telegram_command(command, bot_username):
    await start_client()

    # Enviar el comando al bot
    sent_message = await client.send_message(bot_username, command)
    sent_message_id = sent_message.id  # Guardar el ID del mensaje enviado

    # Esperar la respuesta
    retries = 0
    response = None
    profile_image = None

    while retries < 5:
        await asyncio.sleep(3)  # Esperar de forma asíncrona

        # Obtener solo los mensajes nuevos (posteriores al mensaje enviado)
        messages = await client.get_messages(bot_username, min_id=sent_message_id)

        # Filtrar para encontrar la respuesta del bot
        for msg in messages:
            if msg.message and not msg.message.startswith('/dni'):
                response = msg.message
                if msg.media:
                    profile_image = await client.download_media(msg, file='media/profile_image.jpg')
                break

        if response:
            break  # Salir del bucle si ya se obtuvo respuesta

        retries += 1

    if not response:
        response = "No se recibió respuesta del bot."

    # Devolver los valores para asegurarse de que sean actualizados
    return response, profile_image

# Vista para el registro de nuevos usuarios
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario en la base de datos
            login(request, user)  # Loguear automáticamente al usuario registrado
            return redirect('home')  # Redirigir a la página principal
    else:
        form = RegistroForm()

    # Renderizar el formulario de registro
    return render(request, 'registration/register.html', {'form': form})