import json
import sys
from html import unescape
from pathlib import Path


sources = json.loads(Path("source.json").read_text())
answers = json.loads(Path("answer.json").read_text())
start = int(sys.argv[1])
end = int(sys.argv[2])
for source, answer in zip(sources[start:end], answers[start:end]):
    print("\nARTICLE", source["number"])
    print("SOURCE\n" + unescape(source["source_xml"]))
    print("NOTES SOURCE\n" + unescape(source["source_notes_xml"]))
    print("PROPOSITION\n" + answer["proposed_xml"])
