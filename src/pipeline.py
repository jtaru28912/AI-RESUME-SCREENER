from .exceptions import PipelineFailedError
from .llm_calls import make_api_call
from .helper_utils import get_jd, save_to_json
import pandas as pd
from .config_reader import system_prompt
from .schema import ResumeSchema

def resume_screener_pipeline(resume_df, jd_df, jd_id, output_path, llm_output):
    if resume_df.empty or jd_df.empty:
        raise PipelineFailedError("empty dataframes")

    all_results = []

    for row in resume_df.itertuples():
        try:
            res_id = row.resume_id
            res_details= row.resume_detail
            jd = get_jd(jd_df = jd_df, jd_id = jd_id)

            print(f'Resume_id- {res_id} has started' )

            result=make_api_call(system_prompt=system_prompt,
                                py_class=ResumeSchema,
                                resume=res_details,
                                job=jd)
            
            result_per_resume={'resume_id':res_id}
            result_per_resume.update(result)
            all_results.append(result_per_resume)
            
            llm_res_file=llm_output / f"{res_id}.json"
            print(f'Json output is saved for Resume_id- {res_id}')
            print('-----------------------------------------------\n')
            save_to_json(llm_res_file, result_per_resume)

        except Exception as e:
            print(f'Resume_id- {res_id} got some error- {e}')
            # If we want to fail fast, we could raise here. But for now let's see what happens.
            # But wait, if the error is "Pipeline Failed", it means the OUTER block caught it. 
            # So removing the outer block is the right move.
            pass # Keep the inner try-except for now to see per-resume errors. 

    final_df=pd.DataFrame(all_results)
    print('Final Data Frame is created')

    final_df.to_excel(output_path / "resume_screening_results.xlsx", index=False)
    print('Results are saved to the Excel file!')
