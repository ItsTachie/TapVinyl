# 🎵 TapVinyl

Welcome to the **TapVinyl** project!
This project enhances the music listening experience by blending the **novelty of physical media** with the **convenience of digital streaming**.

With TapVinyl, you can use RFID cards to play your favorite Spotify albums or playlists turning your Raspberry Pi into a modern-day jukebox/vinyl player.

---

## 🎶 Introduction

TapVinyl uses RFID (Radio-Frequency Identification) technology to read the ID from RFID tags.
Each tag corresponds to a specific **Spotify album or playlist**.
When a tag is scanned, the Raspberry Pi sends commands to the Spotify Web API to control playback, letting you physically “tap” into your music collection.

---

## 🔗 Live Demo

👉 [Demo Video](https://youtu.be/yIFws0wX-48)

---

## 🧰 Hardware & Software Requirements

### Hardware:
* RFID Reader: **RC522**
* RFID Tags (one per album/playlist you want to map)
* Microcontroller: **Raspberry Pi 4**
* Jumper Wires
* Power Supply
* Audio output device (optional, for standalone playback)

### Software:
* Python 3
* Required Python libraries:

  * `spotipy`
  * `MFRC522`
  * `RPi.GPIO`
  * `spidev`
* A [Spotify Developer Account](https://developer.spotify.com/dashboard) and registered app for API credentials

---

## 🔮 Future Improvements
* Make the Pi a **Spotify Connect device**, so playback can run directly through its audio output without relying on my laptop. This way i can just connect a speakers to the Pi's aux port and play the music through there.
* Create a case with a spinning motor that i can put small disks on to replicate an actual vinyl player

---

## 🙏 Acknowledgments
* Inspired by various open-source RFID Spotify projects, particularly:
  [Spotify RFID Record Player by talaexe](https://talaexe.com/moderndayrecordplayer)


