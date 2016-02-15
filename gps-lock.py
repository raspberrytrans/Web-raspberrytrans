import gps
import time

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
data = 1
while (data == 1):
 try:
      	report = session.next()
        if report['class'] == 'TPV':
           if hasattr(report, 'lat'):
              print report.lat
        if report['class'] == 'TPV':
           if hasattr(report, 'lon'):
              print report.lon
        if report['class'] == 'TPV':
           if hasattr(report, 'alt'):
              print report.alt
              data = 2
 except KeyError:
  	        pass
 except KeyboardInterrupt:
   		quit()
 except StopIteration:
    		session = None
   		print "GPSD has terminated"

