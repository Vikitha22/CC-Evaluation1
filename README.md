Lost and Found Microservices Performance Experiment

===================================================



1\. Project Overview

\-------------------



This project demonstrates the development, deployment, and performance analysis of a containerized microservice-based Lost and Found application.



The existing Lost and Found application is divided into three independent microservices based on their responsibilities:



1\. User Service

2\. Item Service

3\. Handover Service



Each microservice is implemented as an independent PHP application and containerized using Docker. Docker Compose is used to build, deploy, and manage all three services.



The experiment evaluates the performance of the application under different concurrent workloads by measuring response time, throughput, failed requests, CPU utilization, and memory utilization.





2\. Objectives

\-------------



The objectives of the experiment are:



\- To divide the Lost and Found application into independent microservices.

\- To implement REST API endpoints for the individual services.

\- To containerize each microservice using Docker.

\- To deploy the services using Docker Compose.

\- To establish communication between services through a Docker network.

\- To verify end-to-end communication between multiple services.

\- To evaluate application performance under varying workloads.

\- To measure response time and throughput.

\- To monitor CPU and memory utilization.

\- To analyze the effect of increasing concurrent workloads on system performance.





3\. Microservice Architecture

\----------------------------



The application consists of three independent services.





3.1 User Service

\----------------



Responsibility:



Handles user-related functionality and provides the User Service REST API.



Container:



lostfound-user



Host Port:



8081



API Endpoint:



http://localhost:8081/





3.2 Item Service

\----------------



Responsibility:



Handles lost and found item-related functionality and provides the Item Service REST API.



The Item Service also communicates with the User Service and Handover Service through the Docker network.



Container:



lostfound-item



Host Port:



8082



API Endpoint:



http://localhost:8082/





3.3 Handover Service

\--------------------



Responsibility:



Handles the handover and return process and provides the Handover Service REST API.



Container:



lostfound-handover



Host Port:



8083



API Endpoint:



http://localhost:8083/





4\. Technology Stack

\-------------------



Programming Language:



PHP 8.2



Web Server:



Apache



Containerization:



Docker



Container Orchestration:



Docker Compose



Workload Testing:



ApacheBench



Performance Monitoring:



Docker Stats



Data Processing and Graph Generation:



Python and Matplotlib



Operating Environment:



Windows with XAMPP and Docker Desktop





5\. Project Structure

\--------------------



lostfound-microservices/



&#x20;   docker-compose.yml



&#x20;   generate\_graphs.py



&#x20;   README.md



&#x20;   user-service/

&#x20;       Dockerfile

&#x20;       index.php



&#x20;   item-service/

&#x20;       Dockerfile

&#x20;       index.php



&#x20;   handover-service/

&#x20;       Dockerfile

&#x20;       index.php



&#x20;   results/

&#x20;       workload\_results.csv

&#x20;       response\_time.png

&#x20;       throughput.png

&#x20;       cpu\_utilization.png

&#x20;       memory\_utilization.png





6\. Docker Configuration

\-----------------------



Each microservice has its own Dockerfile.



The services use the PHP 8.2 Apache base image.



Each Dockerfile copies the corresponding service application into the Apache document root and exposes port 80 inside the container.



The host ports are mapped as follows:



User Service:



8081 -> 80



Item Service:



8082 -> 80



Handover Service:



8083 -> 80





7\. Docker Compose Configuration

\-------------------------------



Docker Compose is used to build and deploy all three services.



The services are connected to a common Docker bridge network named:



lostfound-network



The Docker Compose configuration provides:



\- Independent containers for each service

\- Port mapping for external access

\- A common network for inter-service communication

\- Independent service deployment





8\. Building and Deploying the Application

\------------------------------------------



Navigate to the project directory:



&#x20;   cd C:\\xampp2\\htdocs\\lostfound-microservices



Build the Docker images:



&#x20;   docker compose build



Start the services:



&#x20;   docker compose up -d



Verify the running containers:



&#x20;   docker ps



The expected containers are:



&#x20;   lostfound-user

&#x20;   lostfound-item

&#x20;   lostfound-handover





9\. REST API Verification

\------------------------



