# TapVinyl 

Welcome to the TapVinyl Project repository! This project is designed to enhance my music listening experience by combining the novelty of physical media with the convenience and immediate access of digital media.

## Table of Contents
- [Introduction](#introduction)
- [Hardware & Software Requirements](#hardware-&-software-requirements)
- [Future Improvements](#future-improvements)
- [Acknowledgments](#acknowledgments)

## Introduction
This project utilizes RFID (Radio-Frequency Identification) technology to read the id from RFID tags then depending on the action/album or playlist that id represents it will then send requests to the Spotify API to control my music playback, essentially making it a modern day jukebox/vinyl player.

## Hardware & Software Requirements
- RFID Reader (RC522)
- RFID Tags
- Microcontroller (Raspberry Pi Model 4)
- Jumper Wires
- Power Supply
- Python 3
- Required libraries (e.g., spotipy, MFRC522, RPi.GPIO, spidev )

## Future Improvements
One significant challenge I faced was connecting the Raspberry Pi to the Eduroam Wi-Fi network. Instead, I opted to use my phone as a hotspot for the Pi. This allows me to transfer playback to my laptop when I tap the cards, which means my laptop always needs to be on while I'm using it. While it’s not a major inconvenience, I eventually want to make the setup standalone so that it doesn't depend on my laptop being powered on. If I can figure out how to connect the Raspberry Pi to Eduroam, I plan to make it a Spotify Connect device. This way, I can transfer playback to the Pi and play audio through speakers connected to its AUX port.

## Acknowledgments
- Inspiration from various open-source RFID projects
	- in particular [https://github.com/talaexe/Spotify-RFID-Record-Player/blob/main/spotifyTest.py](https://github.com/talaexe/Spotify-RFID-Record-Player/blob/main/spotifyTest.py)>)


