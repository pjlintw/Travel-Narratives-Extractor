#!/bin/bash


# copy MAXCOUNT files from each directory


MAXCOUNT=5

for category in $( ls THUCNews); do
  echo item: $category

  dir=THUCNews/$category
  newdir=data/thucnews/$category
 
  mkdir -p $newdir
  # if [ -d $newdir ]; then
  #   rm -rf $newdir
  #   mkdir -p $newdir
  # fi

  COUNTER=1

  for i in $(ls $dir); do
    cp $dir/$i $newdir
    if [ $COUNTER -ge $MAXCOUNT ]
    then
      echo finished
      break
    fi
    let COUNTER=COUNTER+1
  done

done

