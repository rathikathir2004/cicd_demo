
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
//                     set -e

//                     DEPLOY_DIR=/var/jenkins_home/deploy_app
//                     BACKUP_DIR=/var/jenkins_home/deploy_backup

//                     echo "Backing up current live version (if any)..."
//                     if [ -d "$DEPLOY_DIR" ]; then
//                         rm -rf "$BACKUP_DIR"
//                         cp -r "$DEPLOY_DIR" "$BACKUP_DIR"
//                     fi

//                     echo "Deploying NEW version..."
//                     mkdir -p "$DEPLOY_DIR"
//                     cp calc.py "$DEPLOY_DIR"/
//                     cp test_calc.py "$DEPLOY_DIR"/

//                     # Simulate possible deploy failure (uncomment later to test rollback)
//                     #exit 1
//                 '''
//             }
//             post {
//                 failure {
//                     echo 'Deploy failed! Reverting to previous version...'
//                     sh '''
//                         DEPLOY_DIR=/var/jenkins_home/deploy_app
//                         BACKUP_DIR=/var/jenkins_home/deploy_backup

//                         if [ -d "$BACKUP_DIR" ]; then
//                             rm -rf "$DEPLOY_DIR"
//                             cp -r "$BACKUP_DIR" "$DEPLOY_DIR"
//                             echo "Rollback complete."
//                         else
//                             echo "No backup found; nothing to rollback."
//                         fi
//                     '''
//                 }
//                 success {
//                     echo 'Deploy succeeded. Previous backup kept in case you need manual rollback.'
//                 }
//             }
//         }
//     }
// }

pipeline {
    agent any

    environment {
        GIT_CREDS_ID = 'github_token'   // ID of the Jenkins credential you created
        REPO_URL     = 'https://github.com/rathikathir2004/cicd_demo.git'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: "${REPO_URL}",
                    credentialsId: "${GIT_CREDS_ID}"
            }
        }

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
                    echo 'Deploy succeeded locally.'
                }
            }
        }
    }

    // Runs only if all stages succeeded
    post {
        success {
            echo 'Pipeline success! Merging main -> dev and pushing...'
            withCredentials([usernamePassword(credentialsId: "${GIT_CREDS_ID}",
                                              usernameVariable: 'GIT_USER',
                                              passwordVariable: 'GIT_PASS')]) {
                sh '''
                    set -e
                    git config user.email "rathikathir2004@gmail.com"
                    git config user.name "rathikathir2004"

                    git fetch --all

                    # Ensure we are on dev, merge main into it, then push
                    git checkout dev
                    git merge origin/main

                    # Use injected variables instead of hardcoding the token
                    git push https://${GIT_USER}:${GIT_PASS}@github.com/rathikathir2004/cicd_demo.git dev
                '''
            }
        }
    }
}
