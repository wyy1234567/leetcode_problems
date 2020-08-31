# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

#hour: 30/hr
#min: 6/min

def clock_angle(hour, minutes)
    h = (hour % 12) * 30 + (minutes.to_f / 60) * 30
    minute = minutes * 6
    [(h - minute).abs, 360 - (h - minute).abs].min
end

puts clock_angle(12, 30)