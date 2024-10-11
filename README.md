# DDoS Tool in Python

## Objective

The objective of this script is to create a DDoS attack tool that can be used for educational purposes or to demonstrate the power of distributed denial of service attacks. The tool is designed to simulate multiple attackers simultaneously sending HTTP GET requests to a specified target.

### Explanation

- The script starts by importing the necessary modules: `threading`, `socket`, `random`, and `time`.
- The `target` variable is set to the target IP address or domain name that you wish to attack. The `port` variable is set to the target port (in this case, port 80 for HTTP).
- The `ddos_attack()` function is defined, which contains the main logic of the attack. It creates a socket connection to the target, sends an HTTP GET request, and then closes the connection. If an error occurs during the connection or sending the request, it is caught and ignored.
- The `main()` function creates multiple threads using the `threading.Thread()` class. Each thread runs the `ddos_attack()` function. The number of threads is determined by the range function, which is set to 100 in this example.
- The script then enters the `main()` function, where it starts all the created threads and waits for them to finish using the `join()` method.
- Finally, the script checks if the script is being run as the main program (`__name__ == '__main__'`), and if so, it calls the `main()` function to start the attack.

### Notes

Please note that this script is for educational purposes only. It should not be used against any target without explicit permission and in compliance with applicable laws and regulations.

Remember to replace 'example.com' with the actual target IP address or domain name you wish to attack.
