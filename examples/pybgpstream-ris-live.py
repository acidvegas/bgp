#!/usr/bin/env python

import pybgpstream
stream = pybgpstream.BGPStream(
    # accessing ris-live
    project="ris-live",
    # filter to show only stream from rrc00
    filter="collector rrc00",
)

for elem in stream:
    print(type(elem))
    print(elem)
