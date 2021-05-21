# @author Emily Huntsman BC'21
# under the guidance of Professors Jon Snow and Allison Lopatkin
# @version May 20, 2021

from Bio.Phylo.PAML import codeml
import os

# below insert the names of your alignment and tree files
cml = codeml.Codeml(
    alignment="IRE_NT.phylip",
    tree="IRE_NT.trees",
    out_file="results.out",
    working_dir=os.path.abspath(""),
)

# specifications from Professor Lopatkin reflected in codeml.ctl but can be adjusted according to the PAML manual
cml.read_ctl_file("codeml.ctl")
cml.print_options()

# change command to reflect the path to your paml executable
# this can be found by navigating through your directory structure and into paml4.8/bin and typing pwd (print working directory) in the command line
results = cml.run(command="/Users/annhuntsman/Desktop/PAML_Python/paml4.8/bin/codeml",verbose=True)

# if prompted in the terminal respond accordingly (usually pressing enter)

# omega for selection value
print("omega: "+str(results['NSsites'][0]['parameters']['omega']))
