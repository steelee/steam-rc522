# steam-rc522
Launching Steam games in Windows with Arduino and RFID Cards

This is an experiment with an Arduino NFC. To use the chip RFID-RC522 (MF-RC522) I used [miguelbalboa's RFID library](https://github.com/miguelbalboa/rfid) to read and write. I used [this RFID reader/writer](http://www.amazon.com/gp/product/B00E0ODLWQ?psc=1&redirect=true&ref_=oh_aui_detailpage_o00_s00) wired using the SPI interface to an Arduino Mega2560.

The first commit was more or less a proof-of-concept that got me familiar with RFID.

Things I want to do in the future:

1. Auto-generate paths to game executables.

2. Have user store games in config file or some local database, read from that to get new games.

3. Have one Arduino sketch to write any game, instead of one per game.

4. PyQt??

5. Something involving giant fighting robots.
