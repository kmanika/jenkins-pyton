pipeline {
    agent any
    stages {
        stage('Git Pull') {
            steps {
                echo 'Code Pulling'
                sh 'git clone https://github.com/kmanika/lambda-tf.git'
            }
        }
        stage('terraform plan') {
            steps {
                sh 'cd ./lambda-tf/lambda-tf'
                sh 'ls -ltr'
                echo 'terraform init'
                sh 'terraform init'
                echo 'terraform plan'
                sh 'terraform plan'
            }
        }
        stage('terraform apply') {
            steps {
                echo 'terraform apply'
            }
        }
    }
}
post {
    always {
        cleanWs()
    }
}