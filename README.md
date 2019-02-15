# miniTWOWBot
![](https://img.shields.io/travis/kcomain/TWOWBot-Hacked.svg?style=flat)

### How to use TWOWBot:
#### Hosting an mTWOW:
The host of an mTWOW has a couple of commands for them to use:
* **`set_prompt`** will set the prompt for the round.
* **`responses`** will send you a DM listing all of the responses so far.
* **`start_voting`** will then close responses and allow people to vote.
* Finally, **`results`** will end the round and show results
* You can also use **`transfer`** to make someone else the host of the mTWOW.
#### Traditional mTWOWs:
The owner of a mTWOW can setup a traditional mTWOW where anyone can host:
* **`can_queue on`** will allow people to join the hosting queue with **`join_queue`**.
* **`queue_timer`** will allow you to set a timer for the events.
* Use **`help queue_timer`** for help.
* **`skip_host`** will skip the current host and start a fresh season.
#### Participating in an mTWOW:
When you are participating, you also have some commands you can use:
* **`respond`**, when in a DM, allows you to respond to a prompt.
* **`vote`**, when in a DM, will first generate your voting slide, and then
allow you to vote on it.
#### Other useful commands:
There are a few commands that are useful to know:
* **`prompt`** will show you the current prompt.
* **`round`** and **`season`** will tell you the round and season number
respectively.
* **`id`** will get you the channel identifier for that mTWOW. This is needed
when responding or voting.
#### Getting help:
All of these commands, and more, are available in the **`help`** command.
If you want to invite the bot to your server, or join the official one, use **`about`**.
If you are interested in hosting this bot for yourself, check the GitHub linked in the **`about`** command,
or DM one of the developers (also in the **`about`** command).

---
### All commands:
| command        | brief description |
| -------------- | ----------------- |
| `round`        | Get the current round number. |
| `sudo`         | Run a command ignoring every check. |
| `evaluate`     | Run some code. |
| `vote`         | Vote on the responses. |
| `die`          | Disconnects the bot. |
| `respond`      | Respond to the current prompt. |
| `say`          | Get te bot to say something. |
| `help`         | This help message :D |
| `ping`         | Ping the bot. |
| `id`           | Get the server ID used in voting. |
| `role_ids`     | Get all of the role ids for the server. |
| `about`        | Get info about the bot. |
| `me`           | Get info about yourself. |
| `prompt`       | Get the current prompt. |
| `how`          | Get instructions on hosting a mTWOW. |
| `season`       | Get the current season number. |
| `register`     | Setup channel initially. |
| `show_config`  | Sends the config file for this channel. |
| `set_times`    | Set timer for next events.  Events are voting and results. |
| `set_prompt`   | Set the prompt for this round. |
| `start_voting` | Start voting. |
| `transfer`     | Transfer ownership of this mTWOW. |
| `results`      | End this round and show results. |
| `delete`       | Delete the mTWOW. |
| `responses`    | List all responses this round. |

To get indepth help into any of these commands including what arguments they
require and who can use them, use the `help` command.
