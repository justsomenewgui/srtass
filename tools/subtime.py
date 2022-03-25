class SubTime:
    def __init__(self, seconds=0, milliseconds=0, minutes=0):
        self.seconds = seconds
        self.milliseconds = milliseconds
        self.minutes = minutes

    def timechanger(self, line, x):
        """Fixes subtitle timecode. line[x] is a milliseconds."""
        msLine = int(line[x]) + self.milliseconds
        secLine = int(line[x-1]) + self.seconds
        minLine = int(line[x-2]) + self.minutes
        # milliseconds bloc:
        if msLine < 0:
            while msLine < 0:
                secLine = secLine - 1
                msLine = 1000 + msLine
                line[x] = str(msLine).zfill(3)
        elif msLine > 999:
            while msLine > 999:
                secLine = secLine + 1
                msLine = msLine - 1000
                line[x] = str(msLine).zfill(3)
        else:
            line[x] = str(msLine).zfill(3)
        # seconds bloc:
        if secLine < 0:
            while secLine < 0:
                minLine = minLine - 1
                secLine = 60 + secLine
                line[x-1] = str(secLine).zfill(2)
        elif secLine > 59:
            while secLine > 59:
                minLine = minLine + 1
                secLine = secLine - 60
                line[x-1] = str(secLine).zfill(2)
        else:
            line[x-1] = str(secLine).zfill(2)
        # minutes bloc:
        if minLine < 0:
            while minLine < 0:
                hourLine = int(line[x-3]) - 1
                line[x-3] = str(hourLine).zfill(2)
                minLine = 60 + minLine
                line[x-2] = str(minLine).zfill(2)
        if minLine > 59:
            while minLine > 59:
                hourLine = int(line[x-3]) + 1
                line[x-3] = str(hourLine).zfill(2)
                minLine = minLine - 60
                line[x-2] = str(minLine).zfill(2)   
        else:
            line[x-2] = str(minLine).zfill(2)
        return line
