import webview
import threading
import os

def start_flask():
    os.system("python app.py")  # Runs your Flask app

if __name__ == "__main__":
    threading.Thread(target=start_flask).start()
    import time
    time.sleep(2)  # Wait for server to start
    webview.create_window("My Flask App", "http://127.0.0.1:5000 ")
    webview.start()
