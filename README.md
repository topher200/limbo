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

By default, plugins won't react to messages from other bots (just messages from humans). Define an `on_bot_message` function to handle bot messages too. See the example plugins for an easy way to define these functions.

These are the current default plugins (only a few are enabled for Wordy):

* [calc](https://github.com/llimllib/limbo/wiki/Calc-Plugin)
* [emoji](https://github.com/llimllib/limbo/wiki/Emoji-Plugin)
* [flip](https://github.com/llimllib/limbo/wiki/Flip-Plugin)
* [gif](https://github.com/llimllib/limbo/wiki/Gif-Plugin)
* [google](https://github.com/llimllib/limbo/wiki/Google-Plugin)
* [help](https://github.com/llimllib/limbo/wiki/Help-Plugin)
* [image](https://github.com/llimllib/limbo/wiki/Image-Plugin)
* [map](https://github.com/llimllib/limbo/wiki/Map-Plugin)
* [stock](https://github.com/llimllib/limbo/wiki/Stock-Plugin)
* [stockphoto](https://github.com/llimllib/limbo/wiki/Stock-Photo-Plugin)
* [weather](https://github.com/llimllib/limbo/wiki/Weather-Plugin)
* [wiki](https://github.com/llimllib/limbo/wiki/Wiki-Plugin)
* [youtube](https://github.com/llimllib/limbo/wiki/Youtube-Plugin)

## Contributors

* [@fsalum](https://github.com/fsalum)
* [@rodvodka](https://github.com/rodvodka)
* [@mattfora](https://github.com/mattfora)
* [@dguido](https://github.com/dguido)
* [@JoeGermuska](https://github.com/JoeGermuska)
* [@MathyV](https://github.com/MathyV)
* [@stopspazzing](https://github.com/stopspazzing)
* [@noise](https://github.com/noise)
* [@drewp](https://github.com/drewp)
* [@TetraEtc](https://github.com/TetraEtc)
* [@LivingInSyn](https://github.com/LivingInSyn)
* [@reversegremlin](https://github.com/reversegremlin)
* [@adamghill](https://github.com/adamghill)
* [@PeterGrace](https://github.com/PeterGrace)
* [@SkiftCreative](https://github.com/SkiftCreative)
* [@diceone](https://github.com/diceone)
* [@rnagle](https://github.com/rnagle)
* [@topher200](https://github.com/topher200)
* [@StewPoll](https://github.com/StewPoll)
