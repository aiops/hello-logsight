<a href="https://logsight.ai/"><img src="https://logsight.ai/assets/img/logol.png" width="150"/></a>

**Your Ally for Intelligent DevOps Pipelines**

logsight.ai infuses deep learning and AI-powered analytics to enable continuous software delivery and proactive troubleshooting



# Hello logsight.ai from Github Actions

## Hands-on
### Requirements
1. Register and activate an account at [logsight.ai](https://demo.logsight.ai/)

### Steps
1. **Fork** the repository 
2. Go to **Actions** and click on **I understand my workflows, go ahead and enable them**
3. **Setup repository secrets** by going into **Settings** => **Secrets** => **Actions** => **New repository secret**
   1. `Name`: **LOGSIGHT_USERNAME** should have `Value` of your logsight.ai username
   2. `Value`: **LOGSIGHT_PASSWORD** should have `Value` of your logsight.ai password
   3. Make sure you use the exact same `Names`
   4. In **Settings** make sure you tick the **Issues** box to enable the Github Issues in this repository.
4. The repository contains two **branches** named **baseline** and **candidate**. Go to https://github.com/aiops/hello-logsight/pulls and click on **New pull request**
5. Select **Base repository** to your_github_user/hello-logsight => **base** `main` ==> **compare** `baseline`
6. **Create pull request** and merge the **Baseline** by clicking on **Merge pull request** => **Confirm Merge**
7. Repeat steps 5 and 6 for  the **candidate** branch.
8. The workflow executes automatically. 
9. You can monitor the workflow in the **Actions** tab.
10. After few minutes, it will end with creating an issue report that specifies the **deployment risk**. You can check the report in the repository **Issues**.

#### Details
This repository illustrates the [logsight.ai Stage Verifier](https://docs.logsight.ai/#/monitor_deployments/stage_verifier) via GitHub Actions.

The repository contains [main.yml](https://github.com/aiops/hello-logsight/blob/main/.github/workflows/main.yml) workflow that:
1. Set ups connection to logsight.ai
2. Executes the [hello-logsight.py](https://github.com/aiops/hello-logsight/blob/main/hello_logsight.py) application, which generates logs
3. Verifies the logs from the new deployment in comparison to the previous one


The hello-logsight example ends here. You can get more in-depth knowledge about the actions and how to use them at the [Docs.](https://docs.logsight.ai/#/monitor_deployments/github_action)

