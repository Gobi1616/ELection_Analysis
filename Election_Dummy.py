Python 3.7.9 (v3.7.9:13c94747c7, Aug 15 2020, 01:31:08) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>>  voting_data.append({"county":"Denver", "registered_voters": 463353})
 
SyntaxError: unexpected indent
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data.append({"county":"El Paso", "registered_voters": 461149})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 461149}]
>>> voting_data,pop(0)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    voting_data,pop(0)
NameError: name 'pop' is not defined
>>> voting_data.pop(0)
{'county': 'Arapahoe', 'registered_voters': 422829}
>>> voting_data
[{'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 461149}]
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data
[{'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Arapahoe', 'registered_voters': 422829}]
>>> 