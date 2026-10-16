import os
import time
from datetime import datetime, timezone

import psutil
from flask import Flask, jsonify, render_template

app = Flask(__name__)
START_TIME = time.time()
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.get("/")
def index():
    return render_template("index.html", version=APP_VERSION)


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "devops-monitoring-dashboard",
        "version": APP_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


@app.get("/api/metrics")
def metrics():
    boot_time = datetime.fromtimestamp(psutil.boot_time(), tz=timezone.utc)
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=0.25),
        "memory_percent": psutil.virtual_memory().percent,
        "memory_used_mb": round(psutil.virtual_memory().used / (1024 * 1024)),
        "memory_total_mb": round(psutil.virtual_memory().total / (1024 * 1024)),
        "disk_percent": psutil.disk_usage("/").percent,
        "app_uptime_seconds": int(time.time() - START_TIME),
        "server_boot_time": boot_time.isoformat(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
