#!/usr/bin/env bash
pipenv lock --requirements > requirements.txt
docker build -t hackathon:dev -f Dockerfile.dev .
rm -rf requirements.txt