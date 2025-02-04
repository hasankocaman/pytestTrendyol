pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                bat '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                bat '''
                    pytest tests/test_trendyol.py -v
                '''
            }
        }
    }
    
    post {
        always {
            junit '**/test-results/*.xml'
        }
    }
}
