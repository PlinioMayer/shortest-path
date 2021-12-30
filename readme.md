# Introduction

A simple script that will check all possible paths between
to points in a given map and output the smallest path.

# Map

The map must be drawed in a text file using '#' to as obstacles. All four
borders must also be filled with '#'. The 'S' marks the starting point and
the 'E' the end point.

Examples:

```
######     ##########
# # E#     #S       #
#S  ##     #### #####
#   ##     #E       #
######     ##########
```

# Running

The script can be started as any Python script `python <path-to-the-script> [,args]`.
From the project directory you may run using `python . [,args]`.

## Arguments

The script accepts only one argument: the path to the txt containing the map.
