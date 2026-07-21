ReadMe Content:
WEEK -1:
Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing

 Project Overview

The Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing is a distributed system designed to collect,
process, and aggregate log messages from multiple clients simultaneously using TCP socket programming. The system utilizes multithreading and 
custom socket slicing techniques to ensure efficient handling of high-volume log streams in real time.

This project demonstrates concepts such as socket programming, parallel processing, thread synchronization, and real-time log monitoring.

---

 Features

* Real-time log collection from multiple clients
* Multi-threaded server for parallel client handling
* Custom socket slicing for efficient data transmission
* Log categorization based on log levels
* Timestamped log entries
* Automatic client connection management
* Scalable architecture for multiple concurrent clients
* Console-based real-time monitoring

---

 Technologies Used

* Python 3.x
* Socket Programming
* Threading
* Queue
* Datetime Module
* JSON (Optional for structured logs)

---

 Project Structure

```
Real-Time-Parallel-Log-Aggregation/
│
├── server.py          # Multi-threaded log aggregation server
├── client.py          # Log generator client
├── aggregator.py      # Log processing module
├── utils.py           # Helper functions
├── logs/
│   └── aggregated.log
├── README.md
└── requirements.txt
```

---

 System Architecture

```
+------------+
|  Client 1  |
+------------+
       |
+------------+
|  Client 2  |
+------------+
       |
+------------+
|  Client N  |
+------------+
       |
       ▼
==========================
 Socket Communication
==========================
       ▼
+---------------------------+
| Multi-Threaded Server      |
| Socket Slicing             |
| Log Aggregation            |
+---------------------------+
       ▼
+---------------------------+
| Aggregated Log File        |
| Real-Time Console Output   |
+---------------------------+
```

---

 Working Process

1. Start the server.
2. Multiple clients establish socket connections.
3. Clients continuously generate log messages.
4. The server creates separate threads for each client.
5. Incoming logs are sliced into packets and reconstructed.
6. Logs are timestamped and categorized.
7. Aggregated logs are displayed on the console and stored in a log file.

---

 Log Levels

* INFO
* DEBUG
* WARNING
* ERROR
* CRITICAL

---

 Installation

Clone the repository:

