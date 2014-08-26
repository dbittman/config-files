Intro
==========
Here's remake of the KDE 4.0 Oxygen theme. It's contains elemnts of
KDE 4.0 Oxygen theme and current (KDE 4.7) Oxygen theme for elements
not present in original theme.
Several elements have been redone from scratch to use abilities
provided by current plasma desktop. I've replaced most of the bitmap
components with pure vector/SVG, This change resulted in better shapes
and smoother transitions. Also all the scalable items like progress
bar look much better now without visible stretches and misproportions.

While I've tried to make it as close to the original as it's possible,
the theme  it's not identical to old one. Due to changes in
plasma-desktop and how the things are handled it's not possible to make
plasmoid configuration handle as it was in KDE 4.0.
Few items like analog clock and analog meter were replaced with current
ones, as they fit the theme much better then original ones.
My theme also has thinner widget borders to not waste screen estate.
Shadows got thinner too. Old ones looked weird with blur effect enabled,
adding extra border around widgets with sharp edge instead of gentle fade
they had to be. Now the shadows are still visible, but shouldn't be so
annoying. Another change is translucent background used in "Folder View"
plasmoid. Original theme used regular background, which looked way too
heavy.
Pager is the blue-tinted one from current Oxygen theme, just because 
I like it more than the flat-white one.

I've decided to include colorful systray icons pack made by Kevin Kofler
by default. Many thanks to him for this set :)
If you want monochrome icons back, just rename or remove icons subddir
located in this theme dicrectory.

Installation:
==============
Copy the content of the zip file into ~/.kde/share/apps/desktoptheme/ for
your user only or to the /usr/share/kde4/apps/desktoptheme/ dir for
system-wide installation (root priviledges required).

Bugs and possible TODOs:
===========================
- Worse buttons readability - unfortunately I had to make compromise I don't
  really like. There's no seprate setings for text color on buttons, entry 
  fields (date in calendar, and some plasmoids (AkoNotes). I tried to make 'em
  all looking reasonably well, while keep text readable. There'll be a fix when
  plasma devs decouple those entries.

I hope you'll like it ;)
/Stan aka 'Xeno'


Changelog:
=====================
20.12.2011 - 0.1 Initial version
30.12.2011 - 0.2 Dialogs shadows trimmed some more, less blur outside dialog boxes
		 Shadow bitmap sources included
18.11.2012 - 0.3 Fixed notification progress-bar, redone buttons, now they match
                 panels. Changed some colors (now AkoNotes plasmoid is kinda usable)
                 Updated icons, again thanks to K.Kofler.
02.12.2012 - 0.4 fixed buttons height, now it's fe px larger than text improving readability.
		 "fixed" Lancelot top buttons - it's still ugly, but it's lacelot fault,
		 other therem hide ugilnes not showing background for normal buttons.
		 Improved transluent background, now it's all smooth with no dark edges.
27.01.2013 - 0.5 Verified KDE 4.10 compatibility, fixed groove in battery plasmoid/screen
                 brightness slider, improved buttons in notifications/activites panel. 
                 Made colorfull plasmoid action/config icons (yay). Minor cleanup in svgs
                 definitions.
05.04.2013 - 0.6 fixed notifications background (it's black again :D ), made notifications expand
		 arrow bright, even more colorfull actions icons.
                 