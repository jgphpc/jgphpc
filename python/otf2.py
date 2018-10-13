#!/usr/bin/env python3

## https://silc.zih.tu-dresden.de/otf2-2.1/python/examples.html

import otf2
from otf2.events import *

def read_trace(trace_name="./traces.otf2"):
     with otf2.reader.open(trace_name) as trace:
          print("Read {} string definitions".format(len(trace.definitions.strings)))
          for string in trace.definitions.strings:
              print("String definition with value '{}' in trace.".format(string))

          for location, event in trace.events:
            if isinstance(event, Enter):
                print("Encountered enter event into '{event.region.name}' on location {location} at {event.time}".format(location, event))
            elif isinstance(event, Leave):
                print("Encountered leave event for '{event.region.name}' on location {location} at {event.time}".format(location, event))
            else:
                print("Encountered event on location {} at {}".format(location, event.time))


if __name__ == "__main__":
    read_trace()
