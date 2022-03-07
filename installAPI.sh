#!/bin/bash
 docker pull hercules42/sbfteste:latest
 sudo docker run --name testeSBF -p 8080:8080 -d -it hercules42/sbfteste /bin/bash
 docker exec testeSBF service postgresql start
 docker exec testeSBF waitress-serve --port=8080 --call app:create_app &
