from pydantic import BaseModel, Field
from datetime import date
from typing import List

class Job(BaseModel):
    position: str = Field(..., examples=["Engineer", "Developer", "Analyst", "Scientist", "Team Lead", "Manager"], description="The job's title.")
    company: str = Field(..., description="The company's name")
    location: str = Field(..., description="The job's location, like city or state")
    region: str = Field(..., examples=["North America", "South America", "Europe", "Asia", "Africa", "Oceania"])
    status: str = Field(..., description="Applied, Viewed, Downloaded or Untracked (if was applied in the company site)")
    category: str = Field(..., description="The IT area where the job belongs (BackEnd, Data, SRE, DevOps, RPA...)")
    seniority: str = Field(..., description="Intern, Junior, Mid, Senior, Lead or Manager")
    model: str = Field(..., description="Remote, Onsite or Hybrid")
    when: date = Field(..., description="The diff between today and the last status, as date format [use today's date instead hours ago]")

class Jobs(BaseModel):
    applied: List[Job]