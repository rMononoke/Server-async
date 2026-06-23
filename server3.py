import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] Подключение установлено: {address}")
    
    try:
        while True:
            # Получаем данные от клиента
            data = client_socket.recv(1024)
            
            # Если данных нет (клиент разорвал соединение), выходим из цикла
            if not data:
                break
            
            message = data.decode('utf-8')
            print(f"[{address[0]}:{address[1]}] Сообщение: {message}")
            
            # Эхо-ответ (sendall надежнее обычного send)
            client_socket.sendall(data)
            
    except ConnectionResetError:
        print(f"[!] Соединение с {address} было разорвано.")
    except Exception as e:
        print(f"[!] Ошибка при работе с {address}: {e}")
    finally:
        # Этот блок выполнится в любом случае (даже при ошибке)
        print(f"[-] Отключение клиента: {address}")
        client_socket.close()

def start_server(host='127.0.0.1', port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Позволяет сразу переиспользовать порт после перезапуска сервера
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind((host, port))
    server.listen()
    
    print(f"Сервер запущен и слушает {host}:{port}...")
    
    try:
        while True:
            client_socket, address = server.accept()
            
            # Создаем поток для клиента
            thread = threading.Thread(target=handle_client, args=(client_socket, address))
            # Делаем поток демоном, чтобы он умирал вместе с сервером
            thread.daemon = True 
            thread.start()
            
    except KeyboardInterrupt:
        print("\n[!] Принудительная остановка сервера (Ctrl+C).")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
