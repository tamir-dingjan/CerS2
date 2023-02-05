#!/usr/bin/env python3

import glob
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np


def get_site_volume(filepath):
    store = False
    with open(filepath, 'r') as infile:
        for line in infile.readlines():
            if store:
                store = False
                return float(line.split()[3])
                
            if "Dscore" in line:
                store = True
                continue


def get_all_site_volumes(files):
    time = [get_time_from_filename(x) for x in files]
    volume = [get_site_volume(x) for x in files]
    return time, volume


def get_time_from_filename(filename):
    title = os.path.splitext(os.path.basename(filename))[0]
    time = int(title.split("crop")[-1].split("_")[0])
    simulation_name = title.split("_")[0]
    # Shift md1 filenames forward by 500 timesteps
    if simulation_name == "md1":
        time += 500
    return time


def plot_site_volumes(names, times, vols, outfile):
    sns.set(style="ticks", context="notebook")
    plt.figure(figsize=(5,2))
    
    cmap = ["#92bfb1", "#533747", "#f3be7c"]

    for i, (t, v) in enumerate(zip(times, vols)):
        plt.scatter(t, v, s=10, marker="+", edgecolor="white", linewidth=1, c=cmap[i])
        
    plt.xlim(0,1000)
    plt.xlabel("Time (ns)")
    
    plt.ylabel(r'Site volume ($\AA^3$)')
    
    plt.savefig(outfile, dpi=300, format="png", bbox_inches="tight")
    plt.show()


workdir = "../sitemaps/"
sites = ["coa", "acyl", "sph"]

times = []
vols = []

for site in sites:
    t, v = get_all_site_volumes(glob.glob(os.path.join(workdir, "*"+site+".log")))
    times.append(t)
    vols.append(v)

plot_site_volumes(sites, times, vols, os.path.join(workdir, "site_vols.png"))

for site_i, site in enumerate(sites):
    print("Site: ", site, "\t Average volume: ", np.mean([x for x in vols[site_i] if x != None]))

print("All done!")
