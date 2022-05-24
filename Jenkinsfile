pipeline {
    agent any
    stages {
        stage('Git Pull') {
            steps {
                echo 'Git pull success'
            }
        }
        stage('terraform plan') {
            steps {
                echo 'terraform init & apply'
            }
        }
        stage('terraform apply') {
            steps {
                echo 'terraform apply'
            }
        }
    }
}