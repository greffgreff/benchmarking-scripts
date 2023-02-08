import websocket
import json
import time
import ssl
import sys

messages_to_send = int(sys.argv[1]) or 100
websocket_url = sys.argv[2] or "ws://echo.websocket.events"
message = {"test": "test message"}

ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
ws.settimeout(5)
ws.connect(websocket_url)

print(f"Benchmarking {websocket_url}...")

start = time.time()

messages_sent = messages_to_send
while messages_sent != 0:
    ws.send(json.dumps(message))
    ws.recv()
    messages_sent -= 1
ws.close()

end = time.time()

print(f"Sent {messages_to_send} messages in {end-start:.2f} seconds")
print(f"Average latency: {(end-start)/messages_to_send:.6f} seconds per message")
print("Finished benchmarking.")
