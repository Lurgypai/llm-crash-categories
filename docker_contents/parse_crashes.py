#!/bin/python3
import os
import json
from ollama import chat
from pydantic import BaseModel

class CrashStat(BaseModel):
  category: str
  crashfile: str
  binary: str
  sourcefile: str
  linenumber: int

def main():
    prompt_file = open('/workspace/sys-prompts/prompt.txt', 'r')
    prompt_file_contents = prompt_file.read()
    
    print('prompt contents:', prompt_file_contents)

    all_files = {}

    for file in os.listdir('/workspace/crash-files'):
        print('parsing file', file)
        with open('/workspace/crash-files/' + file) as crash_file:
            crash_file_contents = crash_file.read()

            response = chat(
              messages=[
                {
                  'role': 'user',
                  'content': prompt_file_contents + crash_file_contents,
                }
              ],
              model='llama3.3',
              format=CrashStat.model_json_schema(),
            )

            stat = CrashStat.model_validate_json(response.message.content)
            all_files[file] = stat.model_dump()

    with open('out.json', 'w') as outfile:
        json.dump(all_files, outfile)

if __name__ == "__main__":
    main()
