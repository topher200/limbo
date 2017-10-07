# Limbo
### A [Slack](https://slack.com/) chatbot

## Installation

1. Clone the repo
2. [Create a bot user](https://my.slack.com/services/new/bot) if you don't have one yet, and copy the API Token
3. Set up your .env (see Environment Variables below)
4. `make run` (or `make repl` for local testing)
5. Invite Limbo into any channels you want it in, or just message it in #general. Try typing `!gif dubstep cat` to test it out

## Command Arguments

* --test, -t: Enter command line mode to enter a limbo repl.
* --hook: Specify the hook to test. (Defaults to "message").
* -c: Run a single command.
* --database, -d: Where to store the limbo sqlite3 database. Defaults to limbo.sqlite3.
* --pluginpath, -pp: The path where limbo should look to find its plugins (defaults to /plugins).

## Environment Variables

Create a .env file with these variables:
* SLACK_TOKEN: Slack API token. Required.
* WORDY_GIT_REPO_URL: Required for the 'tag' plugin. declares the git repo.  example: 'ssh://username@git.domain.com/srv/git/repo_name.git'
* LIMBO_LOGLEVEL: The logging level. Defaults to INFO.
* LIMBO_LOGFILE: File to log info to. Defaults to none.
* LIMBO_LOGFORMAT: Format for log messages. Defaults to `%(asctime)s:%(levelname)s:%(name)s:%(message)s`.
* LIMBO_PLUGINS: Comma-delimited string of plugins to load. Defaults to loading all plugins in the plugins directory (which defaults to "limbo/plugins")

## Commands

It's super easy to add your own commands! Just create a python file in the plugins directory with an `on_message` function that returns a string.

You can use the `!help` command to print out all available commands and a brief help message about them. `!help <plugin>` will return just the help for a particular plugin.
