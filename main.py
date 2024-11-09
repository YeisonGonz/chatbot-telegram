import os
import aiml


from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, filters, Application
from controllers.BotCommands import BotCommands
from controllers.MessageManager import MessageManager
from controllers.kernelAIML import load_aiml_kernel

kernel = aiml.Kernel()
messageManager = MessageManager(kernel)
botcommands = BotCommands()
load_dotenv()
load_aiml_kernel(kernel, 'brain/base_aiml.aiml')

async def error_handler(update, context):
    print(f'Error: {context.error}')

def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError("No se encontró el token del bot. Asegúrate de configurar la variable de entorno TELEGRAM_BOT_TOKEN.")

    application = Application.builder().token(token).build()


    application.add_handler(CommandHandler("info", botcommands.info))
    application.add_handler(CommandHandler("bot", messageManager.messageBotHandler))  # Para el comando /bot
    application.add_handler(MessageHandler(filters.TEXT & filters.Entity("mention"), messageManager.messageBotHandler))  # Para menciones
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messageManager.messageGlobal))
    
    application.add_error_handler(error_handler)

    print("Bot iniciado. Esperando mensajes...")
    application.run_polling()

if __name__ == '__main__':
    main()
