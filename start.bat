@echo off

:: Flask im Hintergrund starten, ohne ein zusätzliches Fenster zu öffnen
start /b python app.py

:: Browser mit der Flask-URL öffnen
start "" http://127.0.0.1:5000

:: Batch-Prozess beenden (ohne Pause)
exit