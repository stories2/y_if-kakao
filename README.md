# y_if-kakao

## Run latest service

```
ps -ef | grep yif
kill <yif root process>
```

## Nginx conf

```
server {
        listen 80;
        server_name stories2.iptime.org;

        location / {
                include uwsgi_params;
                uwsgi_pass unix:/home/stories2/y_if-kakao/yif.sock;
        }
}
```

## Init script

```
description "This is y-if service init script"

setuid yif
setgid www-data

exec uwsgi -s /home/stories2/y_if-kakao/yif.sock -w wsgi:app --http-processes=4 --chmod-socket=666 --master &
```

## Service logs

```
sudo tail -f /var/log/nginx/<access.log> or <error.log>
```

## Library

```
sudo pip3 install flask
sudo pip3 install Slacker
sudo pip3 install googletrans
```