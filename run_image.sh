#!/bin/bash

docker run --gpus all --rm -it -v $(pwd)/output:/workspace/output llm-crash-analysis
