#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

data = pd.read_csv(
    "tmd_rmsd.xvg",
    skiprows=18, 
    delim_whitespace=True,
    names=["time", "rmsd"]
)

fig, ax = plt.subplots(figsize=(8.5,2))
sns.set(style="ticks", context="notebook")

plt.plot(data["time"], 10*data["rmsd"], c=sns.xkcd_rgb["ocean blue"], alpha=0.8)

plt.xlabel("Time (ns)")
plt.ylabel(r"Transmembrane RMSD ($\AA$)")

plt.yticks(ticks=[0,1,2,3,4], labels=[0,1,2,3,4])

plt.xticks(ticks=[i for i in range(0, 1000001, 100000)], 
            labels=[i for i in range(0, 1001, 100)])

plt.savefig(os.path.join(workdir, "rmsd_tmd.png"), format="png", bbox_inches="tight", dpi=300)

plt.show()

