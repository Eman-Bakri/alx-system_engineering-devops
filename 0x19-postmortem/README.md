
# Postmortem Incident Report

## An outage in API infrastructure
![Website is down.](https://preview.redd.it/6ll9ab69kou51.png?width=1080&crop=smart&auto=webp&s=701c1625ad2c2af7d40020f2e7aa4c35ce05ed98))
### Issue Summary:
On February 4th, 2024 at 8:04 p.m. attempts to access various APIs generated 500 error responses. As a result, applications dependent on these APIs experienced several errors or affected its functionality negatively during this time frame. The furthest of the problem impacted 100% of traffic directed towards the affected API infrastructure. However, users were still able to utilize specific APIs running on distinct infrastructures. The primary reason for this outage was identified as an erroneous configuration modification that uncovered a flaw in a commonly employed internal library.

### Timeline:
- 7:52 : Modification of configuration implemented.
- 8:04 : Outage started.
- 8:04: Development and incidents teams were alerted.
- 8:37: Unsuccessful attempt to revert the configuration change.
- 9:01 : Successful attempt to revert the configuration change.
- 9:06 : Servers running again.
- 9:41 : All online traffic has been fully restored.

### Root cause and resolution:
At 7:52 p.m., an unintentional release of a configuration change occurred in our production environment, bypassing the testing environment. This change included an incorrect address for the authentication servers in the production setup. As a result, a flaw in the authentication libraries emerged, causing them to get stuck indefinitely. Simultaneously, the internal monitoring systems became permanently blocked during this interaction with the authentication library. The combination of the bug and the configuration error rapidly led to the consumption of all serving threads. Traffic became perpetually queued, awaiting an available serving thread. Consequently, the servers experienced frequent hangs and restarts as they tried to recover, initiating the service outage at 8:04 p.m.

The teams were alerted at 8:04 p.m. in which they immediately started investigating the issue and searching the case. it was identified that it was initiated by the bug resulting from the configuration change. By 8:37, the team was trying to take back the configuration that caused the problem but it failed due to system complexity. However, the team succeeded in rolling it back at 9:01. Certain processes began a gradual recovery, which concluded that a quicker recovery could be achieved through a global restart of all API infrastructure servers. 
At 7:32 p.m. a quarter of the traffic had been reinstated, and by 9:41 p.m., the entirety of the traffic was directed to the API infrastructure.

### Corrective and preventative measures:
Over the past 48 hours, the team conducted an internal assessment of the outage and identified measures to address the root causes, aiming to prevent recurrence and enhance response times. The identified actions include:

1. Temporarily disabling the current configuration release mechanism until safer alternatives are implemented (already completed).
2. Enhancing the rollback process to be faster and more robust.
3. Rectifying the underlying issues in authentication libraries and monitoring to ensure proper timeout/interruption on errors.
4. Implementing programmatically enforced staged rollouts for all configuration changes.
5. Improving the auditing process for high-risk configuration options.
6. Introducing a faster rollback mechanism and enhancing the traffic ramp-up process to swiftly address any future similar issues.
7. Developing a more efficient mechanism for promptly delivering status notifications during incidents.




