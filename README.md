# RescueAnimal
CS 340-Python and MongoDb
## About the Project
This project is a Python-based dashboard for Grazioso Salvare (a company that identifies dogs well suited for search-and-rescue training) as part of the CS 340 course at Southern New Hampshire University. It expanded on a previously developed CRUD application by adding an interactive dashboard using Dash framework. The dashboard allows users to filter the data from a MongoDB database which came from a non-profit organization out of Austin, Texas. 

## Motivation
This project is to help understand how to build a front-end application that incorporates a backend from MongoDB, which can be filtered and displayed in a user friendly interface. The goal is to provide Grazioso Salvare with an application to filter animals based on their rescue mission criteria. (Water, Mountain/Wilderness, or Disaster/Tracking).

## Getting Started
1. Ensure MongoDB is installed and running locally or accessible remotely.
2. Create a database and collection:
   - Database name: AAC
   - Collection name: animals
3. Configure authentication:
   - Username: aacuser
   - Password: password1
4. Clone or copy the dashboard `.ipynb` file and the `animal_shelter.py` CRUD module from Project One.
5. Run the project in Jupyter Notebook.

## Installation
Libraries and tools used:
- Python 3 – Main development language
- Dash – For building the interactive web dashboard (`pip install dash`)
- JupyterDash – Used for testing and ensuring functionality
- dash-leaflet – For map visualizations (`pip install dash-leaflet`)
- pandas – For data manipulation (`pip install pandas`)
- plotly– For pie chart generation (`pip install plotly`)
- base64– To embed the Grazioso logo in the layout
- MongoDB – NoSQL database for flexible schema querying

## Usage
- Use the radio buttons to select one of the three mission types or reset:
•	Water Rescue
•	Mountain or Wilderness Rescue
•	Disaster or Individual Tracking
•	Reset (shows all records)
- View the results in the interactive data table
- See animal breed distribution in the pie chart
- See geo-location of the selected animal on the map

## MongoDB Query Example:
rescue_criteria = {
    "Water Rescue": {
        "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]},
        "sex_upon_outcome": "Intact Female",
        "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
    },
    ...
}

