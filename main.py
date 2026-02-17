from src.pipeline import resume_screener_pipeline
from src.data_loader import load_resume, load_job_description
from src.exceptions import LLMCallFailedError
from src.config_reader import resume_path, jd_path, output_path, project_name, run

print("Starting the Resume Screening Pipeline")

output_folder = output_path / f"{project_name}_{run}"
llm_folder = output_folder / "llm_outputs"

llm_folder.mkdir(parents=True, exist_ok=True)
output_folder.mkdir(parents=True, exist_ok=True)

# Load ALL resumes
res_df = load_resume(resume_input_path=resume_path)

# Load ALL job descriptions
jd_df = load_job_description(job_description_input_path=jd_path)

# 🔑 Select ONE JD
target_jd_file = "Job_Details_IAM.txt"
selected_jd_row = jd_df[jd_df['source_file'] == target_jd_file]

if not selected_jd_row.empty:
    selected_jd_id = selected_jd_row.iloc[0]['job_description_id']
    print(f"Selected JD ID: {selected_jd_id} for file: {target_jd_file}")
else:
    raise ValueError(f"{target_jd_file} not found in loaded Job Descriptions!")

resume_screener_pipeline(
    resume_df=res_df,
    jd_df=jd_df,
    jd_id=selected_jd_id,
    output_path=output_folder,
    llm_output=llm_folder
)

print("Pipeline Execution Completed!")
