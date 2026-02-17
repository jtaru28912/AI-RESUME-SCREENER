from pathlib import Path
from yaml import safe_load
import logging

logger = logging.getLogger(__name__)

with open('config.yaml', 'r') as f:
    config = safe_load(f)


resume_path = Path(config['paths']["resume_path"])
jd_path = Path(config['paths']['jd_path'])
output_path = Path(config['paths']['output_path'])  
model = config['llm']['model']
project_name = config['project']['name']
run = config['project']['run']
system_prompt = config['prompt']['system']


if __name__ == "__main__":
    with open('config.yaml', 'r') as f:
        print(config)