The individual services can be tested using a web browser or an API client.



User Service:



&#x20;   http://localhost:8081/



Item Service:



&#x20;   http://localhost:8082/



Handover Service:



&#x20;   http://localhost:8083/





10\. Inter-Service Communication

\-------------------------------



The services communicate through the Docker bridge network.



The Item Service communicates with the User Service and Handover Service using Docker Compose service names rather than localhost.



The communication is implemented using:



&#x20;   http://user-service/



and:



&#x20;   http://handover-service/



The end-to-end request flow is:



&#x20;   Client

&#x20;      |

&#x20;      v

&#x20;   Item Service

&#x20;      |

&#x20;      +----------------> User Service

&#x20;      |

&#x20;      +----------------> Handover Service



When the Item Service is accessed, it sends requests to the User Service and Handover Service and includes their responses in the resulting JSON response.



The communication was successfully verified through an end-to-end API request.





11\. Workload Testing Methodology

\--------------------------------



ApacheBench was used to generate controlled workloads against the Item Service.



The command format used was:



&#x20;   ab -n 100 -c <concurrency> http://localhost:8082/



Where:



&#x20;   -n 100



represents the total number of requests.



&#x20;   -c



represents the number of concurrent requests.



Five workload levels were evaluated:



&#x20;   1 concurrent request

&#x20;   2 concurrent requests

&#x20;   4 concurrent requests

&#x20;   8 concurrent requests

&#x20;   16 concurrent requests



For each workload level, the following measurements were recorded:



\- Average response time

\- Throughput

\- Failed requests

\- CPU utilization

\- Memory utilization





12\. Resource Monitoring

\-----------------------



Docker container resource utilization was measured using:



&#x20;   docker stats --no-stream



The following metrics were recorded for each service:



\- CPU utilization

\- Memory utilization



Measurements were collected for:



\- User Service

\- Item Service

\- Handover Service





13\. Performance Results

\-----------------------



The measured performance results are shown below.



| Concurrent Requests | Average Response Time (ms) | Throughput (req/s) | Failed Requests |

|---------------------|-----------------------------|--------------------|-----------------|

| 1                   | 4.817                       | 207.59             | 0               |

| 2                   | 4.724                       | 423.35             | 0               |

| 4                   | 6.332                       | 631.76             | 0               |

| 8                   | 14.116                      | 566.73             | 0               |

| 16                  | 24.594                     | 650.55             | 0               |





14\. Resource Utilization Results

\--------------------------------



The recorded CPU and memory utilization values are shown below.



| Concurrent Requests | Item CPU | Item Memory | Handover CPU | Handover Memory | User CPU | User Memory |

|---------------------|----------|-------------|--------------|-----------------|----------|-------------|

| 1                   | 0.00%    | 16.72 MiB   | 0.01%        | 18.84 MiB       | 0.01%    | 16.17 MiB   |

| 2                   | 0.01%    | 16.26 MiB   | 0.01%        | 19.08 MiB       | 0.01%    | 16.90 MiB   |

| 4                   | 0.01%    | 16.41 MiB   | 0.01%        | 19.55 MiB       | 0.01%    | 17.39 MiB   |

| 8                   | 0.01%    | 16.57 MiB   | 0.01%        | 20.27 MiB       | 0.01%    | 17.61 MiB   |

| 16                  | 0.01%    | 16.51 MiB   | 0.01%        | 20.50 MiB       | 0.01%    | 18.08 MiB   |





15\. Performance Analysis

\------------------------



The workload measurements show that average response time generally increased as the number of concurrent requests increased.



At one concurrent request, the average response time was 4.817 ms. At sixteen concurrent requests, it increased to 24.594 ms.



Throughput increased from 207.59 requests per second at one concurrent request to 631.76 requests per second at four concurrent requests.



At eight concurrent requests, throughput decreased to 566.73 requests per second while response time increased to 14.116 ms.



At sixteen concurrent requests, throughput increased again to 650.55 requests per second. However, the average response time also increased to 24.594 ms.



No failed requests were recorded at any of the tested workload levels.



The CPU utilization observed in the Docker statistics remained between 0.00% and 0.01% for the three services during the recorded measurements.