```bash
git clone <repository-url>
cd Real-Time-Parallel-Log-Aggregation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

 Running the Project

Start the server:

```bash
python server.py
```

Run one or more clients:

```bash
python client.py
```

---

 Sample Output

```
[12:30:11] INFO     Client-1 Connected
[12:30:14] WARNING  CPU Usage High
[12:30:18] ERROR    Database Connection Failed
[12:30:22] INFO     Memory Usage Normal
```

 Advantages

* High-speed log processing
* Supports multiple concurrent clients
* Improved scalability
* Efficient network communication
* Easy to extend and customize
* Real-time monitoring capability

 Applications

* Distributed Systems
* Cloud Infrastructure Monitoring
* Network Monitoring
* Server Log Management
* DevOps Monitoring
* Security Log Analysis
* Microservices Architecture

 Future Enhancements

* Web-based dashboard
* Database integration (MySQL/MongoDB)
* Log filtering and searching
* Authentication and encryption
* Load balancing
* Docker deployment
* REST API support
* Real-time analytics and visualization

 Learning Outcomes

* TCP Socket Programming
* Multithreading in Python
* Parallel Processing
* Client-Server Architecture
* Log Aggregation Techniques
* Real-Time Data Streaming
* Network Communication
* Concurrent Programming

 Conclusion

The Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing provides an efficient solution for collecting and processing logs from multiple 
clients simultaneously. By combining socket programming with multithreading and custom packet slicing, the system ensures reliable, scalable, and real-time 
log aggregation suitable for modern distributed environments.


WEEK -2:
 MapReduce Engine – Online Games Data Analysis

 Project Overview

This project implements a simplified **MapReduce Engine** in Python to analyze online gaming data. The engine follows the MapReduce programming model by splitting large datasets into smaller chunks, processing them in parallel using mapper functions, grouping similar records through partitioning and sorting, and finally producing summarized results using reducers.
The project demonstrates how distributed data processing can efficiently analyze online game records such as game names, player activities, or event occurrences.

Project Objective

The primary objective of this project is to design and implement a basic MapReduce Engine capable of processing online gaming datasets efficiently. The engine simulates the workflow of distributed computing systems by dividing tasks into multiple stages and executing them independently before combining the final results.

 Problem Statement

Online gaming platforms generate millions of records every day. Processing these records sequentially is time-consuming. This project solves the problem by implementing a MapReduce Engine that processes the dataset in parallel and calculates the frequency of each online game in the dataset.

Example Input

```
PUBG
Free Fire
Valorant
PUBG
Minecraft
Valorant
PUBG
BGMI
Minecraft
```

Expected Output

```
PUBG 3
Valorant 2
Minecraft 2
Free Fire 1
BGMI 1
```
 Project Workflow

The MapReduce Engine performs the following stages:

1. Read the input dataset.
2. Split the dataset into smaller chunks.
3. Execute multiple mapper processes.
4. Generate intermediate key-value pairs.
5. Partition mapper outputs using hash partitioning.
6. Sort partition files.
7. Reduce grouped records.
8. Generate the final output.

 Features

- Parallel processing using MapReduce concepts
- Automatic input splitting
- Mapper generation of key-value pairs
- Hash-based partitioning
- Sorting intermediate data
- Reduction of duplicate keys
- Final aggregated output generation
- Modular Python implementation

 Project Structure

```
MapReduce/
│
├── master.py
├── splitter.py
├── mapper.py
├── partitioner.py
├── sorter.py
├── reducer.py
├── input.txt
├── requirements.txt
├── README.md
├── partitions/
└── output/
```

 Module Description

 master.py

Controls the complete execution of the MapReduce Engine by calling every module in sequence.

 splitter.py

Splits the input dataset into equal chunks for multiple mapper processes.

 mapper.py

Reads each chunk and converts every game record into an intermediate key-value pair.

Example

```
PUBG
```

becomes

```
(PUBG,1)
```

 partitioner.py

Uses the hash function

```
hash(key) % number_of_reducers
```

to assign each game to the appropriate reducer.

---

 sorter.py

Sorts partition files alphabetically so identical game names appear together.

---

 reducer.py

Groups identical game names and calculates their total occurrences.

Example

```
PUBG
1
1
1
```

Output

```
PUBG 3
```

Technologies Used

- Python 3
- File Handling
- Hash Partitioning
- Sorting Algorithms
- MapReduce Programming Model

 Installation

Install Python 3.

Install dependencies:

```bash
pip install -r requirements.txt
```

Execution

Run the project using:

```bash
python master.py
```

 Sample Input

```
PUBG
Free Fire
Valorant
PUBG
Minecraft
Valorant
PUBG
BGMI
Minecraft
```

 Sample Output

```
PUBG 3
Valorant 2
Minecraft 2
Free Fire 1
BGMI 1
```

 Applications

- Online game popularity analysis
- Player activity monitoring
- Event log analysis
- Gaming statistics generation
- Large-scale gaming data processing
- Distributed analytics systems

 Advantages

- Faster processing through parallel execution
- Scalable architecture
- Efficient handling of large datasets
- Easy to modify for different datasets
- Modular and reusable design
- Demonstrates distributed computing concepts

 Future Enhancements

- Support multiple reducers dynamically
- Process larger real-time gaming datasets
- Add graphical visualization of results
- Integrate with Hadoop or Apache Spark
- Implement multiprocessing for better performance

 Conclusion

This project successfully demonstrates the implementation of a MapReduce Engine for analyzing online game datasets. The engine efficiently processes large amounts of gaming data by splitting the input, generating intermediate key-value pairs, partitioning and sorting the records, and reducing them to produce accurate game occurrence counts. The modular design allows the engine to be extended for various big data applications beyond online gaming.


