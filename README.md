# Setup
## Script download and setup
- download the script: `wget https://raw.githubusercontent.com/matmarx/tryhackme-streak-watcher/refs/heads/main/script.py -O ~/.thm-streak.py`
- edit variables (username, streak start date, discord webhook): `vim ~/.thm-streak.py`
## Cronjob
- edit crontab: `crontab -e`
- add following cronjob that will run the script daily at 22:45 localtime: `45 22 * * * wall $(python3 ~/.thm-streak.py)`

The script can be ran manually whenever for testing purposes.