Memory utilization showed a gradual increase with workload. The Handover Service recorded the highest memory usage among the three services, reaching 20.50 MiB at sixteen concurrent requests.





16\. Performance Graphs

\----------------------



The following graphs were generated from the measured workload data.





16.1 Concurrent Requests vs Average Response Time

\-------------------------------------------------



!\[Concurrent Requests vs Average Response Time](results/response\_time.png)



The graph shows the relationship between the number of concurrent requests and the average response time.





16.2 Concurrent Requests vs Throughput

\--------------------------------------



!\[Concurrent Requests vs Throughput](results/throughput.png)



The graph shows the throughput achieved at different workload levels.





16.3 Concurrent Requests vs CPU Utilization

\-------------------------------------------



!\[Concurrent Requests vs CPU Utilization](results/cpu\_utilization.png)



The graph compares CPU utilization of the User Service, Item Service, and Handover Service under different workload levels.





16.4 Concurrent Requests vs Memory Utilization

\----------------------------------------------



!\[Concurrent Requests vs Memory Utilization](results/memory\_utilization.png)



The graph compares memory utilization of the User Service, Item Service, and Handover Service under different workload levels.





17\. Result Data

\---------------



The complete measured workload data is stored in:



&#x20;   results/workload\_results.csv



The CSV file contains:



\- Concurrent requests

\- Response time

\- Throughput

\- Failed requests

\- Item Service CPU utilization

\- Item Service memory utilization

\- Handover Service CPU utilization

\- Handover Service memory utilization

\- User Service CPU utilization

\- User Service memory utilization





18\. Graph Generation

\--------------------



The graphs are generated using the Python script:



&#x20;   generate\_graphs.py



Run the script using:



&#x20;   python generate\_graphs.py



The script reads:



&#x20;   results/workload\_results.csv



and generates the following graphs inside the results directory:



&#x20;   response\_time.png

&#x20;   throughput.png

&#x20;   cpu\_utilization.png

&#x20;   memory\_utilization.png





19\. Experimental Observations

\-----------------------------



The experiment demonstrates that the containerized microservice application successfully handled all five tested workload levels without request failures.



As concurrency increased, the average response time generally increased.



Throughput increased significantly from one to four concurrent requests and showed variation at higher workload levels.



Memory usage increased gradually with workload.



The Handover Service recorded the highest memory utilization among the three services during the recorded measurements.



The observed CPU utilization remained very low for all three services in the recorded Docker statistics.





20\. Conclusion

\--------------



The Lost and Found application was successfully structured as a three-service microservice application consisting of the User Service, Item Service, and Handover Service.



Each service was independently containerized using Docker and deployed using Docker Compose.



A common Docker network was established to enable communication between the services. Inter-service communication was successfully demonstrated by allowing the Item Service to communicate with both the User Service and Handover Service using Docker service names.



The application was evaluated using five workload levels ranging from one to sixteen concurrent requests. Response time, throughput, failed requests, CPU utilization, and memory utilization were measured.



The results demonstrate the effect of increasing workload on application response time, throughput, and memory utilization.



All tested requests completed successfully, with zero failed requests across the five workload levels.





21\. Project Deliverables

\-----------------------



The project contains:



\- Three independent microservices

\- Three Dockerfiles

\- Docker Compose configuration

\- REST API endpoints

\- Docker network configuration

\- Inter-service communication

\- Workload testing results

\- CPU and memory observations

\- Processed CSV results

\- Performance graphs

\- Performance analysis

\- Experimental conclusion





22\. Verification Commands

\-------------------------



Check Docker version:



&#x20;   docker --version



Check Docker Compose:



&#x20;   docker compose version



Build services:



&#x20;   docker compose build



Start services:



&#x20;   docker compose up -d



Check running containers:



&#x20;   docker ps



Check Docker networks:



&#x20;   docker network ls



Monitor container resources:



&#x20;   docker stats --no-stream



Run a workload test:



&#x20;   C:\\xampp2\\apache\\bin\\ab.exe -n 100 -c 1 http://localhost:8082/



Generate performance graphs:



&#x20;   python generate\_graphs.py

