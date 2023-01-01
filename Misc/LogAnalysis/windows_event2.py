import win32evtlog

# Open the system log and the output file
log_handle = win32evtlog.OpenEventLog("localhost", "System")
with open("output.txt", "w") as output_file:
  # Set the number of events to retrieve
  flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
  total = win32evtlog.GetNumberOfEventLogRecords(log_handle)
  # Read the events in the log
  events = win32evtlog.ReadEventLog(log_handle, flags, 0, total)
  # Iterate through the events and write the details to the output file
  for event in events:
    output_file.write(f"Event ID: {event.EventID}\n")
    output_file.write(f"Time Generated: {event.TimeGenerated}\n")
    output_file.write(f"Source Name: {event.SourceName}\n")
    output_file.write(f"Message: {event.StringInserts}\n")
    output_file.write("="*30+"\n")
