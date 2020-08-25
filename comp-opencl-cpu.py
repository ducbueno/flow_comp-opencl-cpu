#!/usr/bin/env python3

import os
import re
import random
import subprocess

fs = list()
for root, dirs, files in os.walk('/hdd/Tools/opm/opm-tests'):
    for f in files:
        if f.endswith('.DATA'):
            fs.append(os.path.join(root, f))

pattern_model = "__(.*?)\."
ran_models = os.listdir('./data')
ran_models = [re.search(pattern_model, r).group(1) for r in ran_models]

tmp = fs
for r in ran_models:
    for f in tmp:
        if r in f:
            fs.pop(fs.index(f))

cmd = '/hdd/Tools/opm/opm-simulators/build/bin/flow'
gpuMode = ['opencl', 'none']
wellContribs = '--matrix-add-well-contributions=false'

random.shuffle(fs)
fnull = open(os.devnull, 'w')
for f in fs:
    for g in gpuMode:
        print(f + ' (' + g + ')')
        subprocess.run([cmd, f, '--gpu-mode=' + g, wellContribs], stdout=fnull)

        prt_fname = f.split('.')[0] + '.PRT'
        new_prt_fname = os.getcwd() + "/data/" + g + "__" + os.path.basename(prt_fname)
        os.rename(prt_fname, new_prt_fname)
