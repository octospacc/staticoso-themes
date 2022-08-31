#!/bin/sh

for Theme in $(dir ./Themes)
do
	mkdir -p ./Build/Themes/$Theme
	cp ./Snippets/HTMLBase.html ./Build/Themes/$Theme/$Theme.html
	cp ./Themes/$Theme/Style.css ./Build/Themes/$Theme/Style.css
	sed -i "s/{{ThemeBody}}/$(sed 's:/:\\/:g' ./Themes/$Theme/Body.html)/" ./Build/Themes/$Theme/$Theme.html # Broken
done
