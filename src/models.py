from pydantic import BaseModel
from typing import List, Dict

class Module(BaseModel):
    name: str
    purpose: str
    key_functions: List[str]

class DevelopmentPlan(BaseModel):
    project_name: str
    description: str
    file_structure: Dict[str, List[str]]  # e.g., {"app": ["main.py", "auth.py"]}
    modules: List[Module]
    dependencies: List[str]