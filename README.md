# Marvel API Data Integration and Visualization

## Introduction
This project focuses on the integration and automation of data extraction from the Marvel API using Docker, InfluxDB, and Grafana. The primary goal is to create a real-time data visualization system, leveraging the flexibility and capabilities of these tools.

## Table of Contents
1. [Introduction](#introduction)
2. [Background](#background)
3. [Objectives](#objectives)
4. [Development and Analysis](#development-and-analysis)
    - [Automation with Docker](#automation-with-docker)
    - [Data Extraction](#data-extraction)
    - [Storage in InfluxDB](#storage-in-influxdb)
    - [Integration with Grafana](#integration-with-grafana)
5. [Visualization in Grafana](#visualization-in-grafana)
6. [Conclusions](#conclusions)
7. [References](#references)

## Background
To achieve this project, our group utilized the following tools:
- **APIs**: For flexible and integrative data extraction.
- **Docker**: To create consistent and reproducible development environments.
- **InfluxDB**: A time-series database ideal for real-time data monitoring and analysis.
- **Grafana**: An open-source tool for interactive data visualization and analysis.

## Objectives
The objectives of this project are:
- Extract data from the Marvel API using a Python script.
- Store the obtained data in an InfluxDB database.
- Visualize the stored data using Grafana.
- Automate the entire process using Docker.

## Development and Analysis
### Automation with Docker
Docker ensures the portability and replicability of the environment by encapsulating the Python script, InfluxDB, and Grafana in independent containers, facilitating orchestration and deployment.

### Data Extraction
The Python script performs HTTP requests to the Marvel API, processes the responses, and formats the data for storage in InfluxDB. Error handling and pagination are also managed within the script.

### Storage in InfluxDB
InfluxDB is used to store the extracted data. The script connects to InfluxDB, creates the necessary database, and inserts the formatted data into it.

### Integration with Grafana
Grafana is configured to use InfluxDB as a data source, allowing the creation of interactive dashboards for real-time data analysis and monitoring.

## Visualization in Grafana
### Dashboard Creation
Interactive dashboards are designed to display various graphs obtained from the Marvel API data.

![](/img/dashboard.png)

### Graph 1: Number of New Characters per Year
This graph shows the number of new characters introduced in Marvel comics over the years.

![](/img/graphic1.png)

### Graph 2: Comics Published in 2024 by Writers
This graph displays the number of comics published by various writers in 2024.

![](/img/graphic2.png)

### Graph 3: Number of Characters in Important Events
This graph illustrates the number of characters appearing in significant Marvel events.

![](/img/graphic3.png)

### Graph 4: Available Comics of a List of Characters
This graph shows the number of comics available for a selected list of characters.

![](/img/graphic4.png)

## Conclusions
We have developed a system capable of extracting, storing, and visualizing data from the Marvel API in an automated manner using Docker, InfluxDB, and Grafana. Future improvements could include additional Python script functionalities and new data visualizations in Grafana.

## References
- [Docker Documentation](https://docs.docker.com/)
- [Grafana Documentation](https://grafana.com/docs/grafana/latest/)
- [InfluxDB Documentation](https://docs.influxdata.com/influxdb/v2/)
- [Marvel Developer Portal](https://developer.marvel.com/)
- [MIT Technology Review (2024)](https://www.technologyreview.com/2024/01/15/1086461/outperforming-competitors-as-a-data-driven-organization/)
