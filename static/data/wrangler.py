import csv
import json
import re

def convHelper(xin):
    stripped = xin.strip("%")

    if (stripped):
        xout = float(stripped)
    else:
        xout =  None

    return xout

def categorize(q_num):
    if 1 <= q_num <= 4:
        return "masculinity"
    elif 5 <= q_num <= 16:
        return "lifestyle"
    elif 17 <= q_num <= 23:
        return "work"
    elif 24 <= q_num <= 29:
         return "relationships"

# ----- READING FILE -----
with open("masculinity-survey.csv", mode="r") as f:
    csvfile = csv.reader(f)

    ''' LOGIC
        -> check to see if line[0] contains anything
            -> if Yes, new question (q_idx++)
            -> if No, same question, new row
        -> if same question:
            -> add across dimensions
    '''

    questions = []

    new_q = False
    q_idx = -1 

    for line in csvfile:
        if (line[0]):
            # create new Question object
            questions.append(
                {
                    'question'      : line[0],
                    'category'      : categorize(q_idx+2),
                    'adults'        : {},
                    'age_18-34'     : {},
                    'age_35-64'     : {},
                    'age_65+'       : {},
                    'race_NonWhite' : {},
                    'race_White'    : {},
                    'children_Yes'  : {},
                    'children_No'   : {},
                    'or_Straight'   : {},
                    'or_GayBisex'   : {},
                }
            )
            
            q_idx += 1
            # print(line[0])
        else:
            # print(line)
            # print(len(line)) # .. 12 ( 0 - 11 )
            
            target = line[1]

            questions[q_idx]['adults'][target] = convHelper(line[2])
            questions[q_idx]['age_18-34'][target] = convHelper(line[3])
            questions[q_idx]['age_35-64'][target] = convHelper(line[4])
            questions[q_idx]['age_65+'][target] = convHelper(line[5])
            questions[q_idx]['race_NonWhite'][target] = convHelper(line[6])
            questions[q_idx]['race_White'][target] = convHelper(line[7])
            questions[q_idx]['children_Yes'][target] = convHelper(line[8])
            questions[q_idx]['children_No'][target] = convHelper(line[9])
            questions[q_idx]['or_Straight'][target] = convHelper(line[10])
            questions[q_idx]['or_GayBisex'][target] = convHelper(line[11])

with open("masc_survey_formatted.json", "w") as f:
    json.dump(questions, f) 






        