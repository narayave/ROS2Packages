# ROS2Packages

ament build src/[directory name] - builds packages in that directory
ament test src/test1/testcpp_talker - Constructs tests
ament test src/test1/testcpp_listener - Constructs tests

ament package_version src/test1/testcpp_listener - package version

ros2 security create_key demo_keystore/ testcpp_talker

ros2 security create_key demo_keystore/ testcpp_listener
