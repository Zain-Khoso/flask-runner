# Runner Backend

The central server for Runner. Built with Flask to manage user global leaderboards and game distribution.

## Features

- **Leaderboard API**: Securely submit and retrieve scores via MongoDB.

- **Asset Hosting**: Serves the latest `.exe` build for players.

## API Endpoints

**Gameplay**

- `POST /api/add-score` — Submit a new score.

**Distribution**

- `GET /download` — Download the compiled Runner.exe.

---

Built with Problem Solving by [Zain Khoso](https://linkedin.com/in/zain-khoso)