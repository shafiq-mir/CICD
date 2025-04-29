# -*- coding: utf-8 -*-

from netmiko import ConnectHandler



connection_to_router = ConnectHandler(
                      device_type="cisco_ios",
                      host="10.0.0.85",
                      username="shafiq",
                      password="cisco",
)

# output = connection_to_router.send_command(
#   "show ip int brief"
#   )
# print(output)



#--------------------------Create ACCESS-list CONFIGURATION--------------------

# cfg_list = [
#     "ip access-list extended TEST1",
#     "permit ip any host 1.1.1.1",
#     "permit ip any host 1.1.1.2",
#     "permit ip any host 1.1.1.3",
#     "permit ip any host 1.1.1.4",
#     "permit ip any host 1.1.1.5",
# ]
# cfg_output = connection_to_router.send_config_set(cfg_list)

# #print(cfg_output)

#--------------------------OSPF CONFIGURATION--------------------------
# ospf_cfg = [
#     "router ospf 1",
#     "network 10.10.10.10 0.0.0.0 area 0",
#     "router-id 10.10.10.10",
# ]

# ospf_cfg_output = connection_to_router.send_config_set(ospf_cfg)
# print(ospf_cfg_output)

# --------------------------------Enable EIGRP---


# eigrp_cfg = [
#     "router eigrp 1",
#     "network 11.11.11.11 0.0.0.255"
# ]

# output = connection_to_router.send_config_set(eigrp_cfg)
# print(output)



# output = connection_to_router.send_command(
# "show ip protocols "
# )

# ----------------------------------------Correct Ways to Send Multiple show Commands:

# 1 way

# output1 = connection_to_router.send_command("show ip protocols")
# output2 = connection_to_router.send_command("show ip route eigrp")
# output3 = connection_to_router.send_command("show ip interface brief")

# print(output1)
# print(output2)
# print(output3)
# ------Using a Loop for Multiple Commands




# 2nd way

# commands = ["show ip protocols", "show ip route eigrp", "show ip interface brief"]
# for command in commands:
# output = connection_to_router.send_command(command)
# print(f"Output of '{command}':\n{output}\n")


# --------------------Using a List of Commands with send_config_set -

# Using send_multiline-If available in your Netmiko version, this allows batch execution:


# 3rd way


# output1 = connection_to_router.send_command_timing("show ip protocols")
# output2 = connection_to_router.send_command_timing("show ip route eigrp")
output3 = connection_to_router.send_command_timing("show ip interface brief")

print(output3)








# print(output)
# connection_to_router.disconnect()
# connection_to_router.save_config()
# connection_to_router.disconnect()
# print("Configuration saved and connection closed.")
