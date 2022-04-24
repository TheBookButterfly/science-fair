### Procedure
#### Step 1: 
The Jupyter Notebook [GenerateMolecules_v2.ipynb](../blob/main/GenerateMolecules_v2.ipynb) is execute in a Google Collab environment to generate ligand candidates. The ouptut is caputed into a csv file and depuded using excel or similar spreadsheet. The deduped version is available in [generated_molecules_deduped.csv](../blob/main/generated-molecules/generated_molecules_deduped.csv)







### Recreating testdata.tar.gz
The *testdata* folder exceeds the 1000 files limit imposed by github. Hence an archive with the full content of *testdata* is included. To recreate the archive use the command below to merge the split files.
```
cat testdata.tar.gz.?? > testdata.tar.gz
```
