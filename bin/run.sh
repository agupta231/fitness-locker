#!/bin/bash

docker run -it --rm --privileged \
	--name fitness-locker \
	-p 5000:5000 \
	-v `pwd`/../src:/app \
	elixir:locker
