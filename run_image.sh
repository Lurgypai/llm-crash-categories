#!/bin/bash

docker run --rm -it -v $(pwd)/output:/workspace/output llm-crash-analysis
