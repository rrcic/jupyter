#!/bin/bash

lab=$1
wget https://thepracticecloud.s3.us-west-2.amazonaws.com/MachineLearning/${lab}.tar.gz
tar zxvf ${lab}.tar.gz
rm ${lab}.tar.gz
