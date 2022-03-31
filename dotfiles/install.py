#!/usr/bin/python

# Konstantin Zaremski - April 22, 2021
# -- This script installs the packages and configuration files for my personal i3 (i3-gaps) setup with vim & my web browser of choice, vivaldi.

# Importing needed modules
import os

# Performing a system update and installing required packages from official repositories
print('\n  -= NOW BEGINNING INSTALLATION OF SUB-DISTRIBUTION =-')
print('Performing System Update (sudo pacman -Syu)')
os.system('sudo pacman -Syu')
print('Installing Packages (sudo pacman -S --needed - < packages.txt)')
os.system('sudo pacman -S --needed - < packages.txt')
print('Installing Google Chrome (pamac build google-chrome)')
os.system('pamac build google-chrome')

# Install vim plug
print('Installing VIP Plug (curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim)');
os.system('curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')

# Read in configuration files from manifest and move to proper locations
print('Installing Configuration Files...')
with open('./configs/manifest.txt') as configManifest:
    configs = configManifest.readlines()
for config in configs:
    current = config.rstrip().split(' ')
    inputFileName = current[0]
    outputFullPath = current[1]
    outputPath = '/'.join(current[1].split('/')[:-1])
    outputPath = '~/' if outputPath == '~' else outputPath
    # Make directory if needed and copy config file to location
    os.system('mkdir -p ' + outputPath)
    os.system('cp ./configs/' + inputFileName + ' ' + outputFullPath)
    print('  ./configs/' + inputFileName + ' --> ' + outputFullPath)

# Placing desktop wallpaper file
print('Placing desktop wallpaper file')
os.system('cp ./wallpaper.jpg ~/Pictures/wallpaper.jpg')

# Installing ohmyzsh
os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')

# Change the shell
print('Changing shell for current user to zsh...')
os.system('chsh -s /bin/zsh')

print('DONE!\n')
