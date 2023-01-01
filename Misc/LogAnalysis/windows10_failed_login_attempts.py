import win32evtlog

# Open the system log
log_handle = win32evtlog.OpenEventLog("localhost", "System")

# Set the number of events to retrieve
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(log_handle)
print("Total records : ", total)
# Read the events in the log
events = win32evtlog.ReadEventLog(log_handle, flags, 0, total)

# Iterate through the events and print the details of any failed login attempts
for event in events:
  if event.EventID == 4625:  # Event ID for failed login attempts
    print("Failed login attempt detected:")
    print("  Time Generated:", event.TimeGenerated)
    print("  Source Name:", event.SourceName)
    print("  Message:", event.StringInserts)

# Close the log
win32evtlog.CloseEventLog(log_handle)
