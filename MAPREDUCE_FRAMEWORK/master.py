import os

from splitter import split_data
from mapper import mapper
from partition import partition
from sorter import sort_file
from reducer import reducer

REDUCERS=4

with open("input.txt","r") as file:

    lines=file.readlines()

records=lines[1:]

chunks=split_data(records,REDUCERS)

mapped=[]

for chunk in chunks:
    mapped.extend(mapper(chunk))

partition(mapped,REDUCERS)

for i in range(REDUCERS):
    sort_file(f"partitions/part-{i}.txt")

final={}

for i in range(REDUCERS):

    result=reducer(f"partitions/part-{i}.txt")

    for key,value in result.items():

        final[key]=final.get(key,0)+value

os.makedirs("output",exist_ok=True)

with open("output/result.txt","w") as file:

    file.write("Genre,Players\n")

    for key in sorted(final):

        file.write(f"{key},{final[key]}\n")

print("MapReduce Completed Successfully")

print(final)