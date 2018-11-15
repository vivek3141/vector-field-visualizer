# Vector Field Visualizer
A python program to visualize a two dimensional 
vector field, and to calculate divergence and curl 
at any point.

## Requirements
Install the requirements by
```bash
pip install -r requirements.txt
```
OR
* matplotlib - `pip install matplotlib`
## Usage
```bash
python3 main.py [fx] [fy] --mode [mode] --skip [skip] \
--boundx [boundx] --boundy [boundy] --prop [prop] --head_size [head_size]
```
#### --mode
Set mode to COLOR to use color to portray length instead of actual length.
#####--prop
Use prop to adjust the length for which the color should change.
<br><br>
Set mode to BLACK to use actual length.
#### Examples
<img src="https://raw.githubusercontent.com/vivek3141/vector-field-visualizer/master/img/color.jpg" height=240><br>
<img src="https://raw.githubusercontent.com/vivek3141/vector-field-visualizer/master/img/blackwhite.jpg" height=240>

