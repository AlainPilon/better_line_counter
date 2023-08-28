# better_line_counter
Improved version of Roboflow [LineCounter](https://github.com/roboflow/supervision/blob/develop/supervision/detection/line_counter.py) class.

# Features

## Trigger conditions
Default version of LineCounter is only triggered when the detection box has completely passed over the line. This version allows a configuration to support partially detection to be counted.

## Trafic manager
Add an optional TraficManager class to be injected in LineCounter. This TraficManager supports two callback `incoming` and `outgoing` which are triggered on the corresponding count updates.

