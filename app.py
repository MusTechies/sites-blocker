import time

import webbrowser

# A list of sites that should be blocked
blockedSites = input("Enter the sites to be blocked separated by commas: ").split(",")

# The amount of time (in seconds) that the sites should be blocked for
blockDuration = int(input("Enter the duration of time (in minutes) the sites should be blocked for: ")) * 60

# Get the current time
startTime = time.time()

while True:
    # Check the current time
    currentTime = time.time()

    # Calculate the elapsed time
    elapsedTime = currentTime - startTime

    # If the elapsed time is greater than the block duration, exit the loop
    if elapsedTime > blockDuration:
        break

    # Otherwise, check if the current URL is blocked
    currentURL = webbrowser.get().open_new_tab("about:blank").location

    for site in blockedSites:
        if site in currentURL:
            webbrowser.get().open_new_tab("about:blank")
            print(f"Access to {site} is blocked for {blockDuration / 60} minutes.")
            time.sleep(5)

print("You can now access your blocked sites")
