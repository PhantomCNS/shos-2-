# SHOS
shos is a modular smart home platform based on ESP32 and Micropython

## Nodes
### Gas Node
#### Connected devices
- ESP32
- DHT22
- MQ-2
- Buzzer
- Relay
- Switch
#### Responsibilities
- Read Sensors
- Detect dangerous gas level
- Take immediate action
- Send data via Wi-Fi
- Trigger local alarm if necessary

### Display Node
#### Connected devices
- ESP32
- LCD 16*2

#### Responsibilities
- Collect data from other nodes
- display data
- display connection status
- show alarms