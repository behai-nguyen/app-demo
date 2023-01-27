"""
JSON dumps route.
"""
from flask import render_template

import simplejson as json

def do_json_dumps():
    # 
    # This commented out codes should work the same as the active codes.
    #
    # timesheet = '{"status": {"code": 200, "text": ""}, "data": {"timesheet": [{"TIMESHEET_ID": 327, "CONTRACTOR_ID": 67, "TEMPLATE_ID": null, "PERIOD_START": "03/01/2022", "PERIOD_END": "06/01/2022", "CLIENT_ID": 2, "CLOSED": 0, "CLIENT_NAME": "ACME Pty Ltd", "TEMPLATE_NAME": null, "CONTRACTOR_NAME": "User Test"}], "task_data": [{"TASK_ID": 2, "CLIENT_TASK_ID": "xxx", "PROJECT_ID": 2, "NAME": "Development and testing"}], "timesheet_entries": [{"TSE_ID": 4383, "TIMESHEET_ID": 327, "TASK_ID": 2, "PERIOD_DATE": "03/01/2022", "START_HOUR": 1, "START_MINUTE": 23, "START_MERIDIEM": "AM", "FINISH_HOUR": 4, "FINISH_MINUTE": 45, "FINISH_MERIDIEM": "AM", "BREAK_HOUR": 0, "BREAK_MINUTE": 22, "DURATION_HOUR": 3, "DURATION_MINUTE": 0, "CHARGEABLE": 1, "DESCRIPTION": ""}, {"TSE_ID": 4398, "TIMESHEET_ID": 327, "TASK_ID": 2, "PERIOD_DATE": "04/01/2022", "START_HOUR": 3, "START_MINUTE": 24, "START_MERIDIEM": "AM", "FINISH_HOUR": 6, "FINISH_MINUTE": 34, "FINISH_MERIDIEM": "AM", "BREAK_HOUR": 0, "BREAK_MINUTE": 10, "DURATION_HOUR": 3, "DURATION_MINUTE": 0, "CHARGEABLE": 1, "DESCRIPTION": ""}, {"TSE_ID": 4442, "TIMESHEET_ID": 327, "TASK_ID": 2, "PERIOD_DATE": "05/01/2022", "START_HOUR": 1, "START_MINUTE": 12, "START_MERIDIEM": "AM", "FINISH_HOUR": 3, "FINISH_MINUTE": 23, "FINISH_MERIDIEM": "AM", "BREAK_HOUR": 0, "BREAK_MINUTE": 11, "DURATION_HOUR": 2, "DURATION_MINUTE": 0, "CHARGEABLE": 1, "DESCRIPTION": ""}, {"TSE_ID": 4451, "TIMESHEET_ID": 327, "TASK_ID": 2, "PERIOD_DATE": "06/01/2022", "START_HOUR": 2, "START_MINUTE": 11, "START_MERIDIEM": "AM", "FINISH_HOUR": 6, "FINISH_MINUTE": 23, "FINISH_MERIDIEM": "AM", "BREAK_HOUR": 0, "BREAK_MINUTE": 12, "DURATION_HOUR": 4, "DURATION_MINUTE": 0, "CHARGEABLE": 1, "DESCRIPTION": ""}], "timesheet_totals": [{"TOTAL_HOURS": 12, "TOTAL_MINUTES": 0, "ROUNDED_TOTAL_HOURS": 12.0}]}}'
    # return render_template( 'json/json_dumps.html', json_obj=json.loads(timesheet) )

    timesheet = {"status": {"code": 200, "text": ""}, "data": {"timesheet": [{"TIMESHEET_ID": 327, "CONTRACTOR_ID": 67, "TEMPLATE_ID": None, "PERIOD_START": "03/01/2022", "PERIOD_END": "06/01/2022", "CLIENT_ID": 2, "CLOSED": 0, "CLIENT_NAME": "ACME Pty Ltd", "TEMPLATE_NAME": None, "CONTRACTOR_NAME": "User Test"}], "task_data": [{"TASK_ID": 2, "CLIENT_TASK_ID": "xxx", "PROJECT_ID": 2, "NAME": "Development and testing"}], "timesheet_entries": [{"TSE_ID": 4383, "TIMESHEET_ID": 327, "TASK_ID": 2, "PERIOD_DATE": "03/01/2022", "START_HOUR": 1, "START_MINUTE": 23, "START_MERIDIEM": "AM", "FINISH_HOUR": 4, "FINISH_MINUTE": 45, "FINISH_MERIDIEM": "AM", "BREAK_HOUR": 0, "BREAK_MINUTE": 22, "DURATION_HOUR": 3, "DURATION_MINUTE": 0, "CHARGEABLE": 1, "DESCRIPTION": ""}, {"TSE_ID": 4398, "TIMESHEET_ID": 327, "TASK_ID": 2, "PERIOD_DATE": "04/01/2022", "START_HOUR": 3, "START_MINUTE": 24, "START_MERIDIEM": "AM", "FINISH_HOUR": 6, "FINISH_MINUTE": 34, "FINISH_MERIDIEM": "AM", "BREAK_HOUR": 0, "BREAK_MINUTE": 10, "DURATION_HOUR": 3, "DURATION_MINUTE": 0, "CHARGEABLE": 1, "DESCRIPTION": ""}, {"TSE_ID": 4442, "TIMESHEET_ID": 327, "TASK_ID": 2, "PERIOD_DATE": "05/01/2022", "START_HOUR": 1, "START_MINUTE": 12, "START_MERIDIEM": "AM", "FINISH_HOUR": 3, "FINISH_MINUTE": 23, "FINISH_MERIDIEM": "AM", "BREAK_HOUR": 0, "BREAK_MINUTE": 11, "DURATION_HOUR": 2, "DURATION_MINUTE": 0, "CHARGEABLE": 1, "DESCRIPTION": ""}, {"TSE_ID": 4451, "TIMESHEET_ID": 327, "TASK_ID": 2, "PERIOD_DATE": "06/01/2022", "START_HOUR": 2, "START_MINUTE": 11, "START_MERIDIEM": "AM", "FINISH_HOUR": 6, "FINISH_MINUTE": 23, "FINISH_MERIDIEM": "AM", "BREAK_HOUR": 0, "BREAK_MINUTE": 12, "DURATION_HOUR": 4, "DURATION_MINUTE": 0, "CHARGEABLE": 1, "DESCRIPTION": ""}], "timesheet_totals": [{"TOTAL_HOURS": 12, "TOTAL_MINUTES": 0, "ROUNDED_TOTAL_HOURS": 12.0}]}}
    return render_template( 'json/json_dumps.html', json_obj=timesheet )