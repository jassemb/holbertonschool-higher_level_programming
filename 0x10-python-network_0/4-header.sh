#!/bin/bash
#takes URL, sends GET request display body
curl -s "$1" -X GET -H 'X-School-User-Id: 98'
