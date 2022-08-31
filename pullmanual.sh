#!/bin/bash

lab=$1

# wget --no-check-certificate https://www.openwall.com/john/k/${lab}.tar.gz
wget https://thepracticecloud.s3.us-west-2.amazonaws.com/MachineLearning/${lab}.tar.gz
tar zxvf ${lab}.tar.gz
