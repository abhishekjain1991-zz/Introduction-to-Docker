How to run Sysbench on docker
1) Once docker has been installed, build the container using :-
	docker build -t sysbench .
	This will run the Dockerfile which will install all the needed packages inside docker.
2) Now start an interactive container by :-
	docker run -i /bin/bash
3) This creates an interactive session where you can run the sysbench command in the following way:
	sysbench --test=cpu --num-threads=1 run
4) Scale the threads from 1 to 8.
	