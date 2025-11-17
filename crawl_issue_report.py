
import requests
from datetime import datetime

# Jira rest API address.
url = "https://issues.apache.org/jira/rest/api/2/issue/CAMEL-10597"
response = requests.get(url)

# If the request is successful, then parse JSON data.
if response.status_code == 200:
    issue_data = response.json()

    # Here are some properties to be saved to a database.
    Type = issue_data["fields"]["issuetype"]["name"]
    Priority = issue_data["fields"]["priority"]["name"]
    # Parse the components list to get all components.
    components_list = issue_data["fields"]["components"]
    Components = ""
    for one_component in components_list:
        Components = Components + one_component["name"] + ", "    
    Components = Components.rstrip(", ")

    Status = issue_data["fields"]["status"]["name"]
    Resolution = issue_data["fields"]["resolution"]["name"]

    Assignee = issue_data["fields"]["assignee"]["displayName"]
    Reporter = issue_data["fields"]["reporter"]["displayName"]
    Votes = issue_data["fields"]["votes"]["votes"]
    Watchers = issue_data["fields"]["watches"]["watchCount"]

    Created = issue_data["fields"]["created"]
    Updated = issue_data["fields"]["updated"]
    Resolved = issue_data["fields"]["resolutiondate"]
    
    Description = issue_data["fields"]["description"]

    # Generate formatted comments
    # First, get all comments data in JSON.
    all_comments = issue_data["fields"]["comment"]["comments"]
    # It's the list of all comments to save in database.
    all_comments_list_to_save = []
    # Iterate over each comment.
    for one_comment_dict in all_comments:
        # Get the creation time string of this comment.
        creation_time_string = one_comment_dict["created"]
        # Get the year, month, day, hour, minute, second.
        creation_year = int(creation_time_string[0:4])
        creation_month = int(creation_time_string[5:7])
        creation_day = int(creation_time_string[8:10])
        creation_hour = int(creation_time_string[11:13])
        creation_minute = int(creation_time_string[14:16])
        creation_second = int(creation_time_string[17:19])
        # Create a datetime object.
        comment_created_datetime_object = datetime(creation_year, creation_month, creation_day, creation_hour, creation_minute, creation_second)
        # Get the formatted time string.
        formatted_datetime = comment_created_datetime_object.strftime("%d/%b/%y %H:%M")
        # combine to get the desired comment content to save.
        one_formatted_comment_to_save = one_comment_dict["author"]["displayName"] + ":" + formatted_datetime + ":\"" + one_comment_dict["body"]
        # Append one comment to the list.
        all_comments_list_to_save.append(one_formatted_comment_to_save)

    print("Details part starts here: ")
    print("Type: ", Type)
    print("Priority: ", Priority)
    print("Component/s: ", Components)
    print("Status: ", Status)
    print("Resolution: ", Resolution)

    print("People part starts here: ")
    print("Assignee:", Assignee)
    print("Reporter: ", Reporter)
    print("Votes: ", Votes, type(Votes))
    print("Watchers: ", Watchers, type(Watchers))

    print("Dates part starts here!")
    print("Created: ", Created, type(Created))
    print("Updated: ", Updated, type(Updated))
    print("Resolved: ", Resolved, type(Resolved))

    print("Description part starts here!")
    print("Description: ", Description)
    print("Description type: ", type(Description))

    print("Comments part starts here!")
    print("Comments: ", all_comments_list_to_save, type(all_comments_list_to_save))
    
    # print("*******************************************************")
    # print(json.dumps(issue_data, indent=2))
else:
    # If there are some problems, print the returned status code.
    print("Error: ", response.status_code)