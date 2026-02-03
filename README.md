# Runner Backend

The central server for Runner. Built with Flask to manage user authentication, global leaderboards, and game distribution.

## Features

- **User Auth**: Dedicated endpoints for player signup and login.

- **Leaderboard API**: Securely submit and retrieve scores via MongoDB.

- **Asset Hosting**: Serves the latest `.exe` build for players.

## API Endpoints

**Authentication**

- `POST /api/signup` — Register a new player account.

- `POST /api/login` — Authenticate player from the Pygame client.

**Gameplay**

- `POST /api/add-score` — Submit a new score.

**Distribution**

- `GET /download` — Download the compiled Runner.exe.

---

Built with Problem Solving by [Zain Khoso](https://linkedin.com/in/zain-khoso)