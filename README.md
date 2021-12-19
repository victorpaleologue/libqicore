# naoqi_libqicore [![build](https://github.com/ros-naoqi/libqicore/actions/workflows/build.yml/badge.svg?branch=ros2)](https://github.com/ros-naoqi/libqicore/actions/workflows/build.yml)

This fork is used to define the __naoqi_libqicore__ ROS2 package, based on [__libqicore__](https://github.com/aldebaran/libqicore).

## Compilation
To compile __naoqi_libqicore__, clone this repository in a ROS workspace and use the `colcon build` command. Please note that [__naoqi_libqi__](https://github.com/ros-naoqi/libqi) is a dependency of that project, you should have the package `ros-distro-naoqi-libqi` installed, or build the naoqi_libqi project from source in the same workspace.

Please note that you should checkout the branch corresponding to your ROS distro (eg. `galactic-devel` for Galactic, `foxy-devel` for Foxy, etc...)

## Status 

The project can currently be successfully built for `Galactic (focal)` and `Foxy (focal)`. Please refer to the [build workflow](https://github.com/ros-naoqi/libqicore/actions/workflows/build.yml) for more information