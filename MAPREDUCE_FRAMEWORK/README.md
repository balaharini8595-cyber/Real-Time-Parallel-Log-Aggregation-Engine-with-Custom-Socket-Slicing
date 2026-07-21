 Mini MapReduce Framework for Online Games Analysis

 Project Title

Mini MapReduce Framework for Online Games Genre Analysis using Python

 Project Description

This project implements a simplified MapReduce Framework using Python to analyze an Online Games dataset. The framework processes player records and counts the number of players in each game genre.

The project demonstrates the four major phases of the MapReduce model:

- Split
- Map
- Partition
- Sort
- Reduce

The implementation uses Python file handling and multiprocessing concepts.

 Objectives

- Understand the MapReduce programming model.
- Process game datasets efficiently.
- Count players based on game genres.
- Learn data partitioning techniques.
- Understand reducer aggregation.

 Technologies Used

- Python 3
- Multiprocessing
- File Handling
- Hash Partitioning
- Collections Module

Folder Structure

```
MapReduce_Framework
│
├── master.py
├── splitter.py
├── mapper.py
├── partitioner.py
├── sorter.py
├── reducer.py
├── input.txt
│
├── partitions
│   ├── part-0.txt
│   ├── part-1.txt
│   ├── part-2.txt
│   └── part-3.txt
│
├── output
│   └── result.txt
│
├── requirements.txt
└── README.md
```

 Dataset Information

The input dataset contains Online Game player information.

Each record contains:

- Player ID
- Player Name
- Game Name
- Genre
- Hours Played
- Country

Example

```
1001,Arun,PUBG,Battle Royale,5,India
```

 Project Workflow

```
Input File
     │
     ▼
 Splitter
     │
     ▼
 Mapper
     │
     ▼
 Key-Value Pairs
     │
     ▼
 Partitioner
     │
     ▼
 Intermediate Files
     │
     ▼
 Sorter
     │
     ▼
 Reducer
     │
     ▼
 Final Output
```

 Module Description

 splitter.py

Splits the input dataset into equal chunks.

 mapper.py

Reads each record and extracts the Game Genre.

Example

```
Battle Royale → (Battle Royale,1)
FPS → (FPS,1)
Sandbox → (Sandbox,1)
```

partitioner.py

Distributes mapper outputs into multiple partition files using Hash Partitioning.

Formula

```
hash(key) % number_of_reducers
```

sorter.py

Sorts each partition file alphabetically before reducing.

 reducer.py

Counts all occurrences of each game genre.

 master.py

Controls the complete MapReduce execution process.

 Sample Output

```
Genre,Players

Battle Royale,28
FPS,21
RPG,14
Sandbox,18
Sports,10
Strategy,9
```

 Advantages

- Easy to understand
- Demonstrates distributed computing concepts
- Modular implementation
- Supports large datasets
- Easy to extend

Applications

- Online Gaming Analytics
- Big Data Processing
- Log File Analysis
- Player Statistics
- Gaming Reports
- Data Mining
- Hadoop Learning

 Future Enhancements

- Support multiple input files
- Add GUI
- Use Apache Hadoop
- Generate charts
- Database integration
- Cloud deployment

 How to Run

Open the project folder in VS Code.

Open Terminal.

Run the following command:

```
python master.py
```

The final output will be generated inside:

```
output/result.txt
```

 Expected Output

```
Genre,Players

Battle Royale,28
FPS,21
RPG,14
Sandbox,18
Sports,10
Strategy,9
```

 Conclusion

This project successfully demonstrates the implementation of a Mini MapReduce Framework using Python for Online Games Analysis. It follows the complete MapReduce workflow including data splitting, mapping, partitioning, sorting, and reducing. The project can be further extended for large-scale gaming datasets and distributed computing environments such as Hadoop.

 Developed By

Name : _B.BalaHarini______________________

Department : Bachelor of Computer Applications (BCA)

Academic Project : Mini MapReduce Framework using Python
