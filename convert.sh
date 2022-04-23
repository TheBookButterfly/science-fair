#!/bin/bash
input="./generated-molecules/generated_molecules_deduped.csv"
mychars=("a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z")
w=0
x=0
y=0
z=0

function generateName(){
   name=${mychars[$w]}${mychars[$x]}${mychars[$y]}${mychars[$z]}

   ((++z))
   if ((z > 25)); then
      z=0
      ((++y))
   fi
   if ((y > 25)); then
      y=0
      ((++x))
   fi
   if ((x > 25)); then
      x=0
      ((++w))
   fi

}

i=0
while read -r line
do
  generateName
  identity=$name
  echo $identity
  # identity="M-$i"
  filenameSDF=${identity}_ligand".sdf" 
  filenameSMI=${identity}_ligand".smi" 
  filenamePDB=${identity}_protein".pdb"

  mkdir -p testdata/${identity}

  touch testdata/${identity}/${filenameSMI}

  echo ${line} > testdata/${identity}/${filenameSMI}



  obabel -i smi testdata/${identity}/${filenameSMI} -o sdf -O testdata/${identity}/${filenameSDF} --gen3D 

  cp model1.pdb testdata/${identity}/${filenamePDB}

  #echo "id="${identity}", filename="${filename}

  i=$(($i+1))
done < "$input"
