import jenkins
server = jenkins.Jenkins('http://localhost:8080')
version = server.get_version()
print('my version: ', version)