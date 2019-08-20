Color-based risk elicitation
=============================

The game consists of two stages.

*Stage 1*: a player has to choose the difficulty level. Based on this difficulty the range between which
the set of colors are generated will be wider (for easier tasks) or narrower (for more difficult tasks).

The degree of difficulty results in different renumeration per each successful trial

*Stage 2*: A player has to guess which color is shown.

Parameters
----------

For now most of the parameters are set in ``Constants``. It includes:

- ``hue``, ``saturation`` and ``lightness`` for the initial (starting) color.
- number of colors to guess from
- some other parameters such as step

The colors are generated via HSL model. Saturation and lightness are hold constant, while hue is varied
based on a participant choice.


