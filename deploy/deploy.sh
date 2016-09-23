#! /bin/sh


docker build -f Dockerfile -t myimage ../
docker run -d --name mycontainer -p 443:80 myimage
