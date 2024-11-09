import json
import os

def saveMessageContent(message, user, date, chat_id, chat_title, chat_type):
    data = {
        'message': message,
        'user': user,
        'date': date.isoformat(),
        'chat_id': chat_id,
        'chat_title': chat_title,
        'chat_type': chat_type
    }
    
    with open('data/message_content.jsonl', 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        file.write('\n')