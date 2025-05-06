Multi-User Tic Tac Toe (Python + Tkinter + Sockets)

This is a simple two-player networked Tic Tac Toe game built with Python using `Tkinter` for the GUI and `socket` for networking. One player hosts the game (server), and the other connects to it (client) over localhost or a network.

Features

- Real-time two-player Tic Tac Toe over TCP
- Simple and responsive GUI using Tkinter
- Win and draw detection with message alerts
- Easy setup for local or LAN play

Requirements

- Python 3.x

No external libraries are required beyond Python’s standard library.

How to Run
1. Host (Player X)

Run the host script:
python host.py
This will start the server and wait for a client to connect.

2. Client (Player O)
In a separate terminal or machine, run the client script:
python client.py
The client will connect to the host on localhost:9999

Game Rules
Player X (Host) always starts.
Players alternate turns.
The game ends when a player wins or the board is full (draw).
A message box will display the result and then close the application.
