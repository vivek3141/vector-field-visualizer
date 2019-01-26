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
--bound [bound] --prop [prop]
```
#### --mode
Set mode to COLOR to use color to portray length instead of actual length.
##### --prop
Use prop to adjust the length for which the color should change.
<br><br>
Set mode to BLACK to use actual length.
#### Examples
`python3 main.py x y --mode "COLOR"`<br><br>
<img src="https://raw.githubusercontent.com/vivek3141/vector-field-visualizer/master/img/color.jpg"><br>
<br>
`python3 main.py x y --mode "BLACK"`<br><br>
<img src="https://raw.githubusercontent.com/vivek3141/vector-field-visualizer/master/img/blackwhite.jpg">
#### --skip
Skip is the space between each vector for X and Y. Eg. `--skip 2`
#### --bound
Set for bounds of X and Y. Eg. `--boundx "-10,10"`

