#!/usr/bin/env python3
import nrewebservices.ldbws
from config import key

def main(fr, to):
    session = nrewebservices.ldbws.Session("https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16", key)
    a = session.get_fastest_departures([fr], [to])
    b = a.next_departures.pop()
    print(b.service.eta)

if __name__ == "__main__":
    fr = input("From:\n")
    to = input("To:\n")
    main(fr, to)
