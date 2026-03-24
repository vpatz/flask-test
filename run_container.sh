#!/bin/bash

podman build -t flask-test:latest .
podman run -d -p 5000:5000 --name flask-test-container flask-test:latest