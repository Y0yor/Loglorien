| Tactic           | Technique ID | Technique Name | Sub-Technique ID | Sub-Technique Name         | Windows EventIDs | Linux auditd Logs           |
|------------------|--------------|----------------|------------------|----------------------------|------------------|-----------------------------|
| Initial Access | T1189     | Drive-by Compromise | N/A              | N/A                          | 4624, 4688  | USER_START, EXECVE |
| Initial Access | T1190     | Exploit Public-Facing Application | N/A              | N/A                          | 4624, 4688  | USER_START, EXECVE |
| Initial Access | T1133     | External Remote Services | N/A              | N/A                          | 4624, 4688  | USER_START, EXECVE |
| Initial Access | T1200     | Hardware Additions | N/A              | N/A                          | 6416  | USB |
| Initial Access | T1566     | Phishing | N/A              | N/A                          |   |  |
| Initial Access | T1566     | Phishing | T1566.001        | Spearphishing Attachment | 4624, 4688  | USER_START, EXECVE |
| Initial Access | T1566     | Phishing | T1566.002        | Spearphishing Link | 4624, 4688  | USER_START, EXECVE |
| Initial Access | T1566     | Phishing | T1566.003        | Spearphishing via Service | 4624, 4688  | USER_START, EXECVE |
| Initial Access | T1091     | Replication Through Removable Media | N/A              | N/A                          | 6416, 4688  | USB, EXECVE |
| Initial Access | T1195     | Supply Chain Compromise | N/A              | N/A                          |   |  |
| Initial Access | T1195     | Supply Chain Compromise | T1195.001        | Compromise Software Dependencies and Development Tools | 4688, 4697  | EXECVE, CRED_DISP |
| Initial Access | T1195     | Supply Chain Compromise | T1195.002        | Compromise Software Supply Chain | 4688, 4697  | EXECVE, CRED_DISP |
| Initial Access | T1195     | Supply Chain Compromise | T1195.003        | Compromise Hardware Supply Chain | 6416, 4688  | USB, EXECVE |
| Initial Access | T1199     | Trusted Relationship | N/A              | N/A                          | 4624, 4688  | USER_START, EXECVE |
| Initial Access | T1078     | Valid Accounts | N/A              | N/A                          |   |  |
| Initial Access | T1078     | Valid Accounts | T1078.001        | Default Accounts | 4624, 4625, 4720, 4722, 4723, 4724, 4725, 4726  | USER_AUTH, CRED_ACQ, CRED_DISP, USER_START, USER_END |
| Initial Access | T1078     | Valid Accounts | T1078.002        | Domain Accounts | 4625, 33205, 4624, 4, 4624, 1149  | SSH |
| Initial Access | T1078     | Valid Accounts | T1078.003        | Local Accounts | 4624, 4625, 4720, 4722, 4723, 4724, 4725, 4726  | USER_AUTH, USER_ACCT, CRED_ACQ, CRED_REFR, CRED_DISP |
| Initial Access | T1078     | Valid Accounts | T1078.004        | Cloud Accounts | 4624, 4625, 4738, 4720, 4722, 4725, 4726  |  |
