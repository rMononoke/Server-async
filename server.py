import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] Новое подключение: {address}")
    
    while True:
        try:
            # Получаем данные от клиента (до 1024 байт)
            data = client_socket.recv(1024)
            if not data:
                break # Если данных нет, клиент отключился
            
            message = data.decode('utf-8')
            print(f"[{address}] Получено: {message}")
            
            # Отправляем те же данные обратно (echo)
            client_socket.send(data)
        except ConnectionResetError:
            break
            
    print(f"[-] Отключение: {address}")
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 5555
    
    # Создаем TCP сокет
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    
    print(f"Сервер запущен на {host}:{port} и ожидает подключений...")
    
    while True:
        # Принимаем новое подключение
        client_socket, address = server.accept()
        
        # Создаем и запускаем новый поток для каждого клиента
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()
        
        # Показываем количество активных потоков (минус 1 главный поток сервера)
        print(f"[!] Активных клиентских потоков: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
