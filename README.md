# Executable Creation

pyinstaller [--onefile] [-w] filename.py

Here: -w stops console from running

Creates: dist and build folders (dist is the only file we really need)
- if it has dependencies, should be in same folder as them

Uses NSIS to create into an application (using a zipped folder)