import os
from dotenv import load_dotenv
from crewai import Agent
from crewai_tools import SerperDevTool
from crewai import Task
from crewai import Crew, Process

# Load environment variables
load_dotenv()

SERPER_API_KEY=os.environ("SERPER_API_KEY")
GROQ_API_KEY=os.environ("GROQ_API_KEY")

os.environ["SERPER_API_KEY"] = SERPER_API_KEY 
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

os.environ["GROQ_MODEL"] = "llama3-70b-8192" 

search_tool = SerperDevTool()

researcher=Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
       """ Driven by curiosity, you're at the forefront of
        innovation, eager to explore and share knowledge that could change
        the world."""
    ),
    tools=[search_tool],
    allow_delegation=True
)

