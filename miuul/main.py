import base64
import hmac
import hashlib
import time
import struct
import requests
import json

# Bilgilerini gir
email = "gulveren211504041@gmail.com"
secret = email + "HENNGECHALLENGE004"
url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"

# TOTP üretme (RFC6238 + SHA-512)
def generate_totp(secret):
    key = secret.encode()
    timestep = int(time.time()) // 30
    msg = struct.pack(">Q", timestep)
    h = hmac.new(key, msg, hashlib.sha512).digest()
    o = h[-1] & 0x0F
    code = (struct.unpack(">I", h[o:o+4])[0] & 0x7FFFFFFF) % 10000000000
    return str(code).zfill(10)

# Authorization header
password = generate_totp(secret)
auth = base64.b64encode(f"{email}:{password}".encode()).decode()

# JSON payload
payload = {
    "github_url": "https://gist.github.com/gulveren1453/e6021bdca846d0f0f9c90cf42f3d5b71",
    "contact_email": email,
    "solution_language": "python"
}

headers = {
    "Authorization": f"Basic {auth}",
    "Content-Type": "application/json"
}

# POST isteği gönder
response = requests.post(url, headers=headers, data=json.dumps(payload))

print(f"Status Code: {response.status_code}")
print("Response Body:", response.text)



