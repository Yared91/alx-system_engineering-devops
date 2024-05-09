Postmortem: E-commerce Checkout Outage
Issue Summary

Duration: 30 minutes (10:00 AM EAT - 10:30 AM EAT)
Impact: Our e-commerce checkout system experienced a critical outage, preventing users from completing their purchases. This affected 100% of users attempting checkout during the outage window.
Timeline

10:00 AM EAT: Monitoring alerts indicated a surge in failed transactions at the payment processing gateway.
10:01 AM EAT: An engineer on duty investigated the alerts and identified a significant increase in database connection timeouts.
10:02 AM - 10:10 AM EAT: The engineer focused on the database server, suspecting a resource overload. They investigated available memory, CPU usage, and disk space, but found no anomalies.
10:10 AM EAT: The engineer escalated the issue to the database administration team.
10:15 AM EAT: The database team identified a recent configuration change to a key database connection pool setting, which had inadvertently limited the number of available connections.
10:20 AM EAT: The database team reverted the connection pool setting to the previous configuration.
10:25 AM EAT: Monitoring confirmed successful transactions resuming at the payment gateway.
10:30 AM EAT: The engineer declared the issue resolved and communicated the resolution to relevant teams.
Root Cause and Resolution

A recent database configuration change inadvertently limited the number of available connections to the database server. This bottleneck caused application timeouts when the number of concurrent checkout attempts exceeded the available connections. Reverting the configuration change restored the pool size and allowed the system to handle concurrent requests.

Corrective and Preventative Measures

Improved code review process: Implement a more thorough code review process to identify potential configuration changes that could impact system performance.
Automated database connection pool monitoring: Implement automated monitoring that alerts on critical database connection pool settings.
Standardize rollback procedures: Develop standardized rollback procedures for database configuration changes to minimize downtime in case of unforeseen issues.
Team training: Conduct training sessions to sensitize engineers on the criticality of database configuration changes and the importance of thorough testing before deployment.

additional tips for making a postmortem more interesting:

Use clear and concise language: Avoid technical jargon whenever possible. Explain complex concepts in a way that's easy to understand.
Focus on storytelling: Frame the postmortem as a story with a clear beginning, middle, and end. This will help keep readers engaged.
Highlight the learnings: Don't just focus on what went wrong. Make sure to emphasize what you learned from the experience and how you'll prevent similar issues in the future.
