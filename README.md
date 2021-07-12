# After Hour Teams Backend

_Updated Sunday July 11th 2021 by [cassioblu55](https://github.com/cassioblu55)_

_responding to [this](https://github.com/Daupler/coding-challenge) assessment_


## First Time Developer Setup

## Install Dependencies 

```bash
pipenv install
```

**pipenv** is required to be installed, it is used for dependency management  

## Start Virtual Environment

Activate your virtual environment to ensure every subsequent command will use the virtual environment using pipenv:

```bash
pipenv shell
```

## Ensure Database is Up to Date

```bash
./manage.py migrate
```

This will update your local database with the current db models.

## Start localhost

Now, in the terminal start the Django server by running, this project should run on port 8000:

```bash
./manage.py runserver
```

## Testing

Run tests. Development/QA/Production will not deploy if unit tests are failing.

```bash
pipenv install --dev
pipenv run pytest
```


# Requirements
1. View a list of teams, including their members
    1. List of all teams by sending `GET` request to: `localhost:8000/teams`
    2. Get the list of team members by sending a `GET` request to: `localhost:8000/teams/1` where `1` is the id of the team
2. Create new teams
    1. Send a `POST` request to: `localhost:8000/teams/` **Note** the ending '/' is **required**
3. Add/remove team members
    1. To add a team member send a `POST` request to: `localhost:8000/teams/member/`
    2. To delete a team member send a `DELETE` request to `localhost:8000/teams/member/1` where `1` is the team member id
4. Swap two team member's position
    1. Send `POST` request to `localhost:8000/teams/swap/` **Note** the ending '/' is **required**

## Additional Features
1. Notify team member
    1. First create an `event`, send a `POST` request to: `localhost:8000/event/`  **Note** the ending '/' is **required**
    2. You will set the team assignment at the time of `event` creation
    3. To perform the team notification logic send a `POST` request to: `localhost:8000/event/1/call` where `1` is the event id
    4. **Note** no notification will actually be sent, a record of the call being sent will be created 