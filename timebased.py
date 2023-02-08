import websocket
import json
import time
import ssl
import sys

print("Benchmarking...")

websocket_url = sys.argv[2] or "ws://echo.websocket.events"
benchmark_time = int(sys.argv[1]) or 10
messages_sent = 0
messages_received = 0
message = {"test": "test message"}

ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
ws.settimeout(5)
ws.connect(websocket_url)

start = time.time()

while (time.time() - start) < benchmark_time:
    ws.send(json.dumps(message))
    messages_sent += 1
    ws.recv()
    messages_received += 1
ws.close()

end = time.time()

print(f"Sent {messages_sent} messages in {end-start:.2f} seconds")
print(f"Received {messages_received} messages in {end-start:.2f} seconds")
print(f"Average latency: {(end-start)/messages_received:.6f} seconds per message")
print("Finished benchmarking")
