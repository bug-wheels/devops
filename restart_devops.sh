#!/usr/bin/env bash
kill -9 $(ps -ef | grep gunicorn | grep -v grep | awk '{print $2}')
git pull
gunicorn -w 4 -b 0.0.0.0:7000 devops.wsgi