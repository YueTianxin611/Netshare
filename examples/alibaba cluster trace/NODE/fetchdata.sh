#!/bin/bash  
  
url='http://aliopentrace.oss-cn-beijing.aliyuncs.com/v2021MicroservicesTraces'

mkdir data
cd data

mkdir Node
mkdir MSResource
mkdir MSRTQps
mkdir MSCallGraph

cd Node

command="wget -c --retry-connrefused --tries=0 --timeout=50 ${url}/node/Node_0.tar.gz"
${command}
