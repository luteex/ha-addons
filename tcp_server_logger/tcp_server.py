import socket
import logging
import signal
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

HOST = "0.0.0.0"
PORT = 2000

running = True
server_socket = None

def shutdown_handler(signum, frame):
    global running
    logging.info("Graceful shutdown requested")
    running = False
    if server_socket:
        try:
            server_socket.close()
        except Exception:
            pass

def main():
    global server_socket

    logging.info(f"Starting TCP server on {HOST}:{PORT}")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    server_socket.settimeout(1.0)   # 👈 klíčový řádek

    logging.info("Server listening...")

    while running:
        try:
            conn, addr = server_socket.accept()
        except socket.timeout:
            continue
        except OSError:
            break

        logging.info(f"Connection from {addr}")
        with conn:
            conn.settimeout(1.0)
            while running:
                try:
                    data = conn.recv(4096)
                except socket.timeout:
                    continue
                if not data:
                    logging.info(f"Connection closed by {addr}")
                    break
                logging.info(f"Received from {addr}: {data!r}")

    logging.info("TCP server stopped cleanly")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, shutdown_handler)
    signal.signal(signal.SIGINT, shutdown_handler)
    main()
