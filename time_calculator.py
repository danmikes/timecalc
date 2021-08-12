def add_time(start, duration, day = ""):

  dayList = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  durationTuple = duration.partition(":")
  durationHours = int(durationTuple[0])
  durationMinutes = int(durationTuple[2])

  print(start)

  startSplit = start.partition(" ")
  startTuple = startSplit[0].partition(":")
  startHours = int(startTuple[0])
  startMinutes = int(startTuple[2])
  meridiem = startSplit[2]

  meridiemFlip = {"AM": "PM", "PM": "AM"}

  amountDays = int(durationHours / 24)
  print(amountDays)

  endMinutes = startMinutes + durationMinutes
  if (endMinutes > 60):
    startHours += 1
    endMinutes %= 60
  amountFlips = int((startHours + durationHours) / 12)
  endHours = (startHours + durationHours) % 12

  endMinutes = endMinutes if endMinutes > 9 else "0" + str(endMinutes)
  endHours = 12 if endHours == 0 else endHours
  if (meridiem == "PM" and startHours + (durationHours % 12)) >= 12:
    amountDays +=1

  meridiem = meridiemFlip[meridiem] if amountFlips % 2 == 1 else meridiem

  returnTime = str(endHours) + ":" + str(endMinutes) + " " + meridiem

  if (day):
    day = day.lower()
    index = int((dayList.index(day)) + amountDays) % 7
    newDay = dayList[index].capitalize()
    returnTime += ", " + newDay

  if (amountDays == 1):
    return returnTime + " (next day)"
  elif (amountDays > 1):
    return returnTime + " (" + str(amountDays) + " days later)"

  return returnTime
