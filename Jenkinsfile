pipeline {
    agent {
        docker { 
            image 'python:3.9-slim' 
            // This runs the pipeline inside a Linux container with Python pre-installed
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Now this command works because we are inside the python container!
                sh 'python --version' 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the application...'
                sh 'python test_calc.py'
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
