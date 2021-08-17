# Perth City Properties

![perth city](static/images/PerthCity.png)

## Table of Contents

- [Introduction](#Introduction)
- [Structure](#Structure)
- [Setup](#Setup)
- [Analysis](#Analysis)
- [Contributors](#Contributors)
- [Technology](#Technology)
- [Data Sources](#DataSources)

## Introduction

<b>Project Outline:</b>

To create a visualised data on real estate properties in the City of Perth. This includes suburbs - Crawley, East Perth, Nedlands, Northbridge, Perth, and West Perth. We also want to assist future buyers and investors to be able to predict the future property price.

<b>ETL Process:</b>

Dataset scraped from the data source sites and filled some missing data manually to ensure data integrity. 
Cleaned the data by removing N/A and converted data types, combined all the data of the suburbs into a single data frame.
Load data onto SQLite and retrieve SQL data in Flask file to create the API.  

<b>Scope: </b>

Properties meaning residential properties which includes Unit, Apartments, Townhouses, Houses. This project will only look at landed properties - House, Townhouse & Villa.
Rent column implies that the property has been advertised and has been rented out in at the time of the Rent Date. Rent with 0 dollars value have not been advertised for Rental and will have Rent Date of 01/01/1900.



## Structure
```
 
Perth City Properties
|
|__static/                                    
|     |__ css
|     |__ data                              # Directory for the data files
|     |__ images
|
|__ gitignore file
|__ README.md                               # read me file
                   

```

## Setup

## Analysis

## Contributors

- [Helen Amin](https://github.com/helenamin)
- [FangXuan Foo](https://foofx88.github.io)

## Technology

- ![PythonLogo](static/images/pythonlogo.png)

## DataSources
http://house.speakingsame.com/ 

https://www.onthehouse.com.au/

https://www.propertyvalue.com.au/



