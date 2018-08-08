import requests
import json

if __name__ == '__main__':
    depart = "FCO"
    arrive = "WAW"
    date = "2018-08-22"
    people = '1'
    data = {"isFlightChange":'false',"isSeniorOrStudent":'false',
                                "flightList":[{"departureStation":depart,"arrivalStation":arrive,"departureDate":date}],
                                "adultCount":people,"childCount":'0',"infantCount":'0',"wdc":'true'}
    r = requests.post(url="https://be.wizzair.com/8.2.0/Api/search/search",
                      json=data,
                      headers={"content-type": "application/json;charset=UTF-8"})
    text = r.json()
    print(text['outboundFlights'])

