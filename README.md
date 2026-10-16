# OpsPulse — Server & Service Monitoring Dashboard

A small DevOps portfolio project built with Flask, psutil, Docker, and GitHub Actions.

## Features

- Service health endpoint: `/health`
- Resource metrics API: `/api/metrics`
- Dashboard refreshes metrics every 10 seconds
- Docker image runs as a non-root user
- Docker Compose health check
- GitHub Actions runs tests and builds the Docker image on pushes and pull requests to `main`

## Run locally with Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8000`.

## Run with Docker Compose

```bash
docker compose up -d --build
docker compose ps
docker compose logs -f
```

Open `http://localhost` on the same machine. Stop it with `docker compose down`.

## Deploy publicly on an Ubuntu EC2 instance

1. Create an Ubuntu EC2 instance and allow inbound TCP 22 from your own IP and TCP 80 from `0.0.0.0/0`. Do not expose port 8000 publicly.
2. Connect using SSH.
3. Install Docker using Docker's official Ubuntu installation guide: https://docs.docker.com/engine/install/ubuntu/
4. Install Git if needed: `sudo apt-get update && sudo apt-get install -y git`
5. Clone your GitHub repository: `git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git`
6. Enter the project folder and start it: `cd YOUR_REPOSITORY && sudo docker compose up -d --build`
7. Check it: `sudo docker compose ps` and `sudo docker compose logs -f`
8. Open `http://EC2_PUBLIC_IP` in a browser.

For a real production deployment, configure a domain name and HTTPS, restrict SSH to your own IP, patch the server, and add proper authentication if the dashboard is exposed beyond a demo. Do not place secrets in the repository.

## Important metrics note

The metrics describe the environment visible to the Python process. When containerized, CPU and memory readings can reflect the host/container environment depending on platform and configuration. Treat this as a demo, not a replacement for production observability.
