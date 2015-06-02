How to run Apache2 on docker
1) Once docker has been installed, build the container using :-
	docker build -t apache .
	This will run the Dockerfile which will install all the needed packages inside docker.
2) Now start an interactive container by :-
	docker run -i /bin/bash
3) This create an interactive session where you can run the ab command in the following way:
	ab -n 10000 -c 10 http://localhost/
	