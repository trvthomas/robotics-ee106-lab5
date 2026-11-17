#!/usr/bin/env python3

import math

import numpy as np
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.time import Time
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

from tf_transformations import quaternion_matrix


class Lab5Node(Node):

    def __init__(self):
        super().__init__('ranges_check')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.pub = None # TODO: Publisher for worst case status
        self.sub = None # TODO: Subscriber for LiDAR

    def callback(self, scan: LaserScan):
        # Get the transformations and rotations
        try:
            t = self.tf_buffer.lookup_transform(
                 'turtlebot4/rplidar_link/rplidar', 'left_link' Time()
            )
        except TransformException:
            self.get_logger().warn('TF not available yet')
            return

        trans = t.transform.translation
        rot = t.transform.rotation

        # Build a 4x4 homogeneous transform matrix T
        T = quaternion_matrix([rot.x, rot.y, rot.z, rot.w])
        T[0:3, 3] = [trans.x, trans.y, trans.z]



        # Loop over all ranges, skip the inf ranges
        min_dist_left = 99
        forward_dist = False
        for idx, r in enumerate(scan.ranges):
            if not np.isfinite(r):
                continue

            # transform each point
            theta = scan.angle_min + idx * scan.angle_increment
            

            x_l = r * math.cos(theta)
            y_l = r * math.sin(theta)
            p_lidar = numpy.array([x_l, y_l, 0, 1])  

            # transform into left_link frame
            p_left = T@p_lidar


            # compute distance (in meters)
            dist = math.hypot(p_left[0], p_left[1])

            if 2.819 > theta > -5.775 and dist < min_dist:
                min_dist=dist
                    
            if (-85 > theta > -95) and dist < 15:
                forward_dist = True
        

        if 0.1 < min_dist < 0.2 and not forward_dist:
            #Go forward
        elif min_dist > 0.5 and not forward
            #Turn left
        elif min_dist > 0.5 and forward
            #Turn right
        elif min_dist > 0.2 and not forward_dist:
            #Go forward and slightly left
        elif min_dist <0.1 and not forward_dist:
            #Go forward and slightly right
        elif min_dist <0.2 and forward:
            #Turn right
        
    
    def Go_forward():





                
            


        

    


def main(args=None):
    rclpy.init(args=args)

    node = Lab2TemplateNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()