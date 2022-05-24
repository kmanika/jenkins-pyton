import jenkins
server = jenkins.Jenkins('http://localhost:8080')
version = server.get_version()
print('my version: ', version)
server.create_job('folder',jenkins.EMPTY_FOLDER_XML)