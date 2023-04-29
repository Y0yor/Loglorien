| Tactic           | Technique ID | Technique Name | Sub-Technique ID | Sub-Technique Name         | Windows EventIDs | Linux auditd Logs           |
|------------------|--------------|----------------|------------------|----------------------------|------------------|-----------------------------|
| Exfiltration | T1020     | Automated Exfiltration | N/A              | N/A                          | 3  | SOCKADDR |
| Exfiltration | T1020     | Automated Exfiltration | T1020.001        | Traffic Duplication | 3  | SOCKADDR |
| Exfiltration | T1048.002     | Data Transfer Size Limits | N/A              | N/A                          | 3  | SOCKADDR |
| Exfiltration | T1048     | Exfiltration Over Alternative Protocol | N/A              | N/A                          | 3, 23  | SOCKADDR, PATH |
| Exfiltration | T1048     | Exfiltration Over Alternative Protocol | T1048.001        | Exfiltration Over Symmetric Encrypted Non-C2 Protocol | 3, 23  | SOCKADDR, PATH |
| Exfiltration | T1048     | Exfiltration Over Alternative Protocol | T1048.002        | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | 3, 23  | SOCKADDR, PATH |
| Exfiltration | T1048     | Exfiltration Over Alternative Protocol | T1048.003        | Exfiltration Over Unencrypted Non-C2 Protocol | 3, 23  | SOCKADDR, PATH |
| Exfiltration | T1041     | Exfiltration Over C2 Channel | N/A              | N/A                          | 3  | SOCKADDR |
| Exfiltration | T1011     | Exfiltration Over Other Network Medium | N/A              | N/A                          | 3  | SOCKADDR |
| Exfiltration | T1011     | Exfiltration Over Other Network Medium | T1011.001        | Exfiltration Over Bluetooth | 3  | SOCKADDR |
| Exfiltration | T1052     | Exfiltration Over Physical Medium | N/A              | N/A                          | 6416  | KERNEL_DEVICE |
| Exfiltration | T1052     | Exfiltration Over Physical Medium | T1052.001        | Exfiltration over USB | 6416, 20001, 20003, 2100, 4663, 4656  | KERNEL_DEVICE |
| Exfiltration | T1567     | Exfiltration Over Web Service | N/A              | N/A                          | 3  | SOCKADDR |
| Exfiltration | T1567     | Exfiltration Over Web Service | T1567.001        | Exfiltration to Code Repository | 3  | SOCKADDR |
| Exfiltration | T1567     | Exfiltration Over Web Service | T1567.002        | Exfiltration to Cloud Storage | 3  | SOCKADDR |
| Exfiltration | T1567     | Exfiltration Over Web Service | T1029        | Scheduled Transfer | 3, 4698  | SOCKADDR, CRON |
| Exfiltration | T1567     | Exfiltration Over Web Service | T1537        | Transfer Data to Cloud Account | 3  | SOCKADDR |
