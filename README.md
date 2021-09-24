# Huduler

Human scheduler. Create a (master) list of re-occuring actions and generate daily action sheets from that master list.

## Innovocation

```shell
cd huduler
pipenv install
pipenv run python -m huduler actions.yaml > today.markdown
```


## Create an Actions list

Create an actions.yaml file. This is a list of actions, describing how often they ought to be repeated and in what priority. From the actions list, a day-sheet is produced every day. The actions due on that day, say Monday, are put into the day-sheet.

```yaml
# Action list

actions:
  - name: ""
    description: ""
    repeat: ""
    order: ""
    time: ""

  - name: ""
    description: ""
    repeat: ""
    order: ""
    time: ""

```

An action is just a set of keys. As a concrete example, you might have a list of actions like this:

```yaml
actions:
  - name: "Morning Weigh-In"
    description: "Weigh yourself on the bathroom scales, first thing in the morning, before anything else."
    repeat: "Everyday"
    order: "1"
    time: ""

  - name: ""
    description: ""
    repeat: ""
    order: ""
    time: ""

```

## Create a day sheet from an action list

For every new calendar day, Huduler will create a day-sheet specific to that day. The day-sheet is drawn from the actions list.

There are three types of action lists for a day:

1. Priority ordered action list
2. Time ordered action list
3. Orderless action list

The priority ordered action list looks at the 'order' key to determine an actions place in this list.

The time-ordered action list looks at the 'time' key to determine an actions place in this list.

The orderless action list is for any actions that are due on this day but have no time or priority order.

## Keys

Order: the lower the number, the higher the priority. Makes the action appear in the list of ordered actions.

Time: the time of day the action is to be carried out. Note, please use 24hour iso-format for the time. E.g. '23:53' or '09:06'.