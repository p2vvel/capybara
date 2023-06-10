import docker


client = docker.from_env()

# client.containers.run("ubuntu", "echo hello world")

# container = client.containers.run("linuxserver/code-server", "echo hello world")

# temp = container


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


client.containers.get("code").remove(force=True)
