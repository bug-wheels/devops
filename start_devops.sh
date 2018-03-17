#!/usr/bin/env bash
gunicorn -w 4 -b 0.0.0.0:7000 devops.wsgi