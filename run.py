import csv
from dataset.data import MyDataset
from string import punctuation
from multiagents.role.autoselfanswer import *
from multiagents.gpt_api.chatgpt_api import *
from multiagents.role.role import *
import re
import tqdm


def extract_option(text):
    pattern = r'[A-D]'
    matches = re.findall(pattern, text)

    if matches:
        return matches[-1]
    else:
        return None

WW: int = 0

def main():
    dataobj = MyDataset()
    test_range = 300
    

    for idx in tqdm.tqdm(range(test_range), desc = "1 ~ 300"):
        raw_sample = dataobj.get_by_idx(idx) 
        question = raw_sample['question'] if raw_sample['question'][-1] in punctuation else raw_sample['question'] + '?'

        options = raw_sample['options']
        gold_answer = raw_sample['answer_idx']

        result =SelfAnswer(str(question), str(options))

        global WW 

        prompt = MaxVotes(result)

        

        msg = chat_with_gpt(prompt)

        text_answer = extract_option(msg)

        if(text_answer == gold_answer): WW = WW + 1
        
        print("\n***********************\n")
        print(msg)
        print("\n***********************\n")
        print("The selected answer is:\n")
        print(text_answer)
        print("\n***********************\n")
        print("The correct answer is:\n")
        print(gold_answer)
        print("\n***********************\n")
        print("The current accuracy is:")
        print(WW / (idx + 1) * 100)
        print("\n***********************\n")

        da = []
        a = WW / (idx + 1) * 100
        da.append(a)

        with open("./result/output.csv","a",newline='') as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(da)

if __name__ == '__main__':
    main()