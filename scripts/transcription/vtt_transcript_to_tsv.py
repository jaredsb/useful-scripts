#!/usr/bin/env python3

import argparse
import codecs
from itertools import zip_longest

def convert(filename):

    with codecs.open(filename+'.tsv', 'w', 'utf-8') as w:
        with codecs.open(filename, 'r', 'utf-8') as f:

            data = f.readlines()
            
            if data[0].strip() != "WEBVTT":
                print(f"{filename} does not appear to be a Web VTT file")
                print(data[:6])
                exit(1)
                
            transcript = data[2:]
            
            w.write("Index\tStart Time\tEnd Time\tSpeaker\tTranscript\n")

            for n, block in enumerate(zip_longest(*[iter(transcript)] * 4, fillvalue="\n")):
                block = [x.strip() for x in block]
                index = block[0]
                start_time, end_time = block[1].split(" --> ")
                try:
                    speaker, text = block[2].split(": ")
                except ValueError:
                    speaker = ''
                    text = block[2]

                line=f"{index}\t{start_time}\t{end_time}\t{speaker}\t{text}"
                w.write(line + '\n')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("transcript_file", help="Path to transcript VTT file")
    args = parser.parse_args()

    convert(args.transcript_file)
