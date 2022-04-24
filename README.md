### Recreating testdata.tar.gz
The *testdata* folder exceeds the 1000 files limit imposed by github. Hence an archive with the full content of *testdata* is included. To recreate the archive use the command below to merge the split files.
```
cat testdata.tar.gz.?? > testdata.tar.gz
```
