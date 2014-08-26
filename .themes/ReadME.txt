--------
CONTENT:
--------
1. Description of changes
2. Installing the theme

------------
Description:
------------
I didn't create this theme. Actually this is the Ubuntu 11.10 Ambiance theme, but tweaked. 

Changes to the original theme:
1. Added dark panel in Nautilus 
-I never liked the default one. I've always feel it like it was something patched there in a hurry
To do that you have to change the end of the gtk-3.0/apps/nautilus.css to look like this:

/* sidebar */
NautilusWindow .sidebar,
NautilusWindow .sidebar .view {
    background-color: @dark_bg_color;
    color: @dark_fg_color;
}

NautilusWindow .sidebar .frame {
    border-radius: 0;
    border-width: 0;
}

NautilusWindow > GtkTable > .pane-separator {
	background-color: @dark_bg_color;
    border-color: @dark_bg_color;
    border-width: 0 0 0 0;
    border-style: solid;
}

2. Changed the selection color in the OS to be blue. 
- the original orange color was always a bit too odd to me
To do that I've had to change the color values (in hex format) in 
gtk-3.0/gtk.css; gtk-3.0/settings.ini and gtk-2.0/gtkrc

3. Changed the main theme colors to steel blue

4. Added transparency by default to unity panel
 - If you don't want the transparency edit the unity.css (AmbSTEELblue/gtk-3.0/apps) 
from:
.unity-panel {

    background-image: -gtk-gradient (linear, left top, left bottom,
                                     from (alpha(@dark_bg_color,0.75)),
                                     to (alpha(@dark_bg_color,0.99)));
    border-top-color: shade (@dark_bg_color, 1.6);
    border-style: solid;
    border-width: 1 0 0 0;

    -unico-border-gradient: none;
}

to:
.unity-panel {
    background-image: -gtk-gradient (linear, left top, left bottom,
                                     from (shade (@dark_bg_color, 1.5)),
                                     to (shade (@dark_bg_color, 1.04)));
    border-top-color: shade (@dark_bg_color, 1.6);
    border-style: solid;
    border-width: 1 0 0 0;

    -unico-border-gradient: none;
}

5. Window titles were moved to the right of the window. 
- With the Canonical's decision to move the controls (close, minimize, maximize) to the left that area of the window title became a little cluttered for my taste. I've noticed, that the right part of the title window is empty, so I've moved the titles there. I like the result It feels more balanced that way and hope you'll like it too.
To do that you have to change the metacity-1/metacity-theme-1.xml to look like this:

<!-- window titles -->

<draw_ops name="draw_title_text_normal">
  <title color="#333" x="(((width-title_width) / 1) `max` 0)" y="(((height - title_height) / 2) `max` 0)+1"/>
  <title color="#333" x="(((width-title_width) / 1) `max` 0)" y="(((height - title_height) / 2) `max` 0)-1"/>
  <title color="#333" x="(((width-title_width) / 1) `max` 0)" y="(((height - title_height) / 2) `max` 0)"/>
  <title color="#333" x="(((width-title_width) / 1) `max` 0)" y="(((height - title_height) / 2) `max` 0)"/>
  <title color="#dfdbd2" x="(((width-title_width) / 1) `max` 0)-1" y="(((height - title_height) / 2) `max` 0)-1"/>
</draw_ops>

<draw_ops name="draw_title_text_unfocused">
  <title color="#333" x="(((width-title_width) / 1) `max` 0)" y="(((height - title_height) / 2) `max` 0)+1"/>
  <title color="#333" x="(((width-title_width) / 1) `max` 0)" y="(((height - title_height) / 2) `max` 0)-1"/>
  <title color="#333" x="(((width-title_width) / 1) `max` 0)" y="(((height - title_height) / 2) `max` 0)"/>
  <title color="#333" x="(((width-title_width) / 1) `max` 0)" y="(((height - title_height) / 2) `max` 0)"/>
  <title color="#807d78" x="(((width-title_width) / 1) `max` 0)-1" y="(((height - title_height) / 2) `max` 0)-1"/>
</draw_ops>

<draw_ops name="draw_title">

6. Changed window borders to 4 px and added rounded corners 
To do that change the metacity-1/metacity-theme-1.xml to this:

<!-- general window layout -->
<frame_geometry name="frame_geometry_normal" title_scale="medium" rounded_top_left="true" rounded_top_right="true" rounded_bottom_left="true" rounded_bottom_right="true">
  <distance name="left_width" value="4"/>
  <distance name="right_width" value="4"/>
  <distance name="bottom_height" value="4"/>
  <distance name="left_titlebar_edge" value="10"/>
  <distance name="right_titlebar_edge" value="10"/>
  <distance name="button_width" value="18"/>
  <distance name="button_height" value="20"/>
  <distance name="title_vertical_pad" value="12"/>
  <border name="title_border" left="2" right="2" top="0" bottom="0"/>
  <border name="button_border" left="0" right="0" top="1" bottom="1"/>
</frame_geometry>

---------------------
Installing the theme:
---------------------

1. Unpack the downloaded 'tar.gz' archive to your home .themes folder
-if there aint any just create it
2. Use Myunity, gnome tweak tool, ubuntutweak or whatever suits you tool to load the theme
3. Enjoy ;)







