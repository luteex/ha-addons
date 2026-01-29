import snap7
from snap7.util import *
from snap7.snap7types import *

PLC_IP = "192.168.1.120"
RACK = 0
SLOT = 2   # u S7-300 je typicky 2

client = snap7.client.Client()

try:
    print(f"Connecting to PLC {PLC_IP} (rack={RACK}, slot={SLOT})...")
    client.connect(PLC_IP, RACK, SLOT)

    if client.get_connected():
        print("✅ Connection OK – PLC is reachable")
    else:
        print("❌ Not connected")

except Exception as e:
    print("❌ Connection failed:")
    print(e)

finally:
    client.disconnect()
