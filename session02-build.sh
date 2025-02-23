#!/bin/bash

rm -fr session02/
docker run -it -v `pwd`/slides:/slidev/slides --entrypoint npx slidev -- slidev build --base /epfl-civil-127/session02/ slides/session02/session02.md
mv slides/session02/dist ./session02
