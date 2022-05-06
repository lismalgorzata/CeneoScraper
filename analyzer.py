import os
import pandas as pd

print(*[filename.split(".")[0]for filename in os.listdir("./opinions")], sep="\n")

product_number= input("ID: ")

opinions = pd.read_json("opinions/"+product_number+".json")
print(json)