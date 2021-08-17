# Perth City Properties

![perth city](static/images/PerthCity.png)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Introduction](#Introduction)
- [Structure](#Structure)
- [Setup](#Setup)
- [Analysis](#Analysis)
- [Contributors](#Contributors)
- [Technology](#Technology)

## Introduction

Project Outline:

To create a visualised data on real estate properties in the City of Perth. This includes suburbs - Crawley, East Perth, Nedlands, Northbridge, Perth, and West Perth. We also want to assist future buyers and investors to be able to predict the future property price.

ETL Process: 

Scraped Data from the data source sites and filled some missing data manually to ensure data integrity. 
Cleaned the data by removing N/A and converted data types, combined all the data of the suburbs into a single data frame.
Load data onto SQLite and retrieve SQL data in Flask file to create the API.  

Scope:

Properties meaning residential properties which includes Unit, Apartments, Townhouses, Houses.
Rent column implies that the property has been advertised and has been rented out in at the time of the Rent Date. Rent with 0 dollars value have not been advertised for Rental and will have Rent Date of 01/01/1900.

Functionality:

To have a website deployed on Heroku which contain at least 3 pages – Dashboard, Property Price Estimation, and About page. The Dashboard will contain an interactive Tableau Story. The Property Price Estimation page will have an interactive page requiring user inputs with a Machine Learning backend to predict the property prices. The page will also contain a Leaflet map to pinpoint the address of the property.  The About page will contain information regarding the dataset and the project. 



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
