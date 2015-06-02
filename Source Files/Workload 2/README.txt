How to run Python script on docker
1) Once docker has been installed, build the container using :-
	docker build -t workload2 .
	This will run the Dockerfile which will install all the needed packages inside docker.
2) Now start an interactive container by :-
	docker run -i /bin/bash
3) time echo "scale=3000;4*a(1)" | bc -l
	
	