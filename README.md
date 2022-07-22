# behai/app-demo:arm64flask

Build Docker image on Windows 10 Pro for linux/arm64, using Flask development server.

Python codes updated to use absolute import with requirements.txt.

## Built image location

```
https://hub.docker.com/repository/docker/behai/app-demo
```

## To clone this branch

```
git clone -b arm64flask --single-branch https://github.com/behai-nguyen/app-demo.git
```

The codes are in **app-demo** directory of where we are.

## To build and to run

### To build

```
D:\app_demo>docker buildx build --platform linux/arm64 --tag behai/app-demo:arm64flask --push .
```

### To run the image

```
$ sudo docker run -d --network=host -v "/run/docker.sock:/var/run/docker.sock" --rm behai/app-demo:arm64flask
```

### To run the application

```
http://0.0.0.0:9880
```

Replace **0.0.0.0** with appropriate IP address. For example:

```
http://omphalos-nas-01:9880
```

## On .env

I understand it should not be checked in. But this is only a development project, I checked it in for the shake of completeness.

## License
[ MIT license ](http://www.opensource.org/licenses/mit-license.php)
and the [ GPL license](http://www.gnu.org/licenses/gpl.html).
