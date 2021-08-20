import pdfplumber
import os
import re
import json
from pprint import pprint
from tqdm import tqdm

all_files = []

for path, subdirs, files in os.walk('bs.pdf'):
    for name in files:
        all_files.append(os.path.join(path, name))

all_files = [x for x in all_files if ('_final.pdf' in x.lower()) or ('_final_report.pdf' in x.lower())]
events = []
for f in tqdm(all_files):
    with pdfplumber.open('bs.pdf') as pdf:
        lines = []
        lines.append(f)
        for page in pdf.pages:
            text = page.extract_text()
            text = text.split('\n')
            for line in text:
                if 'location: ' in line.lower() or \
                'rpt #:' in line.lower() or \
                'unit:' in line.lower() or \
                'channel:' in line.lower() or \
                'code:' in line.lower() or \
                'response:' in line.lower() or \
                'complaint:' in line.lower() or \
                'nature:' in line.lower() or \
                'business:' in line.lower() or \
                'date/time' in line.lower():
                    lines.append(line.strip())

        events.append(lines)

#100%|██████████| 1726/1726 [09:43<00:00,  3.04it/s]
all_evts = {}
for counter, event in tqdm(enumerate(events[:])):
    evt = {}
    for line in event:
        line = line.strip()

        # --- removed for brevity ---

        match = re.match(r'(Nature:)(.*)(Alarm Lvl:)(.*)(Priority:)(.*)(Event Priority:)(.*)$', line)
        if match:
            evt['nature'] = match.group(2).strip()
            evt['alarm_level'] = match.group(4).strip()
            evt['priority'] = match.group(6).strip()
            evt['event_priority'] = match.group(6).strip()

        # --- removed for brevity ---

        all_evts[counter] = evt

#1726it [00:00, 6206.80it/s]
with open('cad.json', 'w') as outfile:
    json.dump(all_evts, outfile)


