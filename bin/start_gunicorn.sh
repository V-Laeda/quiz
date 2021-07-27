#!/usr/bin/env bash
source /home/user/Проекты/quiz/venv/bin/activate
exec gunicorn -c "/home/user/Проекты/quiz/quizpr/gunicorn_config.py" quizpr.wsgi
