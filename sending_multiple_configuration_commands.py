from netmiko import ConnectHandler

# Define connection details
connection_to_router = ConnectHandler(
    device_type="cisco_ios",
    host="10.0.0.85",
    username="shafiq",
    password="cisco"
    )

# Define the configuration commands
config_commands = [
    "line con 0 ",
    "logging synchronous",
    "exec-timeout 0 0",
    "exit",
    "hostname R9",
    "interface GigabitEthernet 2",
    "ip address 10.10.0.1 255.255.255.0",
    "no shutdown",
    "exit",
    "router ospf 10",
    "router-id 10.10.10.10",
    "network 10.10.10.0 0.0.0.255 area 0",
    "exit",
    "router eigrp 1",
    "network 11.11.11.0 0.0.0.255",
    "exit",
    "no ip domain lookup"


]

# Send configuration commands
# output = connection_to_router.send_config_set(config_commands)

# print(output)

output = connection_to_router.send_command("show ip int brief")
print(output)
output = connection_to_router.send_command("show ip route")
print(output)
output = connection_to_router.send_command("show ip protocols")
print(output)
output = connection_to_router.send_command("show ip eigrp neighbors")
print(output)

connection_to_router.save_config()
#Close the connection
connection_to_router.disconnect()
print("Configuration saved and connection closed.")
