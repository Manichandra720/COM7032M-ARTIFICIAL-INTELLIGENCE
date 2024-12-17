import tkinter as tk
from tkinter import messagebox
from owlready2 import *

# Load the ontology from the local file
onto = get_ontology("26 nov 2024\physics_ontology.owl").load()  # Use the correct file path if needed

# Check if the ontology is loaded
print("Ontology loaded successfully!")

# You can now interact with the ontology
# For example, list all classes:
print("Classes in the ontology:", list(onto.classes()))

# Function to query the ontology
def query_ontology():
    query = entry.get().lower()

    # Check for known concepts in the ontology
    if "force" in query:
        result = "Force is a push or pull on an object that can change its motion."
    elif "energy" in query:
        result = "Energy is the capacity to do work, and it can exist in many forms like kinetic or potential energy."
    elif "motion" in query:
        result = "Motion is a change in the position of an object over time."
    else:
        result = "Sorry, I couldn't find an answer related to your query."
    
    # Display result
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Physics Intelligent Tutoring System")

# Set the window size
root.geometry("400x300")

# Create a label for instructions
label = tk.Label(root, text="Ask a Physics question:", font=("Arial", 14))
label.pack(pady=20)

# Create an entry widget for user input
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Create a button to trigger the query function
query_button = tk.Button(root, text="Get Answer", command=query_ontology, font=("Arial", 12))
query_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=20)

# Run the GUI application
root.mainloop()
