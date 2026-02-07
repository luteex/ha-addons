import socket
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

HOST = "0.0.0.0"
PORT = 2000

def main():
    logging.info(f"Starting TCP server on {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        logging.info("Server listening...")

        while True:
            conn, addr = s.accept()
            logging.info(f"Connection from {addr}")
            with conn:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        logging.info(f"Connection closed by {addr}")
                        break
                    logging.info(f"Received from {addr}: {data!r}")

if __name__ == "__main__":
    main()
