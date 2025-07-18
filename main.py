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

# Creating a senior researcher agent with memory and verbose mode
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

# Creating a writer agent with custom tools and delegation capability
writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        """With a flair for simplifying complex topics, you craft
        engaging narratives that captivate and educate, bringing new
        discoveries to light in an accessible manner."""
    ),
    tools=[search_tool],
    allow_delegation=False
)

