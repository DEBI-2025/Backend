from google import genai
from google.genai import types
import json


import json
import re

def clean_and_parse_gemini_json(response_text):
    """
    Cleans a Gemini-styled response (with ```json blocks and whitespace)
    and returns a parsed Python dictionary.
    """
    # Remove Markdown-style triple backticks and optional language tag (e.g., ```json)
    cleaned = re.sub(r"```(?:json)?", "", response_text, flags=re.IGNORECASE).strip()

    # Remove leading/trailing whitespace and newlines
    cleaned = cleaned.strip()

    # Parse the cleaned string as JSON
    try:
        parsed = json.loads(cleaned)
        return parsed
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        return None



def geminiAPI(api_key,field,level,topic):
    prompt = f"""You are an expert Question Bank generator for software engineering practice. Your task is to generate 10 multiple-choice questions (MCQs) in JSON format, tailored to the user's specifications.
                    User Specifications:
                     Field: {field}
                     Topics: {topic}
                     Question Level: {level}
                    Instructions:
                    1.  Generate 30 Written Question based on the provided field, track, topics, and question level.
                    2.  Ensure all questions are relevant to the specified topics within the given track and field.
                    3.  The question level should accurately reflect the difficulty (entry, intermediate, or advanced).
                    4.  Each question should have a written answer 
                    5.  Return the questions in a JSON with the following structure:
                    {{
                    "questions": [
                        {{
                        "text": "[Question Text]",
                        "Topic": "[the topic this question relate to]",
                        "answer":"[written answer]",
                        "field":"[the field this question relate to]",
                        "level": "[Question Level]"
                        }},
                        {{
                        "text": "[Question Text]",
                        "Topic": "[the topic this question relate to]",
                        "answer":"[written answer]",
                        "field":"[the field this question relate to]",
                        "level": "[Question Level]"
                        }},
                        // ... (28 more questions)
                    ]
                    }}
                    Please generate the 30 questions based on the user's provided specifications.
                    """
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        #config=types.GenerateContentConfig(
        #    system_instruction=sys_instruct),
        contents=[prompt]
    )
    return  clean_and_parse_gemini_json(response.text)


# questions= geminiAPI("AIzaSyDbgILxNKc0RZjgER7LK-SpKVU4X7HFkyI","Software Egnieering","DevOps","Intermedaite")['questions']
# for q in questions : 
#     print(q['text'])
#     for key,item in dict(q['answer'] ).items():
#         print(key , item)
#     break


def quizGeminiAPI(api_key,field,level,topic):
    prompt = f"""You are an expert Question Bank generator for software engineering practice. Your task is to generate 30 multiple-choice questions (MCQs) in JSON format, tailored to the user's specifications.
                    User Specifications:
                     Field: {field}
                     Topics: {topic}
                     Question Level: {level}
                    Instructions:
                    1.  Generate 30 MCQ Question based on the provided field, track, topics, and question level.
                    2.  Ensure all questions are relevant to the specified topics within the given track and field.
                    3.  The question level should accurately reflect the difficulty (entry, intermediate, or advanced).
                    4.  Each question should have choices A,B,C, and D  with  only one correct answer 
                    5.  Return the questions in a JSON with the following structure:
                    {{
                    "questions": [
                        {{
                        "text": "[Question Text]",
                        "choices": [
                        {{"label": "A","choice_text":"[First answer]","is_correct":"[True or False]" }} ,
                        {{"label":"B", "choice_text":"[Second answer]","is_correct":"[True or False]" }},
                        {{"label":"C", "choice_text":"[Third answer]","is_correct":"[True or False]" }} ,
                        {{"label":"D", "choice_text":"[Fourth answer]","is_correct":"[True or False]" }},
                        ],
                        "answer_reason":"short explaination for the correct answer"
                        }},
                        {{ 
                        "text": "[Question Text]",
                        "choices": [
                        {{"label": "A","choice_text":"[First answer]","is_correct":"[True or False]" }} ,
                        {{"label":"B", "choice_text":"[Second answer]","is_correct":"[True or False]" }},
                        {{"label":"C", "choice_text":"[Third answer]","is_correct":"[True or False]" }} ,
                        {{"label":"D", "choice_text":"[Fourth answer]","is_correct":"[True or False]" }},
                        ],
                        "correct_answer":"[A,B,C, or D]",
                        "reason":"short explaination for the correct answer",
                        }},
                        // ... (28 more questions)
                    ]
                    }}
                    Please generate the 30 questions based on the user's provided specifications.
                    """
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        #config=types.GenerateContentConfig(
        #    system_instruction=sys_instruct),
        contents=[prompt]
    )
    
    #return  json.loads(response.text.replace("json","").replace("`",""))
    return clean_and_parse_gemini_json(response.text)

def HrQuestionsGeminiAPI(api_key):
    prompt = f"""Generate a list of 10 HR interview questions for Technical Engineers in (Software Engineering / Cyber secruity / Data science , etc..) to practice.
                Include a mix of the following categories:
                1. Behavioral HR questions
                2. General HR questions
                For each question, return the following details in a JSON structured format:
                {{ 
                "questions": [
                    {{ 
                    "text": "The text of the question",
                    "answer": "Provide a detailed sample answer to the question, showing how the interviewee should respond.",
                    "category": "The category of the question, either 'Behavioral' or 'HR'",
                    "thought_process": "Explain the way the interviewee should think when answering the question. This should guide the approach to answering the question effectively."
                    }},
                    {{ 
                    "text": "The second question text",
                    "answer": "Provide a detailed sample answer to the second question.",
                    "category": "The category of the second question",
                    "thought_process": "Explain the thought process for this question."
                    }},
                    ...
                ]
                }}
            Make sure the answers are practical and can help someone prepare for an HR interview.and make sure the response is JSON data


              """
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        #config=types.GenerateContentConfig(
        #    system_instruction=sys_instruct),
        contents=[prompt]
    )
    return clean_and_parse_gemini_json(response.text)
    #return  json.loads(response.text.replace("json","").replace("`",""))