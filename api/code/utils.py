from fastapi import HTTPException, status
from api.containers import client
from .models import CodeStatus, ContainerEdit, CodeStateCommandEnum
from api import config
from api.auth.models import User

from docker.models.containers import Container
from docker import errors as docker_errors


def user_code_name(user: User) -> str:
    return f"code-{user.username}"


def start_dev_container(user: User) -> Container:
    temp = get_container(user_code_name(user))
    if temp is None:
        code = client.containers.run(
            image="linuxserver/code-server",
            name=user_code_name(user),
            detach=True,
            ports={"8443/tcp": None},
            environment={
                "PASSWORD": "1234",  # TODO: password hashes
                "SUDO_PASSWORD": "1234",
            },
            mem_limit=config.DEV_SERVER_RAM,
        )
        return code
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Container already exists"
        )


def get_container(name: str) -> Container:
    try:
        code = client.containers.get(name)
        return code
    except docker_errors.NotFound:
        return None
    except docker_errors.APIError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Docker API error"
        )


def container_status(container: Container | None) -> CodeStatus:
    if container is None:
        return CodeStatus(name=None, status="Container not created", url=None)
    else:
        if container.status == "running":
            ip = container.ports["8443/tcp"][0]["HostIp"]
            port = container.ports["8443/tcp"][0]["HostPort"]
            url = f"http://{ip}:{port}"
        else:
            url = None
        return CodeStatus(name=container.name, status=container.status, url=url)


def delete_container(container: Container) -> None:
    try:
        container.remove(force=True)
    except docker_errors.APIError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Docker API error")


def container_edit(container: Container, state: ContainerEdit) -> None:
    if state.state == CodeStateCommandEnum.START:
        container.start()
    elif state.state == CodeStateCommandEnum.STOP:
        container.stop()
    elif state.state == CodeStateCommandEnum.RESTART:
        container.restart()
    else:
        return
