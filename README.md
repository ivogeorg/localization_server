### `localization_server`

#### Notes

1. The node which publishes the `map`->`odom` tranform this time is `amcl`, but _only after_ the **2D Pose Estimate** is selected. Note that this can be very inaccurate at first, but after the robot moves around, it will become increasingly accurate.
   | Gazebo (actual) | Rviz2 (probabilistic) |
   | --- | --- |
   | ![Actual](assets/location_in_gazebo.png) | ![AMCL](assets/localization_in_rviz2.png) | 
2. AMCL stands for [**A**daptive **M**onte **C**arlo **L**ocalization](https://roboticsknowledgebase.com/wiki/state-estimation/adaptive-monte-carlo-localization/). Essentially, adaptive _particle filters_. 

