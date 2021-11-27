# 課題Webserv - config 挙動確認用Docker container

## How to use
### Build and run
Build a docker image.
``docker build -t webserv_image .``

Run the image.
``docker run -d -p 8080:80 --name webserv webserv_image``

### Access the page
For example
- http://localhost:8080
- http://localhost:8080/notfound

