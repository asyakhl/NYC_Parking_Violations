# Using NYC Open Parking and Camera Violations API

## Requirements

This project uses NYC Parking Violations data from [NYC Open Data.](https://opendata.cityofnewyork.us/)
The data is pulled from [Open Parking and Camera Violations](https://dev.socrata.com/foundry/data.cityofnewyork.us/nc67-uf89) (OPCV) API, which is made available via 
[Socrata Open Data API](https://dev.socrata.com/).The [app_token](https://data.cityofnewyork.us/login) is necessary to access NYC Open Data APIs.

## Docker Image for Accessing the API

The docker image for retrieving data from OPCV API can be pulled from [this dockerhub profile](https://hub.docker.com/u/asyakhleborodova). The following command line can be used to access OPCV API data:

## Using the API 

$ docker run -e APP_KEY=YOUR_APP_TOKEN -t nyc_parking_violations:1.0 python -m main --page_size=1000 --page_num=4 --output=results.json

--page_size: This command argument is required.

--page_num: This argument is optional, if not provided the API will return all of the
available content. 

--output: This argument is optional, if not included results will be printed to stdout. 