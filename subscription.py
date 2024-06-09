# subscription.py
import re
class RateLimiter:
    def __init__(self, max_requests):
        self.max_requests = max_requests
        self.requests = []

    def add_request(self, request_time):
        self.requests.append(request_time)

        # Remove requests outside of the time window
        self.requests = [req for req in self.requests if req > request_time - 60]

        if len(self.requests) > self.max_requests:
            return False
        else:
            return True

# Usage
limiter = RateLimiter(10)  # 10 requests per minute

# Simulate requests
request_times = range(15)  # Simulate 15 requests in 15 seconds
for request_time in request_times:
    if limiter.add_request(request_time):
        print("Request allowed")
    else:
        print("Too many requests, please slow down")

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

def store_email(email):
    with open('/tmp/subscribers.txt', 'a') as f:
        f.write(email + '\n')

# You can use this function to store emails. For example:
store_email('example@example.com')

