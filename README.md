### Procedure
#### Step 1: 
The Jupyter Notebook [GenerateMolecules_v2.ipynb](../main/GenerateMolecules_v2.ipynb) is executed in a Google Collab environment to generate ligand candidates. The ouptut is caputed into a csv file and any duplicates are removed using excel. The de-duplicated version is available in [generated_molecules_deduped.csv](../main/generated-molecules/generated_molecules_deduped.csv)

#### Step 2:
[convert.sh](../main/convert.sh) program is executed to take the generated molecules in [generated_molecules_deduped.csv](../main/generated-molecules/generated_molecules_deduped.csv) and transform it into a datastructure that *deepchem* can consume. This involves:
  * Converting the SMILE String for each candidate into SDF format using *babel*.
  * Storing the SMILE String and the SDF file into an unique directory for the candidate in appropriately named files.
  * Copying the pdb file for the protein (available in [model1.pdb](../main/model1.pdb)) also into the directory in an appropriately named file.

A sample of this structure can be seen in the [testdata](../main/testdata) directory. The full set is available as three fragments of an archive file. See the [Recreating testdata.tar.gz](#recreating-testdatatargz) below on how the original archive can be recreated from the fragments.

#### Step 3:
[rundeepchem-docker.sh](../main/rundeepchem-docker.sh) is executed to run a docker container with an installation of *deepchem*. Within the container, the [pdbbind_tf.py](../main/pdbbind_tf.py) is executed to generate a pdb binding affinity model and predit the bindings of the testdata dataset.



### Recreating testdata.tar.gz
The *testdata* folder exceeds the 1000 files limit imposed by github. Hence an archive with the full content of *testdata* is included. To recreate the archive use the command below to merge the split files.
```
cat testdata.tar.gz.?? > testdata.tar.gz
```
