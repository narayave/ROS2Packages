# ROS2Packages

ament build src/[directory name] - builds packages in that directory
ament test src/test1/testcpp_talker - Constructs tests
ament test src/test1/testcpp_listener - Constructs tests

ament package_version src/test1/testcpp_listener - package version

ros2 security create_key demo_keystore/ testcpp_talker

ros2 security create_key demo_keystore/ testcpp_listener


ament build --symlink-install = This properly installs the executables?

ros2 run testcpp_listener = Run test listener
ros2 run testcpp_talker = Run test talker over the "chat" topic
