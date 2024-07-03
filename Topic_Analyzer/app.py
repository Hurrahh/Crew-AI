from crewai import Crew, Process
import streamlit as st
from agents import planner,analyzer,writer,researcher,tool
from tasks import research_task,planning_task,write_task,analysis_task


st.set_page_config(
    page_title="Shin",
    page_icon="🤖",
)

crew = Crew(
  agents=[researcher, analyzer, planner, writer],
  tasks=[research_task, analysis_task,planning_task,write_task],
  process=Process.sequential,
)

st.title("Topic Analyzer")

topic = st.text_input("Enter your topic here")
context = st.text_input("Describe your context like in what ways you want your topic to get described ")


if st.button("Submit"):
    response = crew.kickoff(inputs={'topic': topic, 'context': context})
    st.write(response)





