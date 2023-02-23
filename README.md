# UOCIS322 - Project 4 #
You'll learn how to write test cases and test your code, along with more JQuery.

## Overview

This project is a web server that reimplements the RUSA ACP controle time calculator created with `Flask` and `AJAX`. 
The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Further background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders).

We are replacing the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data. 

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine or Docker for development and testing purposes.

### Installing

To get started with this project, fork the repository and clone it onto your local machine using `git clone`. Once cloned, head into the brevets/ directory and run the command `pip install -r requirements.txt`, followed by `python3 flask_brevets.py`.

Instead of using your local machine, you can also use Docker to build and run this project. Simply build a Docker image by using the command `docker build -t [image_name] .`, followed by `docker run -d -p PORT:5000 [image_name]`. This run command will run and create a Docker container in detached mode `-d` and maps a network port `-p` on the host machine to the port `5000` in the container. 

If you want to interact with the container, you can use the command `docker exec -it [container_name] /bin/bash`, enabling you to perform commands and interact with the container's file system. Since this container is running a web server, you can acceess it from your browser by typing `http://localhost:PORT`, where `PORT` is the port number that you speficied in the `docker run` command.

## Tasks

### Flask (back-end)

Users can input the brevet distance, control distance, start time, and kilometer numbers through a web interface that uses Flask and delivers the relevant open and close times in JSON format. It uses the Python libraries `arrow` and `acp_times` to perform time calculations. The main logic of this web application resides in the `_calc_times()` function, which takes in the number of kilometers, distance traveled, and start time as inputs and returns the open and close times with the `YYYY-MM-DDTHH:mm` format as a string. 


### JQuery (front-end)

The front-end logic uses JQuery that provides functionality for getting and setting values of the HTML input fields. The `calc_times` function was implemented from `flask_brevets.py`. The `calc_times` function is triggered when the user inputs a kilometer value. It retrieves the user's input of brevet distance and start time as well as the kilometer value. The function then sends a GET request to a URL with the kilometer, brevet distance, and start time as parameters. The server response, parsed as JSON, provides the open and close times, which are then used to update the corresponding fields in the HTML.

### RUSA ACP controle time algorithm

The algorithm used to calculate the opening and closing times for checkpoints along a route was implemented into the `brevets/acp_times.py` file. 

The `open_time` function uses a set of predefined speed limits for difference ranges of distances, and calculates the total time required to reach the checkpoint based on the distance and speed limits. The function returns the time at which the checkpoint should be opened, based on the start time and total time required to reach the checkpoint.

* Note that the `open_time` uses the maximum speed for these calulations.

The `close_time` function determines the total time necessary to reach the checkpoint based on the distance and speed constraints by using a series of predetermined closing times for particular distances along the route. The function returns the close time for the last checkpoint if the distance of the checkpoint is higher than or equal to the total distance of the ride. Based on the start time of the ride and the total time necessary to reach the checkpoint, the function returns the time at which the checkpoint should be closed.

* Note that the `close_time` function uses the minimum speed for these calculations.


| Control location (km) | Minimum Speed (km/hr) | Maximum Speed (km/hr) |
| --------------------- | --------------------- | --------------------- |
|	   0-200	|	    15		|	    34		|
|	   200-400	|	    15		|	    32		|
|	   400-600	|	    15		|	    30		|
|	   600-1000	|	    11.428	|	    28		|
|	   1000-1300	|	    13.333	|	    26		|

Table from:
	https://rusa.org/pages/acp-brevet-control-times-calculator

### Testing

Five test cases were implemented in the `test_acp_times.py` file based on the interpretation of rules described here https://rusa.org/pages/acp-brevet-control-times-calculator to ensure that the algorithm works as intended. Testing was done using `Nose test suite` for automation.  

* The test casees considers the distances from `0-200km`, `0-300km`, `0-400km`, `0-600km`, and `0-1000km`. 

To run these tests, within the `brevets/` directory, enter `nosetests` into the terminal and all five test cases should pass. 

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.

Completed by Simon Zhao: simonz@uoregon.edu
