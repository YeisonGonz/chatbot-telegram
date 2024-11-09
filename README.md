# ChatBot Telegram

### ¿En qué consiste el proyecto?

Estoy desarrollando un chatbot para Telegram que sea capaz de aprender de las conversaciones que se realicen en el grupo al que pertenezca y ofrecer una serie de comandos personalizables mediante la interfaz AIML.

### Tecnologías 

El proyecto está basado completamente en Python, usando principalmente dos bibliotecas:

- python-telegram-bot -> [Link de la página oficial](https://python-telegram-bot.org/)
- python-aiml -> [Link del repositorio](https://github.com/cdwfs/pyaiml)

### Aprendizaje 🤔

Aún no está implementado, pero el bot en un futuro será capaz de aprender de las conversaciones que se tengan en el grupo. Para que pueda aprender, es necesario que el bot **GUARDE TODOS LOS MENSAJES** del grupo. De este modo, podrá generar su propio dataset especializado en _vosotros_, los usuarios del grupo donde se encuentre el bot.

### Environment

Es necesario agregar al proyecto el archivo ```.env```. Aquí dejo un ejemplo:

```bash
TELEGRAM_BOT_TOKEN=token_del_bot
TELEGRAM_BOT_NAME=nombre_del_bot
```