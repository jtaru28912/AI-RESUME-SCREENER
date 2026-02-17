import json


def get_jd(jd_df, jd_id):
    try:
        return jd_df[jd_df.job_description_id.isin([jd_id])].iloc[0].job_description_text
    except Exception as e:
        raise ValueError('Invalid JD ID or other issue') from e
    

def save_to_json(file_name, data):
      with open(file_name, 'w', encoding='utf-8') as f:
          json.dump(data, f)

