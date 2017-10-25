# Eyes Defender

Show black screen for 2 minutes every 20 minutes.
Remember to user to have a rest.


## Linux Install

```
apt install python-tk python3-tk
git clone ...
cd ...
pip install -r requirements.txt
```

## Start

Eyes.Defender use Python3.

```
./defender.py
```

## Autostart

Add/remove script to autostart use:

* `./defender.py install`
* `./defender.py uninstall`

## Settings

You may set yours work/rest periods. 

```
cp example.config.yaml config.yaml
vim config.yaml
```