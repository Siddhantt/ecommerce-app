pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-username/ecommerce-app.git'
            }
        }

        stage('Build App Image') {
            steps {
                dir('app') {
                    sh 'docker build -t ecommerce-app:latest .'
                }
            }
        }

        stage('Build DB Image') {
            steps {
                dir('db') {
                    sh 'docker build -t ecommerce-db:latest .'
                }
            }
        }

        stage('Test App Health') {
            steps {
                sh 'docker run -d -p 5000:5000 --name test-app ecommerce-app:latest'
                sh 'sleep 5'
                sh 'curl --fail http://localhost:5000/health'
                sh 'docker stop test-app && docker rm test-app'
            }
        }
    }

    post {
        success {
            echo '✅ Build and Test Success!'
        }
        failure {
            echo '❌ Build or Test Failed.'
        }
    }
}


