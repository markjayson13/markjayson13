"""Rebuild the pixel contribution card from the public GitHub calendar.

The workflow runs this on a schedule. Counts are whatever the API returns.
Nothing in the card is typed in by hand.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from playbill import DARK, LIGHT, build_quest, save_svg  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
LOGIN = os.environ.get("QUEST_LOGIN", "markjayson13")
MONTHS = "JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split()


def _query(login: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9-]+", login):
        raise SystemExit(f"unexpected login {login!r}")
    return f"""
    query {{
      user(login: "{login}") {{
        contributionsCollection {{
          contributionCalendar {{
            totalContributions
            weeks {{
              contributionDays {{
                contributionCount
                date
              }}
            }}
          }}
        }}
      }}
    }}
    """


def fetch_calendar(login: str) -> tuple[list[list[tuple[str, int]]], int]:
    payload = json.dumps({"query": _query(login)}).encode()
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GH_TOKEN or GITHUB_TOKEN is required to read the contribution calendar.")
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "farol-playbill",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        body = json.load(response)
    if body.get("errors"):
        raise SystemExit(json.dumps(body["errors"], indent=2))
    calendar = body["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks: list[list[tuple[str, int]]] = []
    for week in calendar["weeks"]:
        days = [(day["date"], int(day["contributionCount"])) for day in week["contributionDays"]]
        if days:
            weeks.append(days)
    return weeks, int(calendar["totalContributions"])


def month_label(iso: str) -> str:
    parsed = dt.date.fromisoformat(iso)
    return f"{MONTHS[parsed.month - 1]} {parsed.year}"


def main() -> None:
    weeks, total = fetch_calendar(LOGIN)
    if not weeks:
        raise SystemExit("contribution calendar was empty")
    first = weeks[0][0][0]
    last = weeks[-1][-1][0]
    start, end = month_label(first), month_label(last)
    title = f"Public GitHub contributions, {start} to {end}. {total} contributions."
    desc = "Pixel grid of the public contribution calendar. Counts come from GitHub."
    save_svg(ROOT / "assets" / "quest-log-light.svg", build_quest(LIGHT, weeks, total, start, end), title, desc)
    save_svg(ROOT / "assets" / "quest-log-dark.svg", build_quest(DARK, weeks, total, start, end), title, desc)


if __name__ == "__main__":
    main()
