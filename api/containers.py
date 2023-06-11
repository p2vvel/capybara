import docker
from . import config

client = docker.DockerClient(base_url=config.CODE_DOCKER_URI)

# client.containers.run("ubuntu", "echo hello world")

# container = client.containers.run("linuxserver/code-server", "echo hello world")

# temp = container

client.containers.list()

code = client.containers.run(
    image=config.CODE_DOCKER_URI,
    name="code",
    detach=True,
    ports={"8443/tcp": 8443},
    environment={
        "PASSWORD": "1234",
        "SUDO_PASSWORD": "4567",
    },
    # mem_limit="1g",
)


client.containers.get("code").remove(force=True)


def start_dev_container():
    code = client.containers.run(
        image="linuxserver/code-server",
        name="code",
        detach=True,
        ports={"8443/tcp": 8443},
        environment={
            "PASSWORD": "1234",
            "SUDO_PASSWORD": "4567",
        },
        # mem_limit="1g",
    )

def get_dev_containers():
    return client.containers.list(all=True, filters={"ancestors"})