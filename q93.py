#coding = utf-8

import sys 
from tqdm import tqdm
 
analogy_data = sys.stdin

TRUE_COUNT = 0.0
FALSE_COUNT = 0.0

for line in tqdm(analogy_data):
    words = line.rstrip().split() 
    if len(words) < 6:
        continue
    else:
        if words[3] == words[4]:
            TRUE_COUNT += 1.0
        else:
            FALSE_COUNT += 1.0

print str(TRUE_COUNT/(TRUE_COUNT+FALSE_COUNT)) + " ( " + str(TRUE_COUNT) + " / " + str(FALSE_COUNT) +" ) "



