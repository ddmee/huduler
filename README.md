# Huduler

Human scheduler. Create a (master) list of reoccurring actions and generate daily action sheets from that master list.

## Innovocation

```shell
cd huduler
pipenv install
pipenv run python -m huduler examples/actions.yaml > examples/today.markdown
```

## Examples of output

See `examples/` directory, of a daily sheet output as markdown produced from the actions.yaml.

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
    completion_score: 10
    failure_score: 5

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

## Completion and failure scores

You can assign completion and failure scores to an action. This allows you to build up an action score over time, of how well you are sticking to the actions. Generally, we want to reward ourselves more than punishing ourselves, so it's probably better to make the completition scores a little bit larger than the failure scores, tilting the scoring in your favour.

For example:

```yaml

  - name: "Black Coffee"
    description: "Continue morning fast. Stop coffee at noon."
    repeat: "Everyday"
    order: "2"
    time: ""
    completion_score: 10
    failure_score: 5

  - name: "No junk food"
    description: ""
    repeat: "everyday"
    order: ""
    time: ""
    completion_score: 15
    failure_score: 5

  - name: "Avoid reading the news"
    description: "It's too antagonising."
    repeat: "everyday"
    order: ""
    time: ""
    completion_score: 5
    failure_score: 0

```

The completion scores above value some actions more than others. And some actions are entirely optional, like a bonus score, that if you don't complete have no negative impact.

## Keys

order: the lower the number, the higher the priority. Makes the action appear in the list of ordered actions.

time: the time of day the action is to be carried out. Note, please use 24hour iso-format for the time. E.g. '23:53' or '09:06'.

completion_score: the number of points you gain if you complete this action today

failure_score: the number of points you loose if you fail this action today.
