# PAMLpython for Genetic Selection
This repository contains documentation and examples of how to generate an omega value using MUSCLE, phyML, and CodeML given a collection of nucleotide sequences with corresponding species names.

## Description
A difficulty we found this year in attempting to work through the process above was a discontinuity between the outputs of MUSCLE/phyML and the necessary inputs for CodeML, resulting in an overly complicated and, at times, disjointed workflow. The formatting necessary to use all three technologies is specific and not always obvious or clearly outlined in all documentation. Thus, we decided it would be advantageous to complile a guide for use in the future of the lab when trying to duplicate the pipeline. The process_guide.md file outlines all steps necessary to go from nucleotide sequences to an omega value with CodeML output in the terminal. We hope that these instructions will also people helpful for people with little background in computing. The documentation also explains how to set up a terminal that may have nothing previously installed since the pipeline requires pip, python3, biopython, and PAML.

## Getting Started
Please follow the instructions (in order) found in the file process_guide.md.

### Dependencies

### Installing

#### Prerequisites
* python3: you may need to update or install python3 using homebrew (/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" in the terminal followed by "brew install python3")
* pip: in the terminal run "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py" and "python get-pip.py"

#### PAMLpython locally
* Clone this repository to a local directory by entering `cd ~/Desktop; git clone https://github.com/ajlopatkin/paml_pipeline.git` in terminal. You can also choose to download an archive of this repo and unzip it into your local directory.

### Executing program
Follow the setup instructions found in process_guide.md before typing "python3 paml_py.py in the directory containing all relevant files (alignment, tree, control, paml_py.py). As a note, both biopython and PAML must be installed to run the python file.

## Authors

Emily Huntsman (Barnard '21)  
Allison Lopatkin (https://lopatkinlab.com)  
with guidance from Jonathan Snow (https://sites.google.com/a/barnard.edu/jonathansnow/home)

## Version History

* 0.1
    * May 2021

## License
