import json
import os

# file where all meeting tasks will be stored
TASK_FILE = "tasks.json"


def save_tasks(meeting_name, tasks):
    """
    Save tasks for a specific meeting

    Why?
    Earlier:
    - all meetings tasks were getting mixed together

    Now:
    - each meeting gets its own task list
    """

    # check if tasks.json already exists
    if os.path.exists(TASK_FILE):

        # open existing file and load old meeting tasks
        with open(TASK_FILE, "r") as f:
            all_tasks = json.load(f)

    else:
        # first time → create empty dictionary
        all_tasks = {}

    # store current meeting tasks using meeting file name
    # example:
    # "team_meeting.mp4": [task1, task2]
    all_tasks[meeting_name] = tasks

    # save updated data back into tasks.json
    with open(TASK_FILE, "w") as f:
        json.dump(all_tasks, f, indent=4)


def load_tasks():
    """
    Load all saved meeting tasks
    """

    if os.path.exists(TASK_FILE):

        with open(TASK_FILE, "r") as f:
            return json.load(f)

    return {}


def get_pending_tasks(meeting_name):
    """
    Return only pending tasks
    for current meeting

    Why?
    We don't want tasks from old meetings
    showing in new meeting UI
    """

    # load all meetings data
    all_tasks = load_tasks()

    # get tasks for current meeting only
    meeting_tasks = all_tasks.get(meeting_name, [])

    # filter only pending tasks
    pending_tasks = [
        task for task in meeting_tasks
        if task["status"] == "pending"
    ]

    return pending_tasks