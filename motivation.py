import langchain
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

chat_model = ChatGroq(api_key=GROQ_API_KEY,model="llama-3.1-8b-instant",temperature=0.7)



def motivation_ai(student_name,weak_subject,problem_solving,stress_management,backup_plan,communication,motivation_level):
    
    prompt = f"""
    You are an AI student mentor and psychologist.
    Analyze the student's personality and learning behavior.
    Student Details:
    Name : {student_name}
    Weak subject: {weak_subject}
    Problem Solving Ability:{problem_solving}/10
    Stress Management: {stress_management}
    Backup plan: {backup_plan}
    Communication Skill: {communication}
    Motivation Level: {motivation_level}

    Give:

    1. Personality analysis
    2. Motivation
    3. Study improvement techniques
    4. Confidence boosting advice
    5. Time management tips
    6. Stress handling advice

    Instructions:
    - Keep response student friendly
    - Use simple language
    - Make response motivational
    - Keep answer structured
    - Use bullet points
    """

    response = chat_model.invoke(prompt)
    return response.content



