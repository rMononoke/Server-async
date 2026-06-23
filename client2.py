import socket

def start_client():
    host = '127.0.0.1'
    port = 5555
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((host, port))
        print("Успешное подключение к серверу!")
        print("Вводи сообщения ниже. Для выхода напиши 'exit'.")
        
        while True:
            # Ждем ввод от пользователя
            message = input("\nТы: ")
            
            if message.lower() == 'exit':
                break
                
            if message.strip() == '':
                continue
            
            # Отправляем сообщение на сервер
            client.send(message.encode('utf-8'))
            
            # Получаем ответ от сервера
            data = client.recv(1024)
            print(f"Эхо от сервера: {data.decode('utf-8')}")
            
    except ConnectionRefusedError:
        print("Не удалось подключиться. Проверь, запущен ли сервер.")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
