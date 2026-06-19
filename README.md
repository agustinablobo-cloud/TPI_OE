# UNIVERISDAD TECNOLOGICA NACIONAL (UTN) --- TPI --- ORGANIZACION EMPRESARIAL --- 2026

Alumnas: Agustina Lobo & Chiara Aquino

Fecha de entrega: 19/06/2026

Titulo del trabajo: Trabajo Practico Integrador


# DESCRIPCIÓN DEL PROYECTO

VacacionesBot es un chatbot deasarrolado en python para automatizar el proceso de solicitud de vacaciones de los empleados de una organización.

El sistema permite:

Identificar al empleado mediante su numero de legajo.
Consultar los dias de vacaciones disponibles.
Aprobar o rechazar solicitudes segun sus dias disponibles.
Gestionar multiples conversaciones mediante una maquina de estados.
Consultar información almacenada en un archivo CSV que simula una base de datos.

# TECNOLOGIAS UTILIZADAS

Python 3
Telegram Bot API
Libreria python-telegram-bot
Archivo CSV como base de datos simulada

# ESTRUCTURA

Proyecto/
│
├── bot.py
├── codigo python.py
├── empleados.csv
├── README.md

# INSTALACIÓN

1. Clonar o descargar el proyecto
2. Instalar las dependencias:
pip install python-telegram-bot

# Ejecución

Desde la terminal ejecutar:
python bot.py

Una vez iniciado el programa, abrir Telegram y buscar @Dias_vacaciones_bot

Enviar: 
/start

Para comenzar la interacción

# FLUJO DE FUNCIONAMIENTO

1. El usuario inicia la conversación
2. Selecciona la opción SOLICITAR
3. Ingresa su numero de legajo
4. Ingresa la cantidad de dias que desea tomar de vacaciones
5. El sistema verifica la disponibilidad
6. La solicitud es aprobada o rechazada 

