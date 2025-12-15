pipeline {
    agent any    // <‑‑ run on the Jenkins node itself

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'python3 --version || python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the application...'
                sh 'python3 test_calc.py || python test_calc.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to production...'
                echo 'Great success! The app is live.'
            }
        }
    }
}
