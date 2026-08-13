# ===== imports ======
import json

def save_wifi_credentials(ssid, password):
    # ===== data to be converted to JSON ======
    data = {
        "ssid": ssid,
        "password": password
    }

    # ===== convert to JSON string ======
    text = json.dumps(data)

    print(text)  # Output: {"ssid": "SHOS-Setup", "password": "gasnode123"}

    # ===== save to file ======
    with open("wifi_credentials.json", "w") as file:
        file.write(text)
