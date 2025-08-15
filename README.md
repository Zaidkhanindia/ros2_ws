In this Repositry, 

i created my first node, using python. it is simple just display "hello" on the command line, and runs after every 1 sec. - [File name: my_first_node.py]
Then created a Publisher node, which publishes the x and z values for linear and angular which makes turtle to run in circle. - [File name: Circle_Publisher_Node.py]
Then created a Subscirber node, which subscribe to the position node to get the x, y position of the turtlesim. - [File name: Position_Subscriber_Node.py]
Then created a Loop node, combination of above two nodes, the first node which takes position tells the turtle to turn after 9 on x or y and it turns whenever 
it goas to a corner of screen, Later, added a service/ client in it which changes the pen colour when it crosses the middle of screen which is 5.4. - [File name: Loop_Node.py]
