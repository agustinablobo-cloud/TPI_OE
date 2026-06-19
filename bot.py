from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8651896545:AAH7l4kK44g3TunqmPW9WpMHbcH1aHiy4hc"             #Token del bot

import csv

def cargar_empleados():
    empleados = {}
    with open('empleados.csv', mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            legajo = fila['legajo']
            empleados[legajo] = {
                'nombre': fila['nombre'],
                'dias': int(fila['dias'])
            }
    return empleados

# Cargar BD al iniciar el bot
empleados = cargar_empleados()

# Guardamos el estado de cada usuario
user_state = {}
formulario = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_state[user_id] = "inicio"
    formulario[user_id] = {}
    await update.message.reply_text("🤖 VacacionesBot 🤖 \n Sistema de Gestión de Solicitudes de Vacaciones ✈️ \n Departamento de Recursos Humanos 💼\n\n ¡Hola! 👋 \n\n Ingrese SOLICITAR para pedir días de vacaciones 📩 \n\n Ingrese SALIR para terminar 🚪🏃🏻‍♀️")

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    texto = update.message.text.lower()

    # Si no tiene estado, lo mandamos a inicio
    if user_id not in user_state:
        user_state[user_id] = "inicio"
        formulario[user_id] = {}

    estado = user_state[user_id]

    if estado == "inicio":
        if texto == "solicitar":
            user_state[user_id] = "legajo"
            await update.message.reply_text("Por favor, ingrese su número de legajo 🗂️:")
        elif texto == "salir":
            await update.message.reply_text("👋 Gracias por usar el sistema 👋")
            user_state[user_id] = "inicio"
        else:
            await update.message.reply_text("🚫 Ingrese una opción válida: SOLICITAR o SALIR 🚫")

    elif estado == "legajo":
        legajo = update.message.text
        if legajo in empleados:
            formulario[user_id]["legajo"] = legajo
            nombre = empleados[legajo]["nombre"]
            await update.message.reply_text(f"¡Hola, {nombre} 👋😊!")
            user_state[user_id] = "dias"
            await update.message.reply_text("¿Cuántos días de vacaciones desea solicitar? 📅✍🏻")
        else:
            await update.message.reply_text(" ERROR ❗. Legajo no encontrado 🤔 Ingreselo nuevamente 🔍")

    elif estado == "dias":
        try:
            dias = int(update.message.text)
            formulario[user_id]["dias"] = dias
            user_state[user_id] = "verificar"

            legajo = formulario[user_id]["legajo"]
            solicitud_dias = formulario[user_id]["dias"]
            dias_disponibles = empleados[legajo]["dias"]

            if solicitud_dias <= dias_disponibles:
                empleados[legajo]["dias"] -= solicitud_dias
                resto_dias = empleados[legajo]["dias"]
                await update.message.reply_text(f"Estado de solicitud APROBADA ✅. Le quedan {resto_dias} días de vacaciones")
            else:
                await update.message.reply_text(f"Estado de solicitud RECHAZADA ❌. Solo le quedan {dias_disponibles} días de vacaciones disponibles")

            user_state[user_id] = "inicio"
            formulario[user_id] = {}
            await update.message.reply_text("Escribí SOLICITAR para hacer otra solicitud 📩 o SALIR 🚪🏃🏻‍♀️")

        except ValueError:
            await update.message.reply_text("ERROR ❗. Ingrese solo números 🔢")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))
app.run_polling()
