ALGORITHM = "HS256"     # used for password hashing
SECRET = "d9b17b791db4a785cfaf89a02f5eb3b4459670d74d68be3900ce88de50a33e68"

MONGO_URI = "mongodb://localhost:27017/code"
MONGO_DB = "code"

# docker instance used to run development vscode servers
CODE_DOCKER_URI = "tcp://localhost:4243"
DEV_SERVER_IMAGE = "linuxserver/code-server"