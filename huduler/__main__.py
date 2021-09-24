"""Command line interface"""
# stdlib
from datetime import date, time
from pathlib import Path
from textwrap import dedent
# 3rd party
import click
import yaml
from yaml.loader import SafeLoader
# local



def open_actions_yaml(file_path:str) -> dict:
    action_list_path = Path(file_path)
    with open(action_list_path, 'rt') as file_obj:
        data = yaml.load(file_obj, Loader=SafeLoader)
    return data


def filter_days_actions(day:date, actions_data:dict) -> list[dict]:
    # holds list of todays actions
    todays_actions = []

    for action in actions_data['actions']:
        action_repeat = action['repeat']

        if action_repeat.lower() in ['everyday', day.strftime('%A').lower()]:
            # action due on this date
            todays_actions.append(action)
        # else action isn't due on this date.

    return todays_actions


def ordered_actions(actions:list[dict]) -> list[dict]:
    """Order the list of actions by the order key.
    Drops action that have no order value.
    """
    acts_with_order = filter(lambda act: act.get('order'), actions)
    return sorted(acts_with_order, key=lambda act: act['order'])


def time_ordered_actions(actions:list[dict]) -> list[dict]:
    """Order the list of actions by the time key.
    Drops action that have no time value.
    """
    acts_with_time = filter(lambda act: act.get('time'), actions)
    return sorted(acts_with_time, key=lambda act: time.fromisoformat(act['time']))


def orderless_actions(actions:list[dict]) -> list[dict]:
    """Get the list of actions that have neither a time or order key."""
    return list(filter(lambda act: not(act.get('time') or act.get('order')), actions))


def day_sheet_markdown(day:date,
                       ordered_actions: list[dict]=None,
                       time_ordered_actions: list[dict]=None,
                       orderless_actions: list[dict]=None) -> str:
    """Get the daysheet in markdown format with the actions
    """
    mkd = f"""
    # {day.strftime('%A')} {day.isoformat()}

    """
    mkd = dedent(mkd)

    for count, action in enumerate(ordered_actions, start=1):
        sliver = f"""
        ## {count}. {action.get('name')}

        {action.get('description')}

        Repeats: {action.get('repeat')}
        """
        mkd += dedent(sliver)

    for action in time_ordered_actions:
        sliver = f"""
        ## {action['time']}HR: {action.get('name')}

        {action.get('description')}

        Repeats: {action.get('repeat')}
        """
        mkd += dedent(sliver)

    for action in orderless_actions:
        sliver = f"""
        ## {action.get('name')}

        {action.get('description')}

        Repeats: {action.get('repeat')}
        """
        mkd += dedent(sliver)

    return mkd


@click.command()
@click.argument('action-list')
def main(action_list:str):
    """Provide an action list file to build the day sheet from
    """
    today = date.today()
    data = open_actions_yaml(file_path=action_list)
    todays_act = filter_days_actions(day=today, actions_data=data)
    # Don't yet care if action appears in multiple lists...
    ordered_acts = ordered_actions(actions=todays_act)
    time_ordered_acts = time_ordered_actions(actions=todays_act)
    orderless_acts = orderless_actions(actions=todays_act)

    markdown = day_sheet_markdown(day=today,
                                  ordered_actions=ordered_acts,
                                  time_ordered_actions=time_ordered_acts,
                                  orderless_actions=orderless_acts)

    print(markdown)

if __name__ == '__main__':
    main()