# GrubhubDataCleaning

## Goal: clean data to make it representable.

### Description:

* Extract data from GrubHub's API. This data is in the grubhub_neu_data.json file.
* Use this as static data to train a model to give out dish recommendations based on what dishes the restaurants have.
* There is a lot of unnecessary data in this file, like delivery fees, store contact information ....
* Clean this data and extract data related to the restaurant's name, location and dishes.
* Dishes should have the dish's name, description (if any), and an image of the dish (if any).

### Tools Used (Extracting Data)

* **<Proxyman (IOS app)>**, use SSH proxying to get relevant API endpoints.
* **<Python (Requests)>**, use the get method to get the JSON data.
* **<Python (JSON)>**, convert data (from dictionary to JSON) to write to the output file.
* **<NOTE>** this process is not shown due to the usage of an authetication key, which is private to me.

### Tools Used (Cleaning Data)

* **<[JSON Pretty Print](https://jsonformatter.org/json-pretty-print)>**, use this to see how the data is formatted, and to extract the relevant data.
* **<Python (JSON)>**, use this to load the data as a dictionary, for extraction.
  
