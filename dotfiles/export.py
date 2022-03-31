#!/usr/bin/python

# Konstantin Zaremski - April 22, 2021
# -- This script 'packages' the config files from the manifest into the repository

# Import modules
import os

# Read in manifest file
print('\nExporting Configuration Files...')
with open('./configs/manifest.txt') as configManifest:
    configs = configManifest.readlines()
for config in configs:
    current = config.rstrip().split(' ')
    outputName = current[0]
    inputPath = current[1]
    # Copy and notift
    os.system('cp ' + inputPath + ' ./configs/' + outputName);
    print('  ' + inputPath + ' --> ./configs/' + outputName);

print('DONE!\n')
