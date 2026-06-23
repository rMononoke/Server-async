import socket
import sys

def start_client(host='127.0.0.1', port=5555):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((host, port))
        print("Успешное подключение к серверу!")
        print("Вводи сообщения ниже. Для отключения напиши 'stop'.")
        
        while True:
            message = input("\nТвое сообщение: ").strip()
            
            # Защита от отправки пустых строк
            if not message:
                continue
                
            # Проверка на стоп-слово (используем lower() на случай ввода 'STOP' или 'Stop')
            if message.lower() == 'stop':
                print("Команда принята. Отключаемся от сервера...")
                break
                
            # Отправка сообщения
            client.sendall(message.encode('utf-8'))
            
            # Ожидание эхо-ответа
            data = client.recv(1024)
            if not data:
                print("Сервер разорвал соединение.")
                break
                
            print(f"Эхо-ответ сервера: {data.decode('utf-8')}")
            
    except ConnectionRefusedError:
        print("Ошибка: Сервер недоступен. Проверь, запущен ли он.")
    except KeyboardInterrupt:
        print("\n[!] Принудительное завершение работы (Ctrl+C).")
    finally:
        client.close()
        sys.exit()

if __name__ == "__main__":
    start_client()
