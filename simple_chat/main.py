import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

load_dotenv()


class ResponseModel(BaseModel):
    response: str


model = ChatOpenAI(base_url=os.environ.get("OPENAI_BASE_URL"),
                   api_key=os.environ.get("OPENAI_API_KEY"),
                   model="gpt-5.4")
model_with_structured_output = model.with_structured_output(ResponseModel)


def main(input) -> str:
    response = model_with_structured_output.invoke(input)
    print(response)
    print(type(response))
    return response.response


if __name__ == "__main__":
    print(main("Hi"))
