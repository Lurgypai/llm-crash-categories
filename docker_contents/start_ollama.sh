#!/bin/bash

ollama serve &> ollama-server.txt &
sleep 1
ollama pull llama3.3
