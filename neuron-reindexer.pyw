import json
from tkinter.filedialog import askopenfilename as search_file

with open(path := search_file(), "r") as jsontext:
    jsondict = json.load(jsontext)
    for i, Node in enumerate(jsondict["brain"]["Nodes"]):
        Node["Index"] = i
    with open(path, "w") as file:
        json.dump(jsondict, file)
