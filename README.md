# If want to run the object-detection on duckiebot(yolo11)

First run `dts devel build -f -H ROBOT_NAME` , This command is use to build the container base on duckiebot environment.

Next Step run `dts devel run -H ROBOT_NAME -L objection_detection` must be -H can not use -R, and the -L means use which launcher file, here we use objection_detection.sh.

# One suggested way to see the result is into rqt_image_view.

First run `dts start_gui_tools ![DUCKIEBOT_NAME]`, this will help us enter ros environment.

And then run `rqt_image_view`, after this command a windown will appear, choose the topic we publish the result, In the code we publish the result to topic "object_detection/image/compressed".


# Template: template-ros

This template provides a boilerplate repository
for developing ROS-based software in Duckietown.

**NOTE:** If you want to develop software that does not use
ROS, check out [this template](https://github.com/duckietown/template-basic).


## How to use it

### 1. Fork this repository

Use the fork button in the top-right corner of the github page to fork this template repository.


### 2. Create a new repository

Create a new repository on github.com while
specifying the newly forked template repository as
a template for your new repository.


### 3. Define dependencies

List the dependencies in the files `dependencies-apt.txt` and
`dependencies-py3.txt` (apt packages and pip packages respectively).


### 4. Place your code

Place your code in the directory `/packages/` of
your new repository.


### 5. Setup launchers

The directory `/launchers` can contain as many launchers (launching scripts)
as you want. A default launcher called `default.sh` must always be present.

If you create an executable script (i.e., a file with a valid shebang statement)
a launcher will be created for it. For example, the script file 
`/launchers/my-launcher.sh` will be available inside the Docker image as the binary
`dt-launcher-my-launcher`.

When launching a new container, you can simply provide `dt-launcher-my-launcher` as
command.
