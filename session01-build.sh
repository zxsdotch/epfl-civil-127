#!/bin/bash

docker run -it -v `pwd`/slides:/slidev/slides --entrypoint npx slidev -- slidev build --base /epfl-civil-127/session01/ slides/session01/session01.md
mv slides/session01/dist ../published_slides/epfl-civil-127/
