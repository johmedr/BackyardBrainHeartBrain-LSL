# Driver to stream data from BackyardBrain's Heart & Brain kit to the Lab Streaming Layer
Example below shows how to use the driver with [OpenVibe](http://openvibe.inria.fr/) 
## 1- Installing the package
Using [Pip](https://pypi.org/project/pip/) 
```Bash
> pip install byb2lsl
```

## 2- Launch the driver
``` 
> python -m byb2lsl.driver
```

## 3- Connect to OpenVibe
Launch the program OpenVibe Acquisition Server. 
In Driver, select "LabStreamingLayer". 
In Driver Properties > Signal Stream, select "ByB Heart&Brain".
In Preferences > Drift Correction, select "Let the driver decide". 

## 4- Use in OpenVibe Designer
Start OpenVibe Designer. 
Add a new "Acquisition Server" node, which will stream the data from the Backyard Brain. 
Connect to your pipeline... 
