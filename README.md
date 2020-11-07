# osscar-docs
[![Documentation Status](https://readthedocs.org/projects/osscar-docs/badge/?version=latest)](https://osscar-docs.readthedocs.io/en/latest/?badge=latest)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/osscar-docs/master?urlpath=%2Fvoila%2Frender%2Fnotebooks%2Findex.ipynb)

Documentation on how to create new educational apps and to deploy them with the OSSCAR technology

## List of Jupyter notebook tutorial

* [Jupyter introduction](./notebooks/Jupyter_introdcution.ipynb)

Binder is cloud computing platform to deploy Jupyter notebooks. It is easy to use and share the notebooks. Here, we are using the Binder platform to delivery our tools and notebooks for courses. The configurations for Jupyter Notebook and JupyterLab are slightly different. Please check the link below:  

* [Use Binder for Jupyter notebook and lab](./notebooks/Binder_tutorial.ipynb)

Widgets are largely used for this projects. The ipywidgets package well supports to implement widgets in the Jupyter.

* [Use widget for the Jupyter](./notebooks/Use_widgets.ipynb)

Besides all the default widgets in the package, one can also create custom widgets.

* [A custom widget example](./notebooks/Custom_widget_example.ipynb)

By using the widgets, we can demonstrate scientific problems and knowledge. Here is a demo to show the sine function with widgets in Jupyter notebook.

* [Sine function with widget interact](./notebooks/Sine_function_a.ipynb)
* [Sine function with more advanced widgets](./notebooks/Sine_function_b.ipynb)

Voila package can render Jupyter notebooks in live with interactive widgets. Through using Voila with Binder, one can create web applications. The web apps can be deployed on
Binder and Dokku platforms.

* [Voila for web applications](./notebooks/Binder_voila.ipynb)

You can view the sine function with Binder and Voila by click the Binder badge.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/osscar-docs/master?urlpath=%2Fvoila%2Frender%2Fnotebooks%2FSine_function_b.ipynb)

## Visualizer

We are using the Nglview as the visualizer for molecular and solid structures.

[GitHub link for Nglview](https://github.com/arose/nglview)

Here are two tutorials for basic and advanced usage of Nglview in the Jupyter
notebooks. Besides, we also need to use the three.js library to create 3D object
widgets. The **pythreejs** package can be used to implement related widgets.

| Topics | Notebooks | Binder |
| ------ | --------- | ------ |
| Nglview basic usage | [Nglview basic usage](./notebooks/nglview_basic.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/osscar-docs/master?urlpath=%2Ftree%2Fnotebooks%2Fnglview_basic.ipynb) |
| Nglview advanced usage | [Nglview advanced usage](./notebooks/nglview_advanced.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/osscar-docs/master?urlpath=%2Ftree%2Fnotebooks%2Fnglview_advanced.ipynb) |
| Pythreejs tutorial |  [Pytrheejs tutorial](./notebooks/pythreejs_example.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/osscar-docs/master?urlpath=%2Ftree%2Fnotebooks%2Fpythreejs_example.ipynb) |

# Acknowledgements

We acknowledge support from the EPFL Open Science Fund via the [OSSCAR](http://www.osscar.org) project.

<img src='http://www.osscar.org/wp-content/uploads/2019/03/OSSCAR-logo.png' width='230'>
