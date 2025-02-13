#!/bin/bash

docker run -it -p 127.0.0.1:8100:8100 -v `pwd`/slides:/slidev/slides --entrypoint npx slidev -- slidev -p 8100 --remote '' slides/session01/session01.md
