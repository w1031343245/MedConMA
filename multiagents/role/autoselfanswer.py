import sys
sys.path.append("./MedConMA/")
from multiagents.role.role import *
from prompt.prompt import *

def SelfAnswer(
        question: str,
        option: str,
):
    print("\n\n\n**************************************************************\n\n\n")
    Experts : list[Expert] = []

    while len(Experts) < 5:
        Experts.append(None)

    question_role, question_domain = get_question_domains_prompt(question)
    raw_question_domain = chat_with_gpt(question_role, question_domain)
    if raw_question_domain == "ERROR.":
        raw_question_domain  = "Medical Field: " + " | ".join(["General Medicine" for _ in range(3)])
    question_domains = raw_question_domain.split(":")[-1].strip().split(" | ")
    question_domains.append(None)
    question_domains.append(None)
    question_domains.append(None)
    print(question_domains)

    options_role, options_domain = get_options_domains_prompt(question, option)
    raw_option_domain = chat_with_gpt(options_role, options_domain)
    if raw_option_domain == "ERROR.":
        raw_option_domain  = "Medical Field: " + " | ".join(["General Medicine" for _ in range(2)])
    options_domains = raw_option_domain.split(":")[-1].strip().split(" | ")
    options_domains.append(None)
    options_domains.append(None)

    print(options_domains)
    if(question_domains[0] != None):
        Experts[0] = Expert("Alice", "Expert1", question_domains[0], question, option)
    else:
        Experts[0] = Expert("Alice", "Expert1", None, question, option)
    if(question_domains[1] != None):
        Experts[1] = Expert("Bob", "Expert2", question_domains[1], question, option)
    else:
        Experts[1] = Expert("Bob", "Expert2", None, question, option)
    if(question_domains[2] != None):
        Experts[2] = Expert("David", "Expert3", question_domains[2], question, option)
    else:
        Experts[2] = Expert("David", "Expert3", None, question, option)
    if(options_domains[0] != None):
        Experts[3] = Expert("Lili", "Expert4", options_domains[0], question, option)
    else:
        Experts[3] = Expert("Lili", "Expert4", None, question, option)
    if(options_domains[1] != None):
        Experts[4] = Expert("Lisa", "Expert5", options_domains[1], question, option)
    else:
        Experts[4] = Expert("Lisa", "Expert5", None, question, option)

    context: str = ""
    for expert in Experts:
        msg = expert.run()
        context = context + expert.name + ":" + str(msg) + '\n'+ "**************************************************************\n"


    print("\n\n\n*****************The analysis is complete*********************\n\n\n")
    print("\n\n\n**************************************************************\n\n\n")
    print(context)
    print("\n\n\n**************************************************************\n\n\n")
    return context