import docker
from . import config

client = docker.DockerClient(base_url=config.CODE_DOCKER_URI)
