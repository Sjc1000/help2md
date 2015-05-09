#sjBot



##bot
```python
class bot():
	"""No documentation"""
```

###__init__
```python
	def __init__(self, network, port, rejoin=1):
		"""__init__
		params:
		    - network - The network for the bot to join.
		    - port    - The port for the bot to join on.
		    - rejoin  - Should the bot attempt to rejoin if he disconnects."""
```

###handle_data
```python
	def handle_data(self, data):
		"""handle_data
		Handles incoming data from the main_loop()
		params:
		    - data - The data recieved from IRC."""
```

###ident
```python
	def ident(self):
		"""ident
		Identifies the bot. If a password has been set."""
```

###join
```python
	def join(self, channel):
		"""join
		Joins a channel.
		params:
		    - channel - The channel to join."""
```

###leave
```python
	def leave(self, channel):
		"""leave
		Leaves a channel.
		params:
		    - channel - The channel to leave."""
```

###main_loop
```python
	def main_loop(self):
		"""main_loop
		The main data recieving loop.
		This loop handles all the data and then sends it to self.handle_data()"""
```

###make_connection
```python
	def make_connection(self):
		"""make_connection
		Attemps to make 10 connections to IRC.
		Starts at 10 seconds between delay attempts and goes up to 100."""
```

###notify
```python
	def notify(self, user, data):
		"""notify
		Sends a NOTICE to IRC.
		params:
		    - user - The user to send to NOTICE to.
		    - data - The data to send to the user."""
```

###on376
```python
	def on376(self, *params):
		"""on376
		End of MOTD."""
```

###on433
```python
	def on433(self, host, p, nickname, *params):
		"""on443
		When the current nickname is already taken.
		params:
		    - host     - The host of the IRC network we are on.
		    - p        - Just a asterix, nothing special.
		    - nickname - The nickname that is taken.
		    - params   - The words This nickname is in use. Or something
		                    similar."""
```

###onALL
```python
	def onALL(self, *params):
		"""onALL
		Creates this so the bot has somewhere to send the data if the parent
		    doesn't have onALL"""
```

###onPING
```python
	def onPING(self, host):
		"""onPING
		Happens when the bot finds a PING message."""
```

###privmsg
```python
	def privmsg(self, channel, data):
		"""privmsg
		Sends a PRIVMSG to IRC.
		params:
		    - channel - The channel to send the privmsg to.
		    - data    - The data to send in the privmsg."""
```

###send
```python
	def send(self, data):
		"""send
		Sends data to IRC.
		params:
		    - data - The data to send to IRC. Automatically appends a newline
		                to the end."""
```

###shutdown
```python
	def shutdown(self, force=0):
		"""shutdown
		Called when the bot looses connection to IRC."""
```

###startup
```python
	def startup(self, nickname='sjBot', user='sjBot', host='sjBot', realname='Uptone Software/sjBot'):
		"""startup
		called right after the IRC connects."""
```

##pprint
```python
def pprint(data, color=None, background=None, prefix=' ', suffix='\r\n', timestamp=1, timecolor='purple'):
	"""No documentation"""
```

##sjBot
```python
class sjBot():
	"""No documentation"""
```

###__init__
```python
	def __init__(self, keyfile='keys'):
		"""No documentation"""
```

###download_url
```python
	def download_url(self, url):
		"""No documentation"""
```

###getsettings
```python
	def getsettings(self):
		"""No documentation"""
```

###handle_data
```python
	def handle_data(self, data):
		"""handle_data
		Handles incoming data from the main_loop()
		params:
		    - data - The data recieved from IRC."""
```

###ident
```python
	def ident(self):
		"""ident
		Identifies the bot. If a password has been set."""
```

###is_command
```python
	def is_command(self, command):
		"""No documentation"""
```

###iterate
```python
	def iterate(self, timeout=60):
		"""No documentation"""
```

###join
```python
	def join(self, channel):
		"""join
		Joins a channel.
		params:
		    - channel - The channel to join."""
```

###leave
```python
	def leave(self, channel):
		"""leave
		Leaves a channel.
		params:
		    - channel - The channel to leave."""
```

###load_plugins
```python
	def load_plugins(self, plugin_folder):
		"""No documentation"""
```

###main_loop
```python
	def main_loop(self):
		"""main_loop
		The main data recieving loop.
		This loop handles all the data and then sends it to self.handle_data()"""
```

###make_connection
```python
	def make_connection(self):
		"""make_connection
		Attemps to make 10 connections to IRC.
		Starts at 10 seconds between delay attempts and goes up to 100."""
```

###notify
```python
	def notify(self, user, data):
		"""notify
		Sends a NOTICE to IRC.
		params:
		    - user - The user to send to NOTICE to.
		    - data - The data to send to the user."""
```

###on376
```python
	def on376(self, host, *params):
		"""No documentation"""
```

###on396
```python
	def on396(self, host, chost, *params):
		"""No documentation"""
```

###on433
```python
	def on433(self, host, ast, nickname, *params):
		"""No documentation"""
```

###on730
```python
	def on730(self, host, nickname, ohost):
		"""No documentation"""
```

###on731
```python
	def on731(self, host, nickname, ohost):
		"""No documentation"""
```

###onALL
```python
	def onALL(self, *params):
		"""No documentation"""
```

###onPING
```python
	def onPING(self, host):
		"""onPING
		Happens when the bot finds a PING message."""
```

###onPRIVMSG
```python
	def onPRIVMSG(self, uhost, channel, *message):
		"""No documentation"""
```

###privmsg
```python
	def privmsg(self, channel, data):
		"""privmsg
		Sends a PRIVMSG to IRC.
		params:
		    - channel - The channel to send the privmsg to.
		    - data    - The data to send in the privmsg."""
```

###send
```python
	def send(self, data):
		"""send
		Sends data to IRC.
		params:
		    - data - The data to send to IRC. Automatically appends a newline
		                to the end."""
```

###shorten_url
```python
	def shorten_url(self, url):
		"""No documentation"""
```

###shutdown
```python
	def shutdown(self, force=0):
		"""shutdown
		Called when the bot looses connection to IRC."""
```

###start_monitor
```python
	def start_monitor(self):
		"""No documentation"""
```

###startup
```python
	def startup(self):
		"""No documentation"""
```

# Dependencies
- imp
- json
- os
- sys
- threading
- time
- urllib

***Made with help2md***