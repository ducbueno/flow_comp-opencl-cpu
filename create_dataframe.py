#!/usr/bin/env python3

import os
import re
import pandas as pd

features = ['nnzb', 'SolverTime', 'AssemblyTime', 'LinearSolveTime', 'NewtonIterations', 'LinearIterations']*2
modes = ['opencl']*6 + ['none']*6
df = pd.DataFrame(columns=pd.MultiIndex.from_tuples(zip(modes, features)))

fs = os.listdir('./data')
fs = ['./data/' + f for f in fs]

for f in fs:
    with open(f) as infile:
        pattern_g = "(?s:.*)/(.*?)__"
        pattern_model = "__(.*?)\."
        g = re.search(pattern_g, f).group(1)
        model = re.search(pattern_model, f).group(1)

        for line in infile:
            if 'nnzb:' in line:
                df.loc[model, (g, 'nnzb')] = int(line.split()[-1].strip())
            if line.startswith('Solver time (seconds)'):
                df.loc[model, (g, 'SolverTime')] = float(line.split()[-1].strip())
            if line.startswith('Assembly time (seconds):'):
                df.loc[model, (g, 'AssemblyTime')] = float(line.split()[3])
            if line.startswith('Linear solve time (seconds):'):
                df.loc[model, (g, 'LinearSolveTime')] = float(line.split()[4])
            if line.startswith('Overall Newton Iterations:'):
                df.loc[model, (g, 'NewtonIterations')] = int(line.split()[3])
            elif line.startswith('Overall Linear Iterations:'):
                df.loc[model, (g, 'LinearIterations')] = int(line.split()[3])

        infile.close()

df.to_csv('./sim_data.csv', index=True, header=True)
