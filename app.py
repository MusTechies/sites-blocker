import time
import webbrowser

# A list of sites that should be blocked
blocked_sites = ["https://www.facebook.com", "https://twitter.com", "https://instagram.com"]

# The amount of time (in seconds) that the sites should be blocked for
block_duration = 1800  # 30 minutes

# Get the current time
start_time = time.time()

while True:
    # Check the current time
    current_time = time.time()

    # Calculate the elapsed time
    elapsed_time = current_time - start_time

    # If the elapsed time is greater than the block duration, exit the loop
    if elapsed_time > block_duration:
        break

    # Otherwise, check if the current URL is blocked
    current_url = webbrowser.get().open_new_tab("about:blank").location

    for site in blocked_sites:
        if site in current_url:
            webbrowser.get().open_new_tab("about:blank")
            print(f"Access to {site} is blocked for {block_duration / 60} minutes.")
            time.sleep(5)

print("Access to blocked sites has been restored.")
