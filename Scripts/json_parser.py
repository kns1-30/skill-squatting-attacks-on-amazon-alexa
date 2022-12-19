import json
import os
import pandas as pd

cols = ["Expected Output", "Actual Output", "File name", "Parsed Json file"]
csv_file_path = os.path.join(os.getcwd(), "failed_words.csv")
if not os.path.isfile(csv_file_path):
    cols = ["Expected Output", "Actual Output", "File name", "Parsed Json file"]
    df=pd.DataFrame([],columns=cols)
    df.to_csv(csv_file_path,index=False)

df = pd.read_csv(csv_file_path)
# updating the column value/data


for file in os.listdir(os.path.join(os.getcwd(), "JSON\\")):

    f = open(os.path.join(os.getcwd(), "JSON\\", file))

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data["testCases"]:
        #print(i)
        if i["status"] == "FAILED":
            # print("Expected", i["annotation"]["expectedTranscription"])
            # print("Output ", i["output"]["transcription"])
            # print("File Name",i["annotation"]["filePathInUpload"])
            try:
                df = pd.concat([df,pd.DataFrame([[i["annotation"]["expectedTranscription"], \
                                                i["output"]["transcription"], \
                                                i["annotation"]["filePathInUpload"], file]], columns=cols)])

            except TypeError:
                df = pd.concat([df,pd.DataFrame([[i["annotation"]["expectedTranscription"], \
                                                "null", \
                                                i["annotation"]["filePathInUpload"], file]], columns=cols)])
df.to_csv(csv_file_path, index=False)