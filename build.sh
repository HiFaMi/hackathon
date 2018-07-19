#!/usr/bin/env bash
pipenv lock --requirements > requirements.txt
git add -f .secrets
git add -A
eb deploy --profile fc-8th-eb --staged
git reset HEAD requirements.txt .secrets
rm -rf requirements.txt