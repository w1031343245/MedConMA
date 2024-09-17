def ExpertFirstAnswer(domain: str, question: str):
    PROMPT_TEMPLATE: str = """
    You are a medical expert in the domain of {domain}.
    From your area of specialization, you will scrutinize and diagnose the symptoms presented by patients in specific medical scenarios.
    Please meticulously examine the medical scenario outlined in this question: 
    {question}
    Analyze all the options and select the one you think is most appropriate. The options include only A to D.
    You need to complete the following steps:
    1.Carefully read the medical scenario presented in the question.
    2.Scrutinize each option individually to assess whether it is plausible or should be eliminated based on reason and logic.
    3.Pay close attention to discerning the disparities among the different options and rationalize their existence. 
    4.A handful of these options might seem right on the first glance but could potentially be misleading in reality.
    5.Output your analysis of the above steps 1 to 4.
    6.Analyze what additional knowledge you need to further solve this problem. Please relate it to the question and output the extra knowledge required.
    7.Output the answer you consider most appropriate.
    8.Evaluate the accuracy of your answer to this question. The more additional knowledge you need, the lower your accuracy(Accuracy ranges from 0.0 to 1.0.).
    9. You must output the accuracy of your answer to this question(Accuracy ranges from 0.0 to 1.0.).
    """
    
    prompt = PROMPT_TEMPLATE.format(domain = domain, question = question)

    return prompt

def ExpertAnswer(domain:str, question: str,context:str):
    PROMPT_TEMPLATE: str = """
    You are a medical expert in the domain of {domain}.
    From your area of specialization, you will scrutinize and diagnose the symptoms presented by patients in specific medical scenarios.
    Please meticulously examine the medical scenario outlined in this question:
    {question}
    You have received some additional knowledge regarding the question:
    {context}
    Analyze all the options and select the one you think is most appropriate. The options include only A to D.
    You need to complete the following steps:

    1. Carefully read the medical scenario presented in the question.
    2. Scrutinize each option individually to assess whether it is plausible or should be eliminated based on reason and logic.
    3. Pay close attention to discerning the disparities among the different options and rationalize their existence.
    4. A handful of these options might seem right at first glance but could potentially be misleading in reality.
    5. Output your analysis of the above steps 1 to 4.
    6. Analyze what additional knowledge you need to further solve this problem. Please relate it to the question and output the extra knowledge required.
    7. Output the answer you consider most appropriate.
    8.Evaluate the accuracy of your answer to this question. The more additional knowledge you need, the lower your accuracy(Accuracy ranges from 0.0 to 1.0.).
    9. You must output the accuracy of your answer to this question(Accuracy ranges from 0.0 to 1.0.).
    """

    prompt = PROMPT_TEMPLATE.format(domain = domain, question = question, context = context)

    return prompt

def Knowledge_Obtain(question:str, msg: str):
    PROMPT_TEMPLATE: str = """
    You need to strictly follow the following steps to supplement additional knowledge:
    1. First, analyze this answer:
   {msg}
    2. Extract the additional knowledge required in this answer.
    3. In relation to the question:
   {question}
    4. Provide the additional knowledge you have identified:
    """

    prompt = PROMPT_TEMPLATE.format(question = question,msg = msg)

    return prompt

def ClinicalMedicine():
    PROMPT_TEMPLATE: str = "You are an expert in the field of clinical medicine."

    return PROMPT_TEMPLATE

def SpecialistDoctors1():
    PROMPT_TEMPLATE: str = "You are an expert in the field of Specialty Medicine."

    return PROMPT_TEMPLATE

def BasicMedicalDoctor1():
    PROMPT_TEMPLATE: str = "You are an expert in the field of Basic Medical Sciences."

    return PROMPT_TEMPLATE

def ForensicDoctor1():
    PROMPT_TEMPLATE: str = "You are an expert in the field of Forensic Medicine."

    return PROMPT_TEMPLATE

