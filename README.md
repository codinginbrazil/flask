# [Flask](https://flask.palletsprojects.com/)


#### [Requirements](https://github.com/codinginbrazil/flask/blob/master/requirements.txt)
> Python version 3.8.5
#### Docker
~~~bash
# Permissão para o usuário executar o docker.sock
sudo cd /var/run && sudo chown wellington -R docker.sock
~~~

##### Dockerfile
~~~bash
docker build --pull --rm -f "Dockerfile" -t image_name "."
~~~

##### Docker Compose
~~~bash
docker-compose -f "docker-compose.yml" up -d --build
~~~

* Server
> http://0.0.0.0:5000/

##### Install requirements
~~~bash
pip install -r requirements.txt
~~~

--- 

#### Saiba mais
##### Palestra
* [Introdução ao Flask - Eduardo Mendes](https://www.youtube.com/watch?v=Snxl0T8ugeI)

##### Curso
* [Júlia Rizza](https://www.youtube.com/watch?v=r40pC9kyoj0&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
* [CodeShow - Bruno Rocha](https://www.youtube.com/watch?v=QxPebq0DZoo&list=PLjSf4DcGBdiHcpYGF5vWKBoo32c-xjXuZ)

##### Conferência 
* [FlaskConf - BR](https://www.youtube.com/channel/UCcjcRw_NjYJdW2ZaXsBiDqg/featured)

##### Docker
* [Docker Hub](https://hub.docker.com/_/python?tab=description) 
* [Docker para desenvolvedores - Rafael Gomes](https://leanpub.com/dockerparadesenvolvedores)
* [runnable.com](https://runnable.com/docker/python/docker-compose-with-flask-apps)
* [rollout.io](https://rollout.io/blog/using-docker-compose-for-python-development/)