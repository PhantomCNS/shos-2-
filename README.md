# SHOS-2

SHOS-2 is a modular smart home operating system built around ESP32 microcontrollers and MicroPython. The project is designed to monitor environmental conditions, detect dangerous gas levels, trigger alarms, and provide a simple interface for local or remote control.

The system is made of connected nodes, each responsible for a specific task. This modular structure keeps the project flexible and easy to extend with more sensors, devices, and automation features over time.

## Overview

The main goal of SHOS-2 is to create an affordable and expandable smart home platform that can:

- monitor air quality and temperature
- detect gas leaks and hazardous conditions
- react automatically with local alarms
- display status information on a local device
- communicate over Wi-Fi
- allow simple interaction through a phone or web interface

## System architecture

The project is divided into a few functional parts.

### Gas node

The gas node is the safety and sensing unit of the system. It reads environmental data and checks whether conditions become dangerous.

Typical hardware includes:

- ESP32
- DHT22 temperature and humidity sensor
- MQ-2 gas sensor
- buzzer
- relay
- switch

Responsibilities:

- read sensor values
- detect unsafe gas levels
- trigger alarms and local actions
- send data through the network
- support emergency behavior when risk is detected

### Display node

The display node acts as the local status interface for the system. It collects information from other nodes and presents it in a human-readable format.

Typical hardware includes:

- ESP32
- 16x2 LCD display

Responsibilities:

- collect node data
- show connection status
- display alarms and warnings
- present system information locally

### Web interface

A lightweight web layer is included to support a user-facing interface and easier interaction.

Responsibilities:

- expose information to the user
- support remote access
- provide a simple UI for monitoring and control

## Features

- ESP32-based modular smart home platform
- Wi-Fi connectivity
- local alarm handling
- gas leak detection
- sensor-based automation
- display-based status information
- web interface support
- extensible node-based architecture
- suitable for future development with additional smart devices

## Why this project exists

This project is intended to be a practical, flexible smart home and safety solution. It combines sensor monitoring, local reaction logic, and network connectivity in a way that can be adapted to different rooms, devices, or danger scenarios.

The gas detection capability makes it useful not only as a general smart home platform, but also as an environmental safety system with early warnings.

## Repository structure

- firmware/gas-node: gas sensing and control logic
- firmware/display-node: display and status presentation
- firmware/web: web frontend assets
- docs: architecture and project documentation
- README files: module-level notes and documentation

## Current status

The project is in an active modular development stage. The foundation is already present for:

- gas detection
- ESP32-based node communication
- local alerts
- display-based monitoring
- web interaction support

The design is intended to evolve as more features and sensors are added.

## Future improvements

Potential future work includes:

- expanding sensor coverage
- improving reliability and communication logic
- refining web control features
- adding more automation rules
- improving documentation and deployment steps
- adding more device nodes for different rooms or functions

## Summary

SHOS-2 is a smart home platform focused on modularity, safety, and expandability. It uses ESP32 devices and connected sensors to monitor the home environment, detect hazardous gas conditions, and provide useful feedback to the user through local display and network interfaces.

It is designed as a foundation for a more advanced smart home ecosystem, with room for additional sensors, controls, and automation features.