def Anesthesiologist1():
    PROMPT_TEMPLATE: str = "You are an expert in the field of Anesthesiology."

    return PROMPT_TEMPLATE

def Pharmacist1():
    PROMPT_TEMPLATE: str = "You are an expert in the field of Pharmacy."

    return PROMPT_TEMPLATE

def MaxVotes(context: str):
    PROMPT_TEMPLATE: str = """
    You need to strictly follow the following steps to supplement additional knowledge:
    1. First, analyze this text composed by multiple experts:
    {context}
    2. Extract each expert's answer.
    3. Carefully read each expert's answer.
    4. Identify which answer each expert chose.
    5. Output the option chosen the most times(Only output the letter of the option.):
    """

    prompt = PROMPT_TEMPLATE.format(context = context)

    return prompt

def GroupComment(result: str, experience: str):
    PROMPT_TEMPLATE: str = """
    Based on your past problem-solving experience:
    {experience}
    Please comment on the expert's response below:
    {result}
    Praise him and point out his mistakes:
    """

    prompt = PROMPT_TEMPLATE.format(result = result, experience = experience)

    return prompt

def AnswerModify(result:str, comment: str, context: str):
    PROMPT_TEMPLATE: str = """
    The following are the comments from all the experts who answered your questions:
    {comment}
    Here is your answer:
    {result}
    Combining your own experience:
    {context}
    Analyze all the options and select the one you think is most appropriate. The options include only A to D.
    You need to complete the following steps:
    1.Analyze the recommendations from each expert regarding your answer, summarize these recommendations based on your own experience, and keep only the ones you consider correct.
    2.Modify your answer based on the summary generated in the previous step.
    3.Carefully read the medical scenario presented in the question.
    4.Scrutinize each option individually to assess whether it is plausible or should be eliminated based on reason and logic.
    5.Pay close attention to discerning the disparities among the different options and rationalize their existence. 
    6.A handful of these options might seem right on the first glance but could potentially be misleading in reality.
    7.Output your analysis of the above steps 3 to 6.
    8.Output the answer you consider most appropriate.
    9.You must output the accuracy of your answer to this question(Accuracy ranges from 0.0 to 1.0.).
    """

    prompt = PROMPT_TEMPLATE.format(result = result, comment = comment, context = context)

    return prompt

def Question_Analyse(question: str):
    PROMPT_TEMPLATE: str = """
    Analyze the following questions:
    {question}
    identify the knowledge required to answer them, 
    and output the additional knowledge needed:
    """

    prompt = PROMPT_TEMPLATE.format(question = question)

    return prompt

def get_question_domains_prompt(question):
    question_domain_format = "Medical Field: " + " | ".join(["Field" + str(i) for i in range(4)])
    question_classifier = "You are a medical expert who specializes in categorizing a specific medical scenario into specific areas of medicine."
    prompt_get_question_domain = f"You need to complete the following steps:" \
            f"1. Carefully read the medical scenario presented in the question: '''{question}'''. \n" \
            f"2. Based on the medical scenario in it, classify the question into five different subfields of medicine. \n" \
            f"3. You should output in exactly the same format as '''{question_domain_format}'''."
    return question_classifier, prompt_get_question_domain

def get_options_domains_prompt(question, options):
    options_domain_format =  "Medical Field: " + " | ".join(["Field" + str(i) for i in range(3)])
    options_classifier = f"As a medical expert, you possess the ability to discern the two most relevant fields of expertise needed to address a multiple-choice question encapsulating a specific medical context."
    prompt_get_options_domain = f"You need to complete the following steps:" \
                f"1. Carefully read the medical scenario presented in the question: '''{question}'''." \
                f"2. The available options are: '''{options}'''. Strive to understand the fundamental connections between the question and the options." \
                f"3. Your core aim should be to categorize the options into three distinct subfields of medicine. " \
                f"You should output in exactly the same format as '''{options_domain_format}'''"
    return options_classifier, prompt_get_options_domain