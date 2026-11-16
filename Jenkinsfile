pipeline {
        agent any

        environment {
            PYTHON   = 'C:/Users/Personal Computer/jenkins/autotests-venv/Scripts/python.exe'
            UI_COV   = 'C:/Users/Personal Computer/jenkins/autotests-venv/Scripts/ui-coverage-tool.exe'
            PLAYWRIGHT_BROWSERS_PATH = 'C:/Users/Personal Computer/AppData/Local/ms-playwright'
        }

        options {
            timestamps()
            buildDiscarder(logRotator(numToKeepStr: '20'))
        }

        stages {
            stage('Run tests') {
                steps {
                    withCredentials([usernamePassword(credentialsId: 'autotests-user',
                                                       usernameVariable: 'TEST_USER.EMAIL',
                                                       passwordVariable: 'TEST_USER.PASSWORD')]) {
                        bat '"%PYTHON%" -m pytest -m regression --junitxml=report.xml --alluredir=./allure-results --numprocesses 2'
                    }
                }
            }

            stage('Coverage report') {
                steps {
                    bat '"%UI_COV%" save-report'
                }
            }

            stage('Publish') {
                steps {
                    junit allowEmptyResults: true, testResults: 'report.xml'
                    allure results: [[path: 'allure-results']]
                }
            }
        }

        post {
            always {
                archiveArtifacts artifacts: 'report.xml, allure-results/**, coverage.html, coverage-history.json, coverage-report.json',
                                 allowEmptyArchive: true
            }
        }
    }
