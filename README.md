# 🎉 Birthday Wisher

Una aplicación en Python que envía automáticamente correos electrónicos de felicitaciones de cumpleaños basados en plantillas personalizadas.

## 🚀 Características

- **Envío automático** de correos en la fecha correspondiente.
- **Uso de plantillas personalizadas** para los mensajes.
- **Lectura de datos desde un archivo CSV** para gestionar cumpleaños.

## ⚙️ Configuración

Para que la aplicación funcione correctamente, debés configurar tu correo electrónico en `main.py`:

1. Reemplazá `my_email` con tu dirección de correo.
2. Generá una **contraseña de aplicación** en tu proveedor de correo y reemplazá `password`.
3. Asegurate de habilitar el acceso de aplicaciones menos seguras en la configuración de tu correo.

## 📋 Estructura del proyecto

```
birthday-wisher/
├── main.py                # Código principal
├── birthdays.csv          # Lista de cumpleaños
├── letter_templates/      # Plantillas de cartas de felicitación
│   ├── letter_1.txt
│   ├── letter_2.txt
│   ├── letter_3.txt
└── requirements.txt       # Dependencias necesarias
```

