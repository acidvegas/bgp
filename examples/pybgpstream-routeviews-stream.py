#!/usr/bin/env python

import pybgpstream
stream = pybgpstream.BGPStream(
    # accessing routeview-stream
    project="routeviews-stream",
    # filter to show only stream from amsix bmp stream
    filter="router amsix",
)

for elem in stream:
    print(elem)
