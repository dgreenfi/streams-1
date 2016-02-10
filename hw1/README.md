# Exercise 1 - Storytelling and Streaming Data
## David Greenfield (dg2815)


## Part I - Stream Description
The stream I used was one that I created via polling of Microsoft Bing Traffic API.  The api is documented on the [Microsoft Bing Website] (https://msdn.microsoft.com/en-us/library/hh441726.aspx).  

The API provides a REST API that is part of a broader BING Maps suite. At a high level the API returns a list of objects that represent potential travel disruptions and metadata that both describes the event and it's attributes (such as type and severity), as well as metadata to help navigate alternatives (detour).  The API returns a number of data points about Traffic Incidents that may be relevant to travel.  The types of events included are:

+ Accident
+ Congestion
+ DisabledVehicle
+ MassTransit
+ Miscellaneous
+ OtherNews
+ PlannedEvent
+ RoadHazard
+ Construction
+ Alert
+ Weather

These events include a broad base of events that could impact travel both on roads and mass transit.  The API also includes a severity of the event so that applications (and people) can filter through a large list of traffic events to filter to only the most potentially disruptive.  The severity is grouped into 4 categories.

+ LowImpact
+ Minor
+ Moderate
+ Serious

For this homework, I will only use events of type 4 severity.

Events also have a number of times associated with them.  The times are clearly designed to be used in mapping system and are directed towards display on a map and not towards gathering information on the history of the event.  The times include a start time, last modified time (useful in detecting changes) and an end time for planning future channel.

###maps_poller.py - Stream Creation file
In order to create a stream, I make a GET request over the mapArea 35,-68,45,-78.  This is a large bounding box around the NY area. 
I expanded it fairly large to increase the amount of data streaming.  Additionally, in order to both conserve Google
images requests and to keep the content updating I send only 1 event from the api at a time and keep a queue of events
to be served and a list of already served events for detecting new events from the API.

The messages sent to the site are a simplified JSON containing only the attributes I use in the display (description,
coordinates) and the id.

###index.html - Site Page
The site connects to the local websocket server at port 8080.  The site parses the JSON messages and inserts the components 
into the body of the HTML.  Additionally a dynamic call to the Google Street View API is made and used as an inserted image
reference.

### Site Stream
The resulting site stream is a changing display of the description and an image of the location of a 'severe' traffic 
incident


##Part II - starting the site
Note: The site may hit rate limits:
microsoft bing maps key - 10,000/day rate limit
google streetview maps key - 1000/day image limit


###Step 0 - Place Credentials
Make sure credentials file including Microsoft Key and Google key is in /cred
Format should be JSON:
{"bing_key":"{key}",
"google_key":"{key}"}

###Step 1 - Start the polling server
The polling server can be started by running the following within the server folder:
websocketd --port=8080 --staticdir=. bash run_poller.sh 


###Step 2 - Start the Website server
The site server can be started by running
 python -m SimpleHTTPServer from within the root project directory

###Step 3 - Browse to localhost:8000
Enjoy!

