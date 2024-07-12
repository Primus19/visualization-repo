
from jira import JIRA
from jira.exceptions import JIRAError

# Static project and issue keys
EPIC_PROJECT_KEY = "FEDRAMP"
STORY_PROJECT_KEYS = [
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10091",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: vig-app-prod\nImage Name: mgmt-entities-loader\nAge in Days: 486\nOwner: VigApp\n",
        "owner": "VigApp",
        "epic_key": "FEDRAMP-10091",
        "clone_links": True
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10092",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: vig-app-prod\nImage Name: vig-app-backend\nAge in Days: 486\nOwner: VigApp\n",
        "owner": "VigApp",
        "epic_key": "FEDRAMP-10091",
        "clone_links": True
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10093",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: vig-app-prod\nImage Name: vig-app-frontend-react\nAge in Days: 486\nOwner: VigApp\n",
        "owner": "VigApp",
        "epic_key": "FEDRAMP-10091",
        "clone_links": True
    }
    # Add more entries as required...
]

def create_epic_and_clone_stories():
    try:
        # Initialize Jira connection
        jira_token = {
            "username": "primus.vterst",
            "credential": "test"
        }
        jira = JIRA(basic_auth=(jira_token['username'], jira_token['credential']), options={'server': 'https://sentinelone.atlassian.net/'})

        # Prompt user for PI variable
        pi_variable = input("Enter the value for PI: ")

        # Create Epic
        epic_summary = f"Base Image Uplift - {pi_variable}"
        epic = jira.create_issue(project=EPIC_PROJECT_KEY, summary=epic_summary, issuetype={'name': 'Epic'})

        # Echo the name of the created epic
        print(f"Epic created: {epic.key} - {epic_summary}")

        # Iterate through each component and clone stories
        for details in STORY_PROJECT_KEYS:
            project_key = details["project"]
            issue_key = details["issue_key"]
            print(f"Cloning story (Issue Key: {issue_key}) in Project: {project_key}...")

            # Clone the issue from the specified project and clone it into the same project
            original_issue = jira.issue(issue_key)

            # Extract the value of the 'labels' and 'Team' field
            labels = original_issue.fields.labels
            team_field_value = original_issue.fields.customfield_11067
            team_field = {"id": team_field_value.id, "value": team_field_value.value}

            # Create the new issue and set the custom field value, summary
            cloned_issue = jira.create_issue(
                summary=f"{details['summary']} - Base Image Update Required - FedRAMP Deployment Ticket Request",
                description=original_issue.fields.description + details['description'],
                project=project_key,
                issuetype={'name': 'Story'},
                customfield_11067=team_field,
                customfield_11406=True,  # Assuming 'Is Capitalized' is a boolean field
                labels=labels
            )

            # Add the cloned issue to the epic
            jira.add_issues_to_epic(epic.key, [cloned_issue.key])

            # Link cloned issue to the epic
            print(f"Cloned Story: {cloned_issue.key} - {cloned_issue.fields.summary}")

            # Set the Parent Link field for the cloned ticket to the epic
            jira.create_issue_link('is child of', cloned_issue, epic)

            # Ask user if they want to continue with the next component, skip, or stop
            # This can be uncommented for troubleshooting.
            # continue_script = input("Do you want to continue with the next component (Y), skip the next component (S), or stop (N)? ").strip().upper()
            # if continue_script == 'S':
            #     print("Skipping the next component.")
            #     continue  # Skip the next component and continue with the loop
            # elif continue_script == 'N':
            #     print("Stopping the script.")
            #     break  # Exit the loop if the user wants to stop

    except JIRAError as e:
        print(f"Jira API call failed. Error: {e}")

if __name__ == "__main__":
    create_epic_and_clone_stories()
