import os

from datetime import datetime
from controllers.Content import saveMessageContent


class MessageManager:
    
    def __init__(self, kernel=None):
        self.kernel = kernel
    
    # Context is necessary because MessageHandle returned
    # Save all messages, are necessary for machine learning
    async def messageGlobal(self, update, context):
        message = update.message.text
        user = update.effective_user.username or update.effective_user.first_name
        date = datetime.now()
        chat_id = update.effective_chat.id
        chat_title = update.effective_chat.title or "Private Chat"
        chat_type = update.effective_chat.type
        
        try:
            saveMessageContent(message, user, date, chat_id, chat_title, chat_type)
        except Exception as e:
            print(f"Error saving message: {e}")
    
    
    async def messageBotHandler(self, update, context):
        bot_name = os.getenv('TELEGRAM_BOT_NAME')
        message = update.message.text
        aiml_message = message.replace(f'@{bot_name}', '').replace('/bot', '').strip()
        if aiml_message == '':
            aiml_message = 'HOLA'
        respuesta = self.kernel.respond(aiml_message)
        
        if respuesta:
            await update.message.reply_text(respuesta)
        else:
            await update.message.reply_text("No tengo una respuesta para eso.")
