import socket
import threading
import time

def run_test_client(client_id):
    host = '127.0.0.1'
    port = 5555
    
    try:
        # Подключаемся к серверу
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        
        # Отправляем сообщение
        message = f"Привет, я клиент номер {client_id}!"
        client.send(message.encode('utf-8'))
        
        # Получаем эхо-ответ
        data = client.recv(1024)
        print(f"Клиент {client_id} получил ответ: {data.decode('utf-8')}")
        
        # Небольшая пауза, чтобы сервер успел зафиксировать все подключения
        time.sleep(1)
        client.close()
    except ConnectionRefusedError:
        print(f"Клиент {client_id} не смог подключиться. Сервер запущен?")

if __name__ == "__main__":
    print("Запускаем 3 одновременных клиента для проверки...")
    threads = []
    
    # Создаем 3 одновременных клиента
    for i in range(1, 4):
        thread = threading.Thread(target=run_test_client, args=(i,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    print("Тестирование завершено.")
