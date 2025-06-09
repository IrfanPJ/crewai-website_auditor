from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LatestAiDevelopment():
    """LatestAiDevelopment crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def web_scraper_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['WebScraperAgent'],
            verbose=True
        )

    @agent
    def code_analyzer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['CodeAnalyzerAgent'],
            verbose=True
        )
    
    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )
    
    

    @task
    def scrape_website_content(self) -> Task:
        return Task(
            config=self.tasks_config['ScrapeWebsiteContent'],
            agent=self.web_scraper_agent(),
            output_file='scraped_content.txt'
        )

    @task
    def analyse_web_code(self) -> Task:
        return Task(
            config=self.tasks_config['AnalyzeWebCode'],
            agent=self.code_analyzer_agent(),
            output_file='web_code_analysis.md'
        )
    
    @task
    def generate_improvement_report(self) -> Task:
        return Task(
            config=self.tasks_config['GenerateImprovementReport'],
            agent=self.reporting_analyst(),
            output_file='final_report.md'
        )
    

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
