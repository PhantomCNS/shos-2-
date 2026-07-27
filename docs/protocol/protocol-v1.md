# SHOS Communication Protocol

## Overview

This document defines the communication protocol between SHOS nodes.

---

## Communication

- Technology: Wi-Fi
- Protocol: Blynk
- Data Format: JSON

---

## Sender
- gas Node

---

## Reciever
- Display Node

---

## Message Fields

| Field | Type | Description |
| :---: | :--: | :---------: |
| node | string | Sender node |
| temperature | float | Temperature in C |
| Humidity | int | Humidity percentage |
| alarm | bool | Alarm Status |
| fan | bool | Exhuast fan status |

---

## Communication Rules

- Gas Node sends data every 2 seconds.
- If gas exceeds the threshold, send an alarm immediately.
- If Wi-Fi disconnects keep monitoring locally.
- Relay and buzzer must work even if comunication fails.