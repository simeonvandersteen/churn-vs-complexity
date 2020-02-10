## Churn vs Complexity chart

This is a hacked thing to get some insight into the pain points of your (java) code base.
It wasn't meant for sharing so it will take some effort to get up and running.
There's also quite some room for improvement, contributions are welcome!  

Some background can be found [here](https://xebia.com/blog/using-metrics-to-find-the-pain-points-in-a-legacy-codebase/). 

#### Prerequisites:
- Ruby + bundler
- Python 3.7 + pipenv
- SonarQube (I ran sonarqube:7.9.2-community with Docker)


#### How to 

Generate data for a bunch of versions of your code. For each version:

- Check out your git repo to the version you're interested in
- Run unit tests with jacoco reports
- Publish results to Sonar
- Wait for Sonar to have processed the results
- Run "changed-files" script to generate a json file with data from sonar and git combined.
It assumes a semantic version in your commit. You'll also need to change the "component"
query parameter in the sonar URL in the script to pick up the correct files.
- You probably need to remove the sonar data for the next iteration.

(I've dumped most of the commands in generate.sh)

Run "plot" script to plot all the generated json files into a nice chart.