# GraphQL API for Seal Haulage Sites

## Built with Python, Flask and Ariadne

![Screenshot](screenshot.png?raw=true)

Created after following this blog post 
[https://www.twilio.com/blog/graphql-api-python-flask-ariadne](https://www.twilio.com/blog/graphql-api-python-flask-ariadne)


## Data
Contains information from Scottish Government (Marine Scotland) & Sea Mammal Research Unit licensed under the Open Government Licence v3.0.  Seal haulage site data from [https://spatialdata.gov.scot/geonetwork/srv/eng/catalog.search#/metadata/Marine_Scotland_FishDAC_1278](https://spatialdata.gov.scot/geonetwork/srv/eng/catalog.search#/metadata/Marine_Scotland_FishDAC_1278)

----
## Running the api

* Use `flask run main.py` to start the Flask server
* Open the GraphQL PlayGround that comes with Ariadne by visiting `http://127.0.0.1:5000/graphql`


Sample queries can be found in `example_queries.graphql`
