import os
import yaml

from langchain.schema import BaseOutputParser


# Read OpenAI key from ~/.cal_hack/config.yaml
def get_openai_api_key():
    with open(os.path.expanduser("~/.cal_hack/config.yaml"), "r") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
        if "openai_api_key" not in config:
            raise Exception("OpenAI API key not found in ~/.cal_hack/config.yaml,"
                            " please add 'openai_api_key: YOUR_KEY' in the file.")
        openai_api_key = config["openai_api_key"]
        return openai_api_key
