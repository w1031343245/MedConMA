import sys
sys.path.append("./MedConMA/")
from prompt.prompt import *
import re
from multiagents.gpt_api.chatgpt_api import *


def extract_accuracy(text):
    # 正则表达式匹配模式，匹配0.0到1.0之间的数值
    pattern = r'\b0(?:\.\d+)?|1(?:\.0+)?\b'
    matches = re.findall(pattern, text)

    if matches:
        return matches[-1]
    else:
        return 0

def answer(domain: str, question: str):
    
    prompt = ExpertFirstAnswer(domain, question)
    msg = chat_with_gpt(prompt)

    return msg

def NewPrint(name, profile, msg):
    print("\n********************************\n")
    print("%s(%s) todo Analyse" % (name, profile))
    print("\n********************************\n")
    print(msg)
    print("\n********************************\n")

class Expert():
    name: str
    profile: str
    domain: str
    question: str  
    option:str
    context: str

    def __init__(self, name: str, profile: str, domain:str, question: str, option:str) -> None:
        self.name = name
        self.profile = profile
        self.domain = domain
        self.question = question
        self.option = option

    def run(self):
        msg = answer(self.domain, self.question + self.option)

        NewPrint(self.name, self.profile, msg)

        accuracy = extract_accuracy(msg)
        self.context = str(self.profile) + ":" + str(msg) + "\n"
        n:int = 4
        while(float(accuracy) < 0.9 and n >0):
            n = n - 1
            prompt = Knowledge_Obtain(self.question,self.context)
            msg = chat_with_gpt(prompt)

            NewPrint("LLM", "Supplementer", msg)

            self.context = self.context + "\nadditional information:" + str(msg) + "\n"

            msg = chat_with_gpt(ExpertAnswer(self.domain,self.question,msg))
            self.context = self.context + str(self.profile) + ":" + str(msg) + "\n"

            NewPrint(self.name, self.profile, msg)

            accuracy = extract_accuracy(msg)

            if accuracy == 0.0 : self.context = ""

        self.context = self.context + str(self.profile) + ":" + str(msg)

        return msg

