# Robotics EE106 Lab 5 :cowboy_hat_face:

## Commands

Launch the Turtlebot:

```
ros2 launch ee106f26 lab5_turtlebot_world.launch.py model:=lite world:=straight_line
```

Create 2 frames (right_limit and left_limit) with respect to rplidar_link:
```
ros2 run tf2_ros static_transform_publisher --x -0.17 --y -0.0 --z 0.0 --qx 0 --qy 0 --qz 0 --qw 1 --frame-id rplidar_link --child-frame-id right_limit

ros2 run tf2_ros static_transform_publisher --x 0.17 --y 0.0 --z 0.0 --qx 0 --qy 0 --qz 0 --qw 1 --frame-id rplidar_link --child-frame-id left_limit
```