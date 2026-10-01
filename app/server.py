from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Проверяем, что запрос пришел именно на эндпоинт /health
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()

def run():
    server_address = ('', 8080)  # Слушает на всех интерфейсах, порт 8080
    httpd = HTTPServer(server_address, HealthCheckHandler)
    print("Сервер запущен на порту 8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()