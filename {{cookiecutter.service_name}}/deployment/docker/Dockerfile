FROM python:{{cookiecutter.python_version}}-slim

## Install dependencies
RUN pip install "poetry==1.1.4"
COPY poetry.lock pyproject.toml ./
RUN poetry export -o requirements.txt
RUN pip install -r requirements.txt

# Setup project
COPY ./{{cookiecutter.service_name}} /{{cookiecutter.service_name}}

# Run server
CMD ["uvicorn", "{{cookiecutter.service_name}}.entrypoint.app:app", "--host", "0.0.0.0", "--port", "8000"]
