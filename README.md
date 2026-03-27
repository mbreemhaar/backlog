# Backlog

Backlog is a self-hosted to-do management REST API built with FastAPI and 
PostgreSQL. It is designed to be client-agnostic, meaning anyone can build their
own frontend or UI on top of it.

## Status

Backlog is in early development and is not yet ready for use.

## Getting Started

### Prerequisites

To run Backlog on your system, you need to have the following installed:

- [Python 3.13+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/)
- [Docker](https://www.docker.com/) (for running PostgreSQL)

### Development Setup

1. Clone and `cd` into the repository using SSH:
   ```sh
   git clone git@github.com:mbreemhaar/backlog.git
   cd backlog
   ```
   or using HTTPS:
   ```sh
   git clone https://github.com/mbreemhaar/backlog.git
   cd backlog
   ```
2. Install dependencies using `uv`:
   ```sh
   uv sync
   ```
3. Copy the example environment file and adjust as needed:
   ```sh
   cp .env.example .env
   ```
4. Start the PostgreSQL database:
   ```sh
   docker compose up -d
   ```
5. Run the application:
   ```sh
   uv run fastapi dev
   ```

## Quality Checks

Run these checks locally before pushing:

| Check | Command |
| --- | --- |
| Lint | `uv run ruff check` |
| Format check | `uv run ruff format --check` |
| Format fix | `uv run ruff format` |
| Type check | `uv run mypy .` |
| Test | `uv run pytest` |

## License

Backlog is licensed under the [MIT License](LICENSE).
