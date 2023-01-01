
import win32evtlog

# Open the output file
with open("system_log.txt", "w") as f:
  # Open the system log
  log_handle = win32evtlog.OpenEventLog("localhost", "System")

  # Set the number of events to retrieve
  flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
  total = win32evtlog.GetNumberOfEventLogRecords(log_handle)

  # Read the events in the log
  events = win32evtlog.ReadEventLog(log_handle, flags, 0, total)

  # Iterate through the events and write them to the file
  for event in events:
    f.write("Event ID: " + str(event.EventID) + "\n")
    f.write("Time Generated: " + str(event.TimeGenerated) + "\n")
    f.write("Source Name: " + event.SourceName + "\n")
    f.write("Message: " + str(event.StringInserts) + "\n")
    f.write("="*30+"\n")
