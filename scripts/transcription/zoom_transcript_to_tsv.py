#!/usr/bin/env python3

import argparse
import json
import codecs

def convert(filename):

    with codecs.open(filename+'.tsv', 'w', 'utf-8') as w:
        with codecs.open(filename, 'r', 'utf-8') as f:
            data=json.loads(f.read())

            w.write("Index\tStart Time\tEnd Time\tSpeaker\tTranscript\n")

            items = data['results']['items']
            for index, item in enumerate(items):
                content = item['alternatives'][0]['content']
                try:
                    speaker,text = content.split(':')
                except ValueError:
                    speaker = ''
                    text = content
                    
                start_time = item.get('start_time')
                end_time = item.get('end_time')
                line=f"{index}\t{start_time}\t{end_time}\t{speaker}\t{text}"
                w.write(line + '\n')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("transcript_file", help="Path to transcript JSON file (Zoom format)")
    args = parser.parse_args()

    convert(args.transcript_file)
