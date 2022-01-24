# {{cookiecutter.title}}

## Index

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Tests](#tests)
6. [Deployment](#deployment)
7. [Open Api:](#open_api)
8. [Postman collection:](#postman_collection)
9. [Getting started:](#getting_started)

## <a name="overview">Overview</a>

{{cookiecutter.description}}

## <a name="requirements">Requirements</a>

* System requirements

python >= {{cookiecutter.python_version}}

poetry >= x

docker >= x

docker-compose >= x

* Package requirements

Listed in pyproject.toml under '[tool.poetry.dependencies]'


## <a name="installation">Installation</a>

### Dependencies installation for development

It is recommended to use a virtual environment tool like poetry, venv or conda to isolate the installation of the package.

To install package dependencies, install [poetry](https://python-poetry.org/docs/), then run the following command:

~~~
poetry install
~~~ 

Alternatively, you can use the requirements.txt file and install dependencies by pip:

~~~
pip install -r requirements.txt
~~~


## <a name="configuration">Configuration</a>

This project uses environment variables to load its configuration.

Environment variables are read and validated through the use of the [pydantic](https://pydantic-docs.helpmanual.io/) library.

For testing, the environment variables are set by using the [pytest-dotenv](https://pypi.org/project/pytest-dotenv/) library. 
Set variables are the ones located in the .test.env file. 

For development deployment, the environment variables are set by using the [python-dotenv](https://pypi.org/project/python-dotenv/) library.
Set variables are the ones located in the .dev.env. If this file does not exist it must be created.

For production deployment, set variables are the ones located in the .prod.env file.

All .envs file must have the following content.

| Field | Value Type | Description | 
|-------|------------|-------------|
| x | x | x |


## <a name="tests">Tests</a>

From root directory run:

~~~
pytest project_name/tests/
~~~

Integration and validation tests may required some infrastructure. To deploy this infrastructure, from root directory, run:

~~~
chmod +x ./deploy_infrastructure.sh
./deploy_infrastructure.sh
~~~

This will use docker-compose to deploy the needed infrastructure as a collection of docker containers.


## <a name="deployment">Deployment</a>

### Development server

This section explains how to deploy a web server on your local machine to test the app.

From root directory, run:

~~~
chmod +x ./run_dev_server.sh
./run_dev_server.sh
~~~


### Production server via docker-compose

This section explains how to deploy the project as a collection of docker containers via docker-compose.

First, you will need to create an image of the project. To do this, run the following commands:

~~~
chmod +x ./build_docker_image.sh
./build_docker_image.sh
~~~

Now that we have created an image of the project, we will be able to ran it as a docker container.

To run a docker container containing the project and the needed infrastructure, run the following commands:

~~~
chmod +x ./deploy_docker_compose.sh
./deploy_docker_compose.sh
~~~

The project's API should now be available at the following location

~~~
http://localhost:port/
~~~

To tear down the deployment, run the following commands:

~~~
chmod +x tear-down-docker-compose.sh
./tear-down-docker-compose.sh
~~~

*Note*: the docker-compose deployment creates a virtual network that allows to connect other containers to this one by adding
them to this network (https://docs.docker.com/compose/networking/).


## <a name="open_api">Open Api</a>

Once deployed, you can access the Open Api documentation of the system at the following url:

~~~
http://{ip || domain_name}:{port}/docs
~~~

Here {ip || domain_name} relates to either the ip or the domain name where the web server is deployed.

Here, {port} relates to the port where the development web server listens for requests.

For example:

~~~
http://localhost:8000/docs
~~~


## <a name="postman_collection">Postman collection</a>

Under the postman directory there is one postman collection stored. With this collection of requests you can test your
deployment.

To use the collection, import it with the postman app.


## <a name="getting_started">Getting started</a>

To try the app:

1 deploy it

2 import the postman collection

3 make requests to the endpoints
