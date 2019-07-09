# Keep the Dockerfile in your code root Path and execute the below from same path

$ docker build -t flaskapp:latest .
$ docker run -p 5000:5000 flaskapp

# Other Docker Commands

docker kill $(docker ps -q)
docker rm $(docker ps -a -q) 
docker rmi $(docker images -q) carefull

docker system prune (to remove unused containers)

sudo docker exec -it 1c50b67d45b1 bash 
winpty docker exec -it af18e943297b bash


# Curl commands for testing

# with JWT enabled
curl -X GET -H 'Accept: application/json' -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjI2ODM2MzcsImlhdCI6MTU2MjY4MzMzNywibmJmIjoxNTYyNjgzMzM3LCJpZGVudGl0eSI6MX0.cPy6DzAQVDB6PU9GVUhduYGOqj2h35rWAtJTTb54vzs" http://127.0.0.1:5000/items

# without JWT enabled
curl -X PUT -H "Content-Type: application/json" -d '{"price":22}' http://127.0.0.1:5000/item/new

curl -X POST -H "Content-Type: application/json" -d '{"price":22}' http://127.0.0.1:5000/item/tea2

curl -X DELETE http://127.0.0.1:5000/item/new

# User registration & authentication
curl -X POST -H "Content-Type: application/json" -d '{"username": "prem", "password" : "newpass12123"}' http://127.0.0.1:5000/auth      

curl -X POST -H "Content-Type: application/json" -d '{"username": "prem", "password" : "newpass12123"}' http://127.0.0.1:5000/register

