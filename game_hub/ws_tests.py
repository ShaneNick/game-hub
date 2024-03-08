from django.test import TestCase
import websocket
import json

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        data = {"message": "Hello, World!"}
        ws.send(json.dumps(data))
        ws.close()
    run()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws_url = "ws://localhost:8000/ws/some_path/"  # Update with your actual WebSocket URL
    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
