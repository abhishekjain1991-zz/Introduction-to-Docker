How to run the Load Balancer on Docker
1) docker build -t node-hello .
2) docker run -p 80:80 --name web -d node-hello

This spins up the new container with the Docker application image.
We can benchmark the container using the Apache Benchmark by the following command:
ab -n 10000 -c 10 http://ip of rpi/

Install docker-compose for the ARM-based Raspberry pi by the following command:
sudo sh -c "curl -L https://github.com/hypriot/compose/releases/download/1.1.0-raspbian/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose;
chmod +x /usr/local/bin/docker-compose"

Start the webserver farm by "docker-compose up -d"
Benchmark the load balancer by the same Apache Benchmark command ab -n 10000 -c 30 http://localhost/

	