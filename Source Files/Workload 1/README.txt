How to run a Python script on docker
1) Once docker has been installed, build the container using :-
	docker build -t workload1 .
	This will run the Dockerfile which will install all the needed packages inside docker.
2) Now start an interactive container by :-
	docker run -i /bin/bash
3) This creates an interactive session where you can run the python script in the following way:
	python findprime.py 10000
4) The argument 10000 is the range N. This can be changed as per as your convenience.
	