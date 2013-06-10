## What?
Intersect It is a QGIS plugin to place observations (distance or orientation) with their corresponding precision, intersect them using a least-squares solution and save dimensions in a dedicated layer to produce maps.

A demo is available on [youtube](http://www.youtube.com/watch?v=IJQvIe1CLD0&hd=1).

The plugin requires numpy.

## How ?

### Observations
First, you have to place observations which can be distances or orientations (**orientations are not available yet**). 
Click on the corresponding icon to place an observation.

In the dedicated tab in settings, you can define:
* if the snap is used to place observations (using the layers properties).
* the default precision for both types of observations.

The observations are put in two memory layers which are automatically created by the plugin (_IntersectIt Points_ and _IntersectIt Lines_).

The observations can deleted using the usual tools from QGIS or all at once using the broom icon.


### Intersection

Once you have place the needed observations, you can start the intersection process by clicking on the icon. you have to click on the map to define the approximate location of the intersection. All the observations which will be used in intersection process will be highlighted. Distance tolerance and highlighting of selection can be defined in the settings.

Then, if only two observations are selected a simple intersection is calculated. If more than 2, a least-squares adjustment is performed. Convergence threshold and maximum iterations can be defined in settings.

If defined in settings, the least-squares report is displayed for confirmation. It can also be saved in a field of the layer used to save intersection point.

### Dimensions

Once the intersection is found, if defined in settings, the dimensions can be place in layers. These are stored in a multipoint layer: three points are saved. From this, you can use a view in postgis to draw dimension arcs.
The SQL creation code of these two layers can be found [here](https://github.com/3nids/intersectit/wiki/Dimension-layers).


## Changelog
### 1.0.3 26.03.2012
* Increased max length for distances to 999km

### 1.0.2 23.03.2012
* Added one digit in place distance UI

###1.0.1 21.03.2012
* Added help in menu