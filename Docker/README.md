# Docker

## Starting Docker Containers

### MongoDB

`docker run -d -p 27017-27019:27017-27019 --name mongodblagring mongo:latest`


### MySQL

`docker run --name datalagring-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:latest`
