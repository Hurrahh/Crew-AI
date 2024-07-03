import os
from crewai import Agent
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
# Load environment variables
load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize tools and LLM
tool = SerperDevTool()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", verbose=True, temperature=0.5, google_api_key=os.getenv("GOOGLE_API_KEY"))

researcher = Agent(
    role='Senior Researcher',
    goal='Conduct comprehensive research on {topic} trends, opportunities, and challenges.',
    verbose=True,
    memory=True,
    backstory=(
        "With a passion for uncovering emerging trends, you delve deep into"
        "research to provide a detailed analysis of the {topic}."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Defining the writer agent
writer = Agent(
    role='Writer',
    goal='Craft compelling content on {topic} trends and advancements.',
    verbose=True,
    memory=True,
    backstory=(
        "With a talent for storytelling, you translate complex information"
        "into engaging narratives that captivate and educate readers."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False  # Assuming writing requires direct input from the agent
)


# Defining the analyzer agent
analyzer = Agent(
  role='Analyzer',
  goal='Break down {topic} into main subtopics and provide detailed insights on each.',
  verbose=True,
  memory=True,
  backstory=(
    "With an analytical mind, you dissect topics to uncover"
    "the underlying components, providing a structured overview and deep insights."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=True
)

# Defining the planner agent
planner = Agent(
  role='Planner',
  goal='Create a detailed step-by-step preparation plan for {topic} tailored to the context of {context}.',
  verbose=True,
  memory=True,
  backstory=(
    "With a meticulous approach, you design comprehensive"
    "plans that guide users through their preparation journey, ensuring they are well-prepared for their specific needs."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=True
)

