strawpoll-python
================

Python Wrapper to Automate Making a StrawPoll


Requirements:
Built on Python 2.7
Uses built-in modules, `requests` and `re` (regex)


## Usage

#####Create new poll
```python
from strawpoll import StrawPoll

s = StrawPoll.new("new poll", ["Option 1", "Option 2"])
```

#####Get old poll by id
```python
t = StrawPoll.fromID(142857)
```

#####Get old poll by url
```python
v = StrawPoll.fromURL("http://strawpoll.me/314159")
```

#####Access results
```python
s = StrawPoll.new("new poll", ["Option 1", "Option 2"])
print s.url
print s.title
print s.results
print s.totalVotes
```

#####Update results
Call this to update values. Note: The poll is updated upon initialization.
```python
s.updateResults()
```

