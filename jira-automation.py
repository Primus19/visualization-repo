from jira import JIRA
from jira.exceptions import JIRAError

# Static project and issue keys
EPIC_PROJECT_KEY = "10267"
STORY_PROJECT_KEYS = {
   "App Vuln": {"project": "10333", "issue_key": "RANGR-6289"},
   "Atlantis": {"project": "10311", "issue_key": "DTIN-3153"},
   "Atlas Auth": {"project": "10302", "issue_key": "CPS-3494"},
   "Atlas CM": {"project": "10302", "issue_key": "CPS-3719"},
   "Cassandra": {"project": "10245", "issue_key": "PLAT-9119"},
   "CloudFunnel 2.0": {"project": "10385", "issue_key": "DF-1576"},
   "Dataset Components": {"project": "10245", "issue_key": "PLAT-9168"},
   "DV Gateway": {"project": "10311", "issue_key": "DTIN-2897"},
   "File Services": {"project": "10302", "issue_key": "CPS-3720"},
   "FLM": {"project": "10304", "issue_key": "FLM-3315"},
   "Hermes-API": {"project": "10311", "issue_key": "DTIN-3365"},
   "Hit Manager": {"project": "10327", "issue_key": "STR-1874"},
   "Kafka Connect": {"project": "10245", "issue_key": "PLAT-9118"},
   "Management Threat Actions": {"project": "10317", "issue_key": "SPP-2433"},
   "mgmt-cleaner-signing-service": {"project": "10322", "issue_key": "EPPS-5251"},
   "mgmt-upgrade-policy": {"project": "10322", "issue_key": "EPPS-5249"},
   "MGMT-War": {"project": "10327", "issue_key": "STR-1985"},
   "MMS Gateway": {"project": "10314", "issue_key": "EDOPS-6487"},
   "Perseus": {"project": "10311", "issue_key": "DTIN-2898"},
   "Ranger Assets": {"project": "10333", "issue_key": "RANGR-6287"},
   "Ranger Fingerprinter": {"project": "10333", "issue_key": "RANGR-6286"},
   "Ranger Pipeline": {"project": "10333", "issue_key": "RANGR-6285"},
   "Remote Ops Forensics": {"project": "10339", "issue_key": "ELB-6717"},
   "Remote Scripts MMS": {"project": "10339", "issue_key": "ELB-5752"},
   "Reputation": {"project": "10319", "issue_key": "DFREP-3887"},
   "RSO": {"project": "10339", "issue_key": "ELB-5751"},
   "S1 Redis": {"project": "10245", "issue_key": "PLAT-9955"},
   "Scalyr Star Control Plane": {"project": "10327", "issue_key": "STR-1987"},
   "Spark Operator": {"project": "10245", "issue_key": "PLAT-9120"},
   "Tag Manager": {"project": "10317", "issue_key": "SPP-1080"},
   "telemetry-gateway": {"project": "10322", "issue_key": "EPPS-5253"},
   "Vig-app": {"project": "10318", "issue_key": "VGL-1851"}           
}

def create_epic_and_clone_stories():
    try:
        # Your authentication token
        jira_token = {
            'Server': 'https://sentinelone.atlassian.net/',
            'username': 'ENTERCORPEMAILHERE',
            'credential': 'ENTERAPITOKENHERE'
        }

        # Authenticate
        jira = JIRA(server=jira_token['Server'], basic_auth=(jira_token['username'], jira_token['credential']), options={'server': 'https://sentinelone.atlassian.net/', 'server_info': {'server_url': 'https://sentinelone.atlassian.net/'}})

        # Prompt user for PI variable
        pi_variable = input("Enter the value for PI: ")

        # Create Epic
        epic_summary = f"Base Image Uplift - {pi_variable}"
        epic = jira.create_issue(project=EPIC_PROJECT_KEY, summary=epic_summary, issuetype={'name': 'Epic'})

        # Echo the name of the created epic
        print(f"Epic created: {epic.key} - {epic_summary}")

        # Iterate through each component and clone stories
        for component, details in STORY_PROJECT_KEYS.items():
            project_key = details["project"]
            issue_key = details["issue_key"]
            print(f"Cloning story for {component} (Issue Key: {issue_key}) in Project: {project_key}...")

            # Clone the issue from the specified project and clone it into the same project
            original_issue = jira.issue(issue_key)

            # Extract the value of the ;labels and 'Team' field
            labels = original_issue.fields.labels
            team_field_value = original_issue.fields.customfield_11067
            team_field = {"id": team_field_value.id, "value": team_field_value.value}

            # Create the new issue and set the custom field value, summary
            cloned_issue = jira.create_issue(
                summary=f"{component} - Base Image Update Required - FedRAMP Deployment Ticket Request",
                description="The base image for this component is out-of-date. To mitigate vulnerabilities and remain within FedRAMP policy compliance, these base images should be updated at least once per month. Please provide FedRAMP with a new build of the component on the latest base image and submit a FedRAMP deployment ticket with the details for that new version. The template to be used for that deployment ticket is located here:\n\nFEDRAMP-2764: [TEMPLATE][FedRAMP Deployment] <deployable unit> - <version>\n\nPlease reach out to Tim Levesque, Barry Berard, or Joel Stewart if you have any questions.",
                project=project_key,
                issuetype={'name': 'Story'},
                customfield_11067=team_field,
                labels=labels
            )
             # Add the label "FRH-BaseImage" to the cloned ticket
            jira.add_issues_to_epic(epic.key, [cloned_issue.key])

            # Link cloned issue to the epic
            print(f"Cloned Story: {cloned_issue.key} - {cloned_issue.fields.summary}")

            # Set the Parent Link field for the cloned ticket to the epic
            jira.create_issue_link('is child of', cloned_issue, epic)

            # Ask user if they want to continue with the next component, skip, or stop - This can be uncommented for troubleshooting.
            #continue_script = input("Do you want to continue with the next component (Y), skip the next component (S), or stop (N)? ").strip().upper()
            #if continue_script == 'S':
            #    print("Skipping the next component.")
            #    continue  # Skip the next component and continue with the loop
            #elif continue_script == 'N':
            #    print("Stopping the script.")
            #    break  # Exit the loop if the user wants to stop

    except JIRAError as e:
        print(f"Jira API call failed. Error: {e}")

if __name__ == "__main__":
    create_epic_and_clone_stories()
