

class BotCommands():
    
    async def info(self, update, context):
        info = f"""
        Hola, yo soy un Bot que dedica a recopilar informacion de este grupo, para poder aprender de vuestro comportamineto y ofreceros experiencias personalizadas en un futuro.
        """
        await update.message.reply_text(info)
        