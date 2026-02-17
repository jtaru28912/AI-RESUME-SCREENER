import logging
import pandas as pd
import os
import re

from .exceptions import DataLoaderException
from .file_reader_utils import read_file_text

logger = logging.getLogger(__name__)
SUPPORTED_EXTENSIONS = ('.txt', '.pdf', '.docx', '.doc')


def extract_candidate_name(filename: str):
    name = os.path.splitext(filename)[0]
    name = name.split('-')[0]
    name = name.replace('_', ' ')
    name = re.sub(r'\b(resume|cv|final|updated|latest)\b', '', name, flags=re.I)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def load_resume(resume_input_path: str):
    try:
        records = []
        resume_counter = 1

        for file in os.listdir(resume_input_path):
            if not file.lower().endswith(SUPPORTED_EXTENSIONS):
                continue

            resume_id = f"R-{resume_counter}"
            resume_counter += 1

            candidate_name = extract_candidate_name(file)
            file_path = os.path.join(resume_input_path, file)

            resume_text = read_file_text(file_path)
            if not resume_text:
                continue

            records.append({
                'resume_id': resume_id,
                'candidate_name': candidate_name,
                'resume_detail': resume_text,  
                'source_file': file
            })


        df = pd.DataFrame(records)
        return df.sort_values(by='resume_id', ignore_index=True)

    except Exception as e:
        logger.error(f"Error loading resume from {resume_input_path}: {e}")
        raise DataLoaderException(f"Error loading resume from {resume_input_path}: {e}")


def load_job_description(job_description_input_path):
    try:
        records = []
        jd_counter = 1

        for file in os.listdir(job_description_input_path):
            if not file.lower().endswith(SUPPORTED_EXTENSIONS):
                continue

            job_description_id = f"JD-{jd_counter}"
            jd_counter += 1

            jd_title = os.path.splitext(file)[0]
            file_path = os.path.join(job_description_input_path, file)

            job_description_text = read_file_text(file_path)
            if not job_description_text:
                continue

            records.append({
                'job_description_id': job_description_id,
                'job_description_title': jd_title,
                'job_description_text': job_description_text, 
                'source_file': file
                        })

        df = pd.DataFrame(records)
        return df.sort_values(by='job_description_id', ignore_index=True)

    except Exception as e:
        logger.error(f"Error loading job descriptions from {job_description_input_path}: {e}")
        raise DataLoaderException(f"Error loading job descriptions from {job_description_input_path}: {e}")
