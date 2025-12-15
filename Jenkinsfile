// pipeline {
//     agent any    // <‑‑ run on the Jenkins node itself

//     stages {
//         stage('Build') {
//             steps {
//                 echo 'Building the application...'
//                 sh 'python3 --version || python --version'
//             }
//         }
//         stage('Test') {
//             steps {
//                 echo 'Testing the application...'
//                 sh 'python3 test_calc.py || python test_calc.py'
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 echo 'Deploying to production...'
//                 echo 'Great success! The app is live.'
//             }
//         }
//     }
// }

pipeline {
    agent any

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
                echo 'Deploying to folder...'
                sh '''
                    DEPLOY_DIR=/var/jenkins_home/deploy_app

                    # create folder if not exists
                    mkdir -p "$DEPLOY_DIR"

                    # copy app files from workspace to deploy folder
                    cp calc.py "$DEPLOY_DIR"/
                    cp test_calc.py "$DEPLOY_DIR"/
                '''
                echo 'Files copied to deploy folder.'
            }
        }
    }
}
