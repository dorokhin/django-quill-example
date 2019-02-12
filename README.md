# django-quill-example
Django app quill editor example


Awesome Quill

https://github.com/quilljs/awesome-quill

#### Build containers

```bash
docker-compose up -d --build
```

#### Create directories
```bash
docker exec -it django-quill-example_web_1 sh
mkdir -p /data/media/img/blog
chown -R nginx:nginx /data/media/img/
```

#### Check container logs
```bash
docker logs django-quill-example_web_1
```

```bash
docker exec -it django-quill-example_db_1 sh
```

```bash
docker exec -it django-quill-example_db_1 psql editor admin
```


```bash
docker exec -it django-quill-example_web_1 python3 manage.py collectstatic --noinput
```

```bash
docker exec -it django-quill-example_web_1 python3 manage.py makemigrations
```

```bash
docker exec -it django-quill-example_web_1 python3 manage.py migrate
```

```bash
docker exec -it django-quill-example_web_1 python3 manage.py createsuperuser --username=deepblack --email=andrew@dorokhin.moscow
```

