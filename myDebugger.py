from sys import exit

from winappdbg import win32, Debug, HexDump, Crash


# try:
#    from winappdbg import CrashDAO
# except ImportError:
#    raise ImportError("Error: SQLAlchemy is not installed!")

def my_event_handler(event):
    # Get the event name.
    name = event.get_event_name()

    # Get the event code.
    code = event.get_event_code()

    # Get the process ID where the event occured.
    pid = event.get_pid()

    # Get the thread ID where the event occured.
    tid = event.get_tid()

    # Get the value of EIP at the thread.
    pc = event.get_thread().get_pc()

    # Show something to the user.
    bits = event.get_process().get_bits()
    format_string = "%s (%s) at address %s, process %d, thread %d"
    message = format_string % (name,
                               HexDump.integer(code, bits),
                               HexDump.address(pc, bits),
                               pid,
                               tid)
    print message

    # If the event is a crash...
    if code == win32.EXCEPTION_DEBUG_EVENT and event.is_last_chance():
        print "Crash detected, storing crash dump in database..."

        # Generate a minimal crash dump.
        crash = Crash(event)
        print crash

        # You can turn it into a full crash dump (recommended).
        # crash.fetch_extra_data( event, takeMemorySnapshot = 0 ) # no memory dump
        # crash.fetch_extra_data( event, takeMemorySnapshot = 1 ) # small memory dump
        # crash.fetch_extra_data( event, takeMemorySnapshot=2 ) # full memory dump
        # Connect to the database. You can use any URL supported by SQLAlchemy.
        # For more details see the reference documentation.
        # dao = CrashDAO( "sqlite:///crashes.sqlite" )
        # dao = CrashDAO( "mysql+MySQLdb://root:toor@localhost/crashes" )
        # Store the crash dump in the database.
        # dao.add( crash )
        # If you do this instead, heuristics are used to detect duplicated
        # crashes so they arent added to the database.
        # dao.add( crash, allow_duplicates = False )
        # You can also launch the interactive debugger from here. Try it! :)
        # event.debug.interactive()
        # Kill the process.
        event.get_process().kill()

    return


def simple_debugger(argv):
    # Instance a Debug object.
    debug = Debug()
    try:
        # Start a new process for debugging.
        debug.execv(argv)
        # Launch the interactive debugger.
        debug.interactive()
    # Stop the debugger.
    finally:
        debug.stop()
    return
