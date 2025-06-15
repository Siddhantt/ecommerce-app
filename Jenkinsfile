pipeline {
    agent any

    environment {
        GIT_USERNAME = 'Siddhantt'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', credentialsId: 'Githubtoken', url: 'https://github.com/Siddhantt/ecommerce-app.git'
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
                sh '''
                    docker rm -f test-app || true
                    docker run -d -p 5001:5000 --name test-app ecommerce-app:latest
                    sleep 5
                    curl -f http://localhost:5001/health
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Build or Test Failed.'
        }
        success {
            echo '✅ Pipeline completed successfully.'
        }
    }
}

