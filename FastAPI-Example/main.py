from fastapi import FastAPI
import json

app = FastAPI()             # Initializing the Fast API

subcategory_File = r"C:\Users\gnani\Downloads\DWH_Gpt\Global_Electronics_Retailer\SubCategory.json"                 # File Path

# Load JSON
with open(subcategory_File, "r") as f:
    subcategories = json.load(f)

#print(subcategories)           # View the Json format of the Subcategories file

@app.get("/subcategories")      # get() to fetch the data
def get_subcategories():        # function that returns the subcategories
    return subcategories
