from google import genai
from google.genai import types
import json

#sys_instruct="You are a cat. Your name is Neko."
# api_key="AIzaSyDbgILxNKc0RZjgER7LK-SpKVU4X7HFkyI"
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
    return  json.loads(response.text.replace("json","").replace("`",""))


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
    try:
        return  json.loads(response.text.replace("json","").replace("`",""))
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        print("Response text:", response.text)
        return response.text

    