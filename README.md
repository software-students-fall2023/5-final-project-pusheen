
[![Python application CI/CD](https://github.com/software-students-fall2023/5-final-project-pusheen/actions/workflows/python-app-ci.yml/badge.svg)](https://github.com/software-students-fall2023/5-final-project-pusheen/actions/workflows/python-app-ci.yml)
# Final Project


#Fitwell Tracker
Fitwell Tracker is an nutrition tracker used for logging meals and keeping track of weight. The app helps people keep track of their diet and the meals they eat on an every day basis as well as seeing how these meals may affect their weight/health. This app is for personal use.



# Team Members

[Andrew Huang](https://github.com/andrewhuanggg)

[Jazlene Darrisaw](https://github.com/Jazlene30)

[Henry Wang](https://github.com/fishlesswater)

[Ahmed Omar](https://github.com/ahmed-o-324)



# Setting Up

## Running Locally
1. Clone the repository 
2. run pip install --no-cache-dir -r requirements.txt
3. run python app.py


## Running with Docker (run the following commands)
1. cd 5-final-project-pusheen
2. git pull
3. docker-compose pull
4. docker-compose up

## Running Tests
1. pipenv install pytest
2. run pytest
3. pipenv install coverage.py
4. run python -m coverage run -m pytest tests
5. run python -m coverage report -m


# Digital Ocean - Deployed App
- URL : http://143.198.4.193:5000/


# Links to container image


Web app image: https://hub.docker.com/repository/docker/alh8007/
finalproject/general



Mongo image: https://hub.docker.com/_/mongo
