#!/bin/bash -ex

echo "Project dir: $1"

echo "correct commit checked out?"
read

pushd $1

mvn -T 1.0C clean install -DskipTests -Dverification.skip

mvn -Psonar jacoco:prepare-agent surefire:test

mvn -Psonar antrun:run@create-source-dirs sonar:sonar -Dsonar.publish -Dsonar.host.url=http://localhost:9000 -Dsonar.login=admin -Dsonar.password=admin

popd

echo "press enter to continue when sonar is done"
read

bundle exec changed-files $1

echo "now delete sonar project"
