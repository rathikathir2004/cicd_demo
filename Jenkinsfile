

// pipeline {
//     agent any

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
//                 echo 'Deploying to folder...'
//                 sh '''
//                     DEPLOY_DIR=/var/jenkins_home/deploy_app

//                     # create folder if not exists
//                     mkdir -p "$DEPLOY_DIR"

//                     # copy app files from workspace to deploy folder
//                     cp calc.py "$DEPLOY_DIR"/
//                     cp test_calc.py "$DEPLOY_DIR"/
//                 '''
//                 echo 'Files copied to deploy folder.'
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
                    set -e

                    DEPLOY_DIR=/var/jenkins_home/deploy_app
                    BACKUP_DIR=/var/jenkins_home/deploy_backup

                    echo "Backing up current live version (if any)..."
                    if [ -d "$DEPLOY_DIR" ]; then
                        rm -rf "$BACKUP_DIR"
                        cp -r "$DEPLOY_DIR" "$BACKUP_DIR"
                    fi

                    echo "Deploying NEW version..."
                    mkdir -p "$DEPLOY_DIR"
                    cp calc.py "$DEPLOY_DIR"/
                    cp test_calc.py "$DEPLOY_DIR"/

                    # Simulate possible deploy failure (uncomment later to test rollback)
                    # exit 1
                '''
            }
            post {
                failure {
                    echo 'Deploy failed! Reverting to previous version...'
                    sh '''
                        DEPLOY_DIR=/var/jenkins_home/deploy_app
                        BACKUP_DIR=/var/jenkins_home/deploy_backup

                        if [ -d "$BACKUP_DIR" ]; then
                            rm -rf "$DEPLOY_DIR"
                            cp -r "$BACKUP_DIR" "$DEPLOY_DIR"
                            echo "Rollback complete."
                        else
                            echo "No backup found; nothing to rollback."
                        fi
                    '''
                }
                success {
                    echo 'Deploy succeeded. Previous backup kept in case you need manual rollback.'
                }
            }
        }
    }
}
