| Tactic           | Technique ID | Technique Name | Sub-Technique ID | Sub-Technique Name         | Windows EventIDs | Linux auditd Logs           |
|------------------|--------------|----------------|------------------|----------------------------|------------------|-----------------------------|
| Execution | T1204     | User Execution | N/A              | N/A                          | 4688, 4697, 1102  | EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1204     | User Execution | T1204.001        | User Execution - Malicious Link | 4624, 4688, 1102  | EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1204     | User Execution | T1204.002        | User Execution - Malicious File | 4688, 4697, 1102  | EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1204     | User Execution | T1204.003        | User Execution - Malicious Image | 4688, 4697, 1102  | EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1059     | Command and Scripting Interpreter | N/A              | N/A                          |   |  |
| Execution | T1059     | Command and Scripting Interpreter | T1059.001        | PowerShell | 4688, 4697, 4103, 4104, 800  |  |
| Execution | T1059     | Command and Scripting Interpreter | T1059.002        | AppleScript |   | EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1059     | Command and Scripting Interpreter | T1059.003        | Windows Command Shell | 4688, 4697  |  |
| Execution | T1059     | Command and Scripting Interpreter | T1059.004        | Unix Shell |   | EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1059     | Command and Scripting Interpreter | T1059.005        | Visual Basic | 4688, 4697  |  |
| Execution | T1059     | Command and Scripting Interpreter | T1059.006        | Python | 4688, 4697  | EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1059     | Command and Scripting Interpreter | T1059.007        | JavaScript | 4688, 4697  |  |
| Execution | T1059     | Command and Scripting Interpreter | T1059.008        | Network Device CLI |   | EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1569     | System Services | N/A              | N/A                          |   |  |
| Execution | T1569     | System Services | T1569.001        | Launchctl |   |  |
| Execution | T1569     | System Services | T1569.002        | Service Execution | 7034, 7035, 7036  |  |
| Execution | T1053     | Scheduled Task/Job | N/A              | N/A                          | 4698, 4699, 4700, 4701, 4702  | CRED_DISP, USER_START, USER_END |
| Execution | T1053     | Scheduled Task/Job | T1053.002        | At | 4698, 4699, 4700, 4701, 4702  | CRED_DISP, USER_START, USER_END |
| Execution | T1053     | Scheduled Task/Job | T1053.003        | Cron |   | CRON, CRON_JOB |
| Execution | T1053     | Scheduled Task/Job | T1053.005        | Scheduled Task | 4688, 5145, 4698, 4699, 4700, 4701, 4702  |  |
| Execution | T1053     | Scheduled Task/Job | T1053.006        | Systemd Timers |   | UNIT, UNIT_RESULT |
| Execution | T1053     | Scheduled Task/Job | T1053.007        | Container Orchestration Job |   | KUBE_AUDIT |
| Execution | N/A     | N/A | N/A              | N/A                          |   |  |
| Execution | T1203     | Exploitation for Client Execution | N/A              | N/A                          | 4688, 4697  | EXECVE, CRED_DISP |
| Execution | T1047     | Windows Management Instrumentation | N/A              | N/A                          | 4688, 4697, 5857, 5858, 5859  |  |
| Execution | T1106     | Native API | N/A              | N/A                          | 4688, 4697, 1102, 4663  | SYSCALL, EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1648     | Serverless Execution | N/A              | N/A                          | 4688  | EXECVE, execveat |
| Execution | T1129     | Shared Modules | N/A              | N/A                          | 4688, 4697, 1102  | SYSCALL, EXECVE, execveat |
| Execution | T1072     | Software Deployment Tools | N/A              | N/A                          | 4688, 4697, 1102  | EXECVE, execveat, CRED_DISP, USER_START, USER_END |
| Execution | T1609     | Container Administration Command | N/A              | N/A                          | 4688  | EXECVE, execveat, DOCKER |
| Execution | T1610     | Deploy Container | N/A              | N/A                          | 4688  | EXECVE, execveat, DOCKER, KUBE_AUDIT |
