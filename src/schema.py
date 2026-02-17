from pydantic import BaseModel, Field
from typing import List, Literal


class ResumeSchema(BaseModel):
    name: str = Field(
        description="Mention the name of the candidate given in the resume"
    )

    summary: str = Field(
        description="Specify a brief summary of the candidate given in the resume."
    )

    total_experience: float = Field(
        description=(
            "Mention the total experience of the candidate given in the resume. "
            "If the total experience is not directly mentioned, calculate it."
        )
    )

    relevant_experience: float = Field(
        description=(
            "Mention the relevant experience as per the job description. "
            "If the relevant experience is not directly mentioned, calculate it."
        )
    )

    highest_education: str = Field(
        description="Specify the highest education of the candidate."
    )

    relevant_education: Literal["Yes", "No"] = Field(
        description=(
            "Mention whether the candidate has relevant education. "
            "Relevant education includes B.Tech, M.Tech, MCA, MBA, "
            "M.Sc. (Maths/Statistics), or certificates in Data Science or AI."
        )
    )

    matching_skills: List[str] = Field(
        description="Skills of the candidate that exactly or nearly match the job description."
    )

    missing_skills: List[str] = Field(
        description="Skills missing in the candidate as per the job description."
    )

    recommendation: Literal[
        "Strongly Recommended", "Recommended", "Not Recommended"
    ] = Field(
        description="Overall recommendation for the candidate."
    )

    reasoning: str = Field(
        description="Provide reasoning and explanation in at least 50–100 words."
    )