#include <iostream>
#include <memory>

#include "rclcpp/rclcpp.hpp"

#include "std_msgs/msg/float32.hpp"

void chatterCallback(const std_msgs::msg::Float32::SharedPtr msg)
{
  std::cout << "I heard: [" << msg->data << "]" << std::endl;
}
//create a subscriber
int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  // create a node
  auto node = rclcpp::Node::make_shared("test1_testcpp_listener");

  auto sub = node->create_subscription<std_msgs::msg::Float32>(
    "chatter", chatterCallback, rmw_qos_profile_default);

  // spin: Blocking call, do work indefinitely as it comes in.
 //  spin_once: Do one "cycle" of work, with optional timeout.
 //  spin_some: Do all the work that is immediately available to the executor.
  rclcpp::spin(node);

  return 0;
}