### Procedure
#### Step 1: 
The Jupyter Notebook [GenerateMolecules_v2.ipynb](../main/GenerateMolecules_v2.ipynb) is execute in a Google Collab environment to generate ligand candidates. The ouptut is caputed into a csv file and depuded using excel or similar spreadsheet. The deduped version is available in [generated_molecules_deduped.csv](../main/generated-molecules/generated_molecules_deduped.csv)

#### Step 2:
[convert.sh](../main/convert.sh) program is executed to take the generated molecules in [generated_molecules_deduped.csv](../main/generated-molecules/generated_molecules_deduped.csv) and transform it into a datastructure that *deepchem* can consume. This involves:
  * Converting the SMILE String for each candidate into SDF format using *babel*.
  * Storing the SMILE String and the SDF file into an unique directory for the candidate with as an appropriately named file.
  * Copying the pdb file for the protein also into the directory as an appropriately named file.

A sample of this structure can be seen in the [testdata](../main/testdata) directory. The full set is available as three fragments of an archive file. See the [Recreating testdata.tar.gz][1] below on how the original archive can be recreated from the fragments.

#### Step 3:



### [1]: Recreating testdata.tar.gz
The *testdata* folder exceeds the 1000 files limit imposed by github. Hence an archive with the full content of *testdata* is included. To recreate the archive use the command below to merge the split files.
```
cat testdata.tar.gz.?? > testdata.tar.gz
```
