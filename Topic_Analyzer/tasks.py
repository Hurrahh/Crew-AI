from crewai import Task
from agents import planner,analyzer,writer,researcher,tool


research_task = Task(
    description=(
        "Identify the latest trends in {topic}. Analyze market opportunities,"
        "potential risks, and the overall narrative surrounding {topic}."
        "Your final report should clearly articulate the key points,"
    ),
    expected_output='A detailed report on {topic} trends, opportunities, and challenges.',
    tools=[tool],
    agent=researcher,
)

analysis_task = Task(
      description=(
        "Break down the main topic of {topic} into key subtopics."
        "Provide detailed insights and a brief summary for each subtopic."
        "Highlight any significant trends, challenges, and opportunities within each subtopic."
      ),
      expected_output='A detailed report with key subtopics and insights on {topic}.',
      tools=[tool],
      agent=analyzer,
)

planning_task = Task(
      description=(
        "Create a detailed step-by-step preparation plan for {topic} tailored to the context of {context}."
        "The plan should include key resources, timelines, and actionable steps."
        "Ensure the plan is comprehensive and easy to follow."
      ),
      expected_output='A step-by-step preparation plan for {topic} in the context of {context}.',
      tools=[tool],
      agent=planner,
)

write_task = Task(
      description=(
        "Write an article on {topic} trends and advancements."
        "Focus on presenting the research findings in an accessible and engaging manner."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to understand, engaging, and positive."
      ),
      expected_output='A detailed article on {topic} advancements formatted as markdown.',
      tools=[tool],
      agent=writer,
      async_execution=False
)


