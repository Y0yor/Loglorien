import json

def generate_markdown_table(json_data):
    header = "| Tactic           | Technique ID | Technique Name | Sub-Technique ID | Sub-Technique Name         | Windows EventIDs | Linux auditd Logs           |\n"
    separator = "|------------------|--------------|----------------|------------------|----------------------------|------------------|-----------------------------|\n"
    table = header + separator

    for technique in json_data['techniques']:
        # Add technique row without sub-technique details
        windows_eventids = ', '.join([event['eventid'] for event in technique.get('windows_eventids', [])])
        linux_auditd_logs = ', '.join([log['type'] for log in technique.get('linux_auditd_logs', []) if isinstance(log, dict)])
        technique_id = technique.get('technique_id', 'N/A')
        technique_name = technique.get('technique_name', 'N/A')
        row = f"| {json_data['tactic']} | {technique_id}     | {technique_name} | N/A              | N/A                          | {windows_eventids}  | {linux_auditd_logs} |\n"
        table += row
        for entry in technique.get('sub_techniques', []):
            # Add sub-technique row
            windows_eventids = ', '.join([event['eventid'] for event in entry.get('windows_eventids', [])])
            linux_auditd_logs = ', '.join([log['type'] for log in entry.get('linux_auditd_logs', []) if isinstance(log, dict)])
            sub_technique_id = entry.get('sub_technique_id', 'N/A')
            sub_technique_name = entry.get('sub_technique_name', 'N/A')
            row = f"| {json_data['tactic']} | {technique_id}     | {technique_name} | {sub_technique_id}        | {sub_technique_name} | {windows_eventids}  | {linux_auditd_logs} |\n"
            table += row

    return table




if __name__ == "__main__":
    with open("tactics/json/initial_acess.json", "r") as json_file:
        data = json.load(json_file)
    markdown_table = generate_markdown_table(data)
    with open("tactics/view/initial_acess_table_association.md", "w") as output_file:
        output_file.write(markdown_table)
