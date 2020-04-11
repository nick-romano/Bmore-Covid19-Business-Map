
# Bmore-Covid19-Business-Map
https://bmore-curbside-map.site/

# Details
A python data build that spits into a react front end and runs through docker.


## Workflow
1. Data
    - Docker pulls python 3.7 and installs requirements.txt
    - The python script in scraper pulls data from google spreadsheets and creates a json for the data
2. Front End
    - The front end is built in react with mapbox and antd
    - Docker places the json output from the data stage into the front end src files and that works as a local static dataset
    - Docker builds the front end
3. Server
    - Docker pulls NGINX and the front end code and serves it up on an EC2 instance
    
 
