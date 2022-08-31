all: BuildThemes

BuildThemes:
	./Scripts/BuildThemes.py

clean: Clean
Clean:
	rm -rf ./Build
