<a href="https://logsight.ai/"><img src="https://logsight.ai/assets/img/logol.png" width="150"/></a>


# Hello logsight.ai from GitHub Actions

The following illustrates an example of using logsight.ai [Stage Verifier.](https://docs.logsight.ai/#/monitor_deployments/stage_verifier)

## Use Case
<div align=center><img src="assets/use_case.png" alt="drawing" style="width:40%;"/> </div>

[Open tutorial in extra browser page](https://docs.logsight.ai/#/monitor_deployments/github_action)

## Steps
1. **Fork** the repository 
<div align=center><img src="assets/fork.png" alt="drawing" style="width:80%;"/> </div>

2. Go to **Pull Requests** and click on **New pull request**
3. Set `compare` to `candidate` and **Create pull request**.
<div align=center><img src="assets/pullrq.png" alt="drawing" style="width:80%;"/> </div>

5. The **quality check will run**.
<div align=center><img src="assets/check.png" alt="drawing" style="width:80%;"/> </div>

6. If the check is failing, it will create an issue report that specifies the **deployment risk**. You can check the report in the [**Issues**](https://github.com/aiops/hello-logsight/issues).


## Report in Github

The issue looks similar to:
<div align=center><img src="assets/issue.png" alt="drawing" style="width:80%;"/> </div>


## Report in Logsight.ai

To open the detailed online report, you need to have [logsight.ai](https://demo.logsight.ai/) user account. 
**Login and then click** on the detailed report.

The detailed online report shows the overview and the state analysis as in:
<div align=center><img src="assets/report.png" alt="drawing" style="width:80%;"/> </div>


The hello-logsight example ends here. You can get more in-depth knowledge about the actions and how to use them at the [Docs.](https://docs.logsight.ai/#/monitor_deployments/github_action)

