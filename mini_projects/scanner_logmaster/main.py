import argparse
from datetime import datetime, time, timedelta
from collections import defaultdict
from persiantools.jdatetime import JalaliDate
import json

def load_employee_names(json_file="employees.json"):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def parse_logs(filepath, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    data = defaultdict(lambda: defaultdict(list))
    with open(filepath, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) < 3:
                continue
            emp_id = parts[0]
            ts_str = parts[1] + " " + parts[2]
            try:
                ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue
            if start <= ts.date() <= end:
                data[emp_id][ts.date()].append(ts)
    return data, start, end

def get_shifts_for_day(dt):
    weekday = dt.weekday()
    if weekday == 4:
        return [(time(9,30), time(16,0)), (time(16,0), time(22,30))]
    else:
        return [(time(7,30), time(15,0)), (time(15,0), time(22,30))]

def select_shift(in_time, shifts):
    if in_time.time() < shifts[0][0]:
        return shifts[0]
    elif shifts[0][0] <= in_time.time() <= shifts[0][1]:
        return shifts[0]
    elif len(shifts) > 1 and shifts[1][0] <= in_time.time() <= shifts[1][1]:
        return shifts[1]
    else:
        return shifts[1] if len(shifts) > 1 else shifts[0]

def format_missing_or_time(ts, missing=False):
    if missing or ts is None:
        return "\033[1m\033[31mMissing\033[0m"
    return ts.strftime("%H:%M:%S")

def format_delta(diff_hours):
    if diff_hours >= 0:
        return f"\033[1m\033[32m+{round(diff_hours,2)}\033[0m"
    else:
        return f"\033[1m\033[31m{round(diff_hours,2)}\033[0m"

def calculate_hours(data, start, end, detailed=False, employee_names={}, filter_ids=None):
    results = {}
    forgotten_scans_results = {}
    total_days = (end - start).days + 1
    for emp_id, days in data.items():
        if filter_ids and int(emp_id) not in filter_ids:
            continue
        name = employee_names.get(emp_id, emp_id)
        missing_days = []
        forgotten_scans = 0

        if detailed:
            results[name] = {}
            for day_num in range(total_days):
                day = start + timedelta(days=day_num)
                timestamps = sorted(days.get(day, []))
                in_time = timestamps[0] if timestamps else None
                out_time = timestamps[-1] if len(timestamps) >= 2 else None
                shifts = get_shifts_for_day(day)

                if in_time:
                    shift_start_time, shift_end_time = select_shift(in_time, shifts)
                else:
                    shift_start_time, shift_end_time = shifts[0]

                shift_start = datetime.combine(day, shift_start_time)
                shift_end = datetime.combine(day, shift_end_time)

                if (in_time and not out_time) or (out_time and not in_time):
                    forgotten_scans += 1

                if not in_time or not out_time:
                    missing_days.append(day)

                worked_hours = 0.0
                if in_time and out_time:
                    worked_seconds = (out_time - in_time).total_seconds()
                    worked_hours = worked_seconds / 3600

                expected_hours = (shift_end - shift_start).total_seconds() / 3600
                diff_hours = worked_hours - expected_hours

                in_time_str = format_missing_or_time(in_time, missing=(in_time is None))
                out_time_str = format_missing_or_time(out_time, missing=(out_time is None or in_time is None))
                diff_str = format_delta(diff_hours)

                weekday = in_time.strftime("%A") if in_time else "Unknown"
                shamsi = JalaliDate(day)
                shamsi_str = f"{shamsi.year:04d}-{shamsi.month:02d}-{shamsi.day:02d}"

                results[name][day] = (
                    worked_hours,
                    weekday,
                    shamsi_str,
                    in_time_str,
                    out_time_str,
                    diff_str,
                    in_time is None or out_time is None
                )

            forgotten_scans_results[name] = forgotten_scans

        else:
            total_worked = 0.0
            total_expected = 0.0

            for day_num in range(total_days):
                day = start + timedelta(days=day_num)
                timestamps = sorted(days.get(day, []))

                if not timestamps or len(timestamps) < 2:
                    missing_days.append(day)
                    if timestamps:
                        forgotten_scans += 1
                    continue

                in_time = timestamps[0]
                out_time = timestamps[-1]

                shifts = get_shifts_for_day(day)
                shift_start_time, shift_end_time = select_shift(in_time, shifts)
                shift_start = datetime.combine(day, shift_start_time)
                shift_end = datetime.combine(day, shift_end_time)

                worked_seconds = (out_time - in_time).total_seconds()
                worked_hours = worked_seconds / 3600

                expected_hours = (shift_end - shift_start).total_seconds() / 3600

                total_worked += worked_hours
                total_expected += expected_hours

            diff_hours = total_worked - total_expected

            results[name] = (
                round(total_worked, 2),
                format_delta(diff_hours),
                len(missing_days),
                total_days,
                forgotten_scans
            )

    return results, forgotten_scans_results


parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command", required=True)
ch = subparser.add_parser("ch")
ch.add_argument("file")
ch.add_argument("-s", required=True)
ch.add_argument("-e", required=True)
ch.add_argument("-d","--details", action="store_true")
ch.add_argument("-fs","--forgotten-scans", action="store_true",
                help="Show only days with forgotten scans (only works with -d)")
ch.add_argument("-id", "--employee_id", type=int, nargs="+")
args = parser.parse_args()

employee_names = load_employee_names()
data, start, end = parse_logs(args.file, args.s, args.e)
filter_ids = args.employee_id if args.employee_id else None

results, forgotten_scans_results = calculate_hours(
    data, start, end,
    detailed=args.details,
    employee_names=employee_names,
    filter_ids=filter_ids
)

if args.details:
    for name, days in results.items():
        forgotten = forgotten_scans_results.get(name, 0)
        print(f"{name} (Forgotten scans: {forgotten}):")
        for day, (worked_hours, weekday, shamsi, in_time, out_time, diff_str, missing) in sorted(days.items()):

            if args.forgotten_scans:
                has_forgotten = (("Missing" not in in_time) and ("Missing" in out_time)) or \
                                (("Missing" in in_time) and ("Missing" not in out_time))
                if not has_forgotten:
                    continue

            missing_note = " (Missing)" if missing else ""
            print(f"  {day} ({weekday}) {shamsi}: Worked {round(worked_hours,2)}h, In: {in_time}, Out: {out_time}, Δ: {diff_str}{missing_note}")

else:
    for name, (hours, diff_str, missing_count, total_days, forgotten) in sorted(results.items()):
        print(f"{name}: Worked {hours}h, Δ: {diff_str}, Missing: {missing_count}/{total_days} days, Forgotten scans: {forgotten}")