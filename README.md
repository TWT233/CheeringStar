# cheeringstar

[discord bot] pvp rank & info query for Princess Connect Re:Dive

# usage

1. put your pcr account playerprefs xml files into `conf/`

> get playerprefs yourself, no tutorial here >.<)

2. `cp conf/config.yaml.placeholder conf/config.yaml`
3. filling conf/config.yaml fields
4. `pip install -r requirements.txt`
5. `python src/main.py`

# structure

```
cheeringstar
├── conf        ---------------------- config & playerprefs laying here
│   └── config.yaml.placeholder
├── db
├── LICENSE
    ├── README.md   <----------------- you are here! 
├── requirements.txt
└── src
    ├── client.py   ------------------ manage pcr clients
    ├── cmd     ---------------------- define commands
    │   ├── admin.py
    │   ├── chaxun.py
    │   ├── dingyue.py
    │   ├── help.py
    │   └── __init__.py
    ├── config.py   ------------------ make config file ez to use
    ├── db      ---------------------- db ORM
    │   ├── crud.py
    │   ├── __init__.py
    │   ├── init.py
    │   └── models.py
    └── main.py     ------------------ program entry
```