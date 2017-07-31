#!/bin/bash
mytoken=1234567
curl --data "token=$mytoken&amount=$1&text=$2" localhost:8009/submit/expense/