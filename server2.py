import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] Подключился новый клиент: {address}")
    
    while True:
        try:
            # Ожидаем сообщение от клиента
            data = client_socket.recv(1024)
            if not data:
                break
            
            message = data.decode('utf-8')
            print(f"[Сообщение от {address}]: {message}")
            
            # Отправляем эхо-ответ клиенту
            client_socket.send(data)
        except ConnectionResetError:
            break
            
    print(f"[-] Клиент отключился: {address}")
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 5555
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    
    print(f"Сервер запущен и слушает порт {port}...")
    
    while True:
        client_socket, address = server.accept()
        # Запускаем отдельный поток для каждого нового клиента
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()
