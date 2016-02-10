
import time
import requests
import json

from sys import stdout

def main():
    #polls for new sever accidents and adds them to a json list, pops 1 at a time and sends them to the stdout
    events=[]
    proc_events=[]
    creds=load_creds('../cred/keys.txt')

    while True:
        #get new results
        res=pingserver(creds['bing_key'])
        #reconciles new events by ID
        events+=new_events(res,proc_events)
        #sends to server
        events=output_severe_loc(events,proc_events,creds['google_key'])
        #pastmax,inc_ids=outputnew(res,pastmax,inc_ids)
        time.sleep(5)

def load_creds(credloc):
    #load keys from key file
    with open(credloc) as data_file:
        data = json.load(data_file)
    return data

def new_events(res,proc_events):
    new_events=[]
    #create a list of incidents to output with just the attributes I want: coordinates, description, severity,id
    for set in res['resourceSets']:
        for incident in set['resources']:
            #only output severe incidents
            if incident['severity']==4:
                #only output if id not in processed list
                if incident['incidentId'] not in proc_events:
                    #only process if not previously processed
                    new_events.append({'id':incident['incidentId'],'coordinates':incident['toPoint']['coordinates'],\
                        'description':incident['description'],'severity':incident['severity']})
    #return new events
    return new_events

def output_severe_loc(new_events,proc_events,gkey):
    #remove 1 event from the queue to show, was going to sort by severity but there wasn't much granularity there
    disp_event=new_events.pop()
    proc_events.append(disp_event['id'])
    disp_event['google_key']=gkey
    #send to stdout
    print json.dumps(disp_event)
    #print check for event processing logic
    # flush stdout to websocket
    stdout.flush()
    return new_events

def ping_server(key):
    #gets raw response from server for hardcoded lat, long range
    url='http://dev.virtualearth.net/REST/v1/Traffic/Incidents/35,-68,45,-78?'
    url+='&key='+key
    r= requests.get(url)
    return r.json()


def clean_mod(strmod):
    #clean up bing date string format of "lastModified":"\/Date(1309391096593)\/", to numerical for comparison
    ## not bring used for final version
    temp=strmod.split('(')[1]
    temp=int(temp[0:-2])
    return temp


if "__name__"!='main':
    main()