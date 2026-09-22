import json
import subprocess
import sys


command = [
    sys.executable,
    "manage.py",
    "dumpdata",
    "--settings=config.sqlite_settings",
    "--natural-foreign",
    "--natural-primary",
    "--exclude",
    "contenttypes",
    "--exclude",
    "auth.permission",
    "--exclude",
    "admin.logentry",
    "--exclude",
    "sessions",
    "--indent",
    "2",
]

result = subprocess.run(
    command,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if result.returncode != 0:
    print("DUMP FAILED:")
    print(result.stderr.decode("utf-8", errors="replace"))
    sys.exit(1)

# Django output can contain Unicode characters.
# Decode using UTF-8 first, then fallback safely if needed.
try:
    output = result.stdout.decode("utf-8")
except UnicodeDecodeError:
    output = result.stdout.decode("utf-8", errors="replace")

try:
    data = json.loads(output)
except json.JSONDecodeError as error:
    print("INVALID JSON:")
    print(error)
    print(output[:2000])
    sys.exit(1)

with open(
    "sqlite_data.json",
    "w",
    encoding="utf-8",
    newline="\n",
) as file:
    json.dump(
        data,
        file,
        ensure_ascii=False,
        indent=2,
    )

print(f"Export successful: {len(data)} objects exported.")