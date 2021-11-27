# A container for  checking the operation of  webserv-config file

## How to use
### Build and run
Build a docker image.
```
docker build -t webserv_image .
```

Run the image.
```
docker run -d -p 8080:80 --name webserv webserv_image
```

Execute bash in webserv container.
```
docker exec -it webserv bash
```

### Access the page
For example
- http://localhost:8080
- http://localhost:8080/notfound

