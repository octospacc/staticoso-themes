#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def Main():
	for Theme in os.listdir("Themes"):
		Path(f"./Build/Themes/{Theme}").mkdir(parents=True, exist_ok=True)
		try:
			shutil.copyfile(f"./Themes/{Theme}/Style.css", f"./Build/Themes/{Theme}/Style.css")
		except FileExistsError:
			pass
		with open(f"./Snippets/Base.html", "r") as f:
			Base = f.read()
		with open(f"./Themes/{Theme}/Body.html", "r") as f:
			Body = f.read()
		with open(f"./Build/Themes/{Theme}/{Theme}.html", "w+") as f:
			f.write(Base.replace("{{Body}}", Body))

if __name__ == "__main__":
	Main()
