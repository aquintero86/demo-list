
# BackEndBase
Demo API list 


# Description
This system describes the use and setup of a **Demo Api rest** using [**Python**] (https://www.python.org/downloads/) and [**Flask**] (https://palletsprojects.com/p/flask/)




# Requirements
- [**Python**](https://www.python.org/downloads/) 3.7.x
- [**virtualenv**](https://virtualenv.pypa.io/en/stable/) (Recomended)
- [**Redis**](https://virtualenv.pypa.io/en/stable/) (Recomended)




## Install this repository
Clonar este repositorio y alojarlo en una carpeta conveniente.

    git clone https://github.com/aquintero86/demo-list.git

It is recommended to use [**virtualenv**](https://virtualenv.pypa.io/en/stable/) for development and testing.


##Activate virtualenv in Gnu / Linux environments

```sh
$ virtualenv --python python3 env
$ source env/bin/activate
```


## Install dependencies

Once inside the environment, install the dependencies: 
```sh
(env) $ pip install -r requirements.txt
```

# using the local environment (optional)
[** sqlite **] (https://www.sqlite.org/index.html) is being used as a database, it can be used in local mode.
```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
```



# Web server init
Some configurations for starting the web server are described below.


## Using Flask run (Recomended)

```sh
(env) $ flask run
```

## Using python

```sh
(env) $ python app.py
```

## Using docker

```sh
(env) $ docker-compose up
```

```sh
(env) $ gunicorn --bind 0.0.0.0:6969 --reload --log-level debug main:app
```


## Deployment in Google App Engine

### Using gcloud deploy

```sh
(env) $ gcloud app deploy --project PROJECT_ID --version VERSION_ID --no-promote
```

### Using gcloud build
```sh
(env) $ gcloud builds submit .
```
>La direccion y el puerto por defecto es: [**http://localhost:5000**](http://localhost:5000)



# Estructura del Proyecto (Propuesta)
```text
/
    __
    ├── app.py
    ├── app.yaml
    ├── cache.py
    ├── config.py
    ├── db.py
    ├── docker-compose.yml
    ├── Dockerfile
    ├── exceptions.py
    ├── functions.py
    ├── model.py
    ├── Procfile
    ├── redis_conn.py
    ├── requirements.py
    └── users.sqlite3
    ├── .gitignore
    ├── app.yaml
    ├── Dockerfile
    ├── LGPL.txt
    ├── README.md
    ├── requirements.txt

