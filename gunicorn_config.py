"""Gunicorn configuration for Render deployment"""
import os

# Bind to 0.0.0.0 on PORT from environment
bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"

# Worker configuration
workers = 2
worker_class = "sync"
timeout = 120

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Server mechanics
daemon = False
pidfile = None
