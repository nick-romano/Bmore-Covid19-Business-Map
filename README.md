
# Bmore-Covid19-Business-Map (Archived)
https://nick-romano.github.io/Bmore-Covid19-Business-Map/

# Details
This was an application that ran on Docker. It would parse a live Google Spreadsheet that contained updated details for restaurants in Baltimore at the start of the Covid-19 pandemic. The script would take each location and use the Google Places API to plot the location on a map. The final locations and details were visualized using a custom web map application. The docker container managed the running of the script followed by the hosting of the website / webmap. The current github pages URL is just an archive from one of those runs.


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
    
 
