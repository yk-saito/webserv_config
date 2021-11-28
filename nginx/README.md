# A container for  checking the operation of  nginx-config file

## How to use
### Build and run
Build a docker image.
```
docker build -t nginx_image .
```

Run the image.
```
docker run -d -p 8080:80 --name nginx nginx_image
```

Execute bash in webserv container.
```
docker exec -it nginx bash
```

### Access the page
For example
- http://localhost:8080
- http://localhost:8080/notfound


