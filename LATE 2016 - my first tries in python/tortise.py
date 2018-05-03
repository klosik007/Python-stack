import math

def race(v1, v2, g):
    time = []
    t = round(g / ((v2-v1)/3600), 3)

    if t < 3600:
        time.append(0.0)
        time.append( round(t/60, 0))
        time.append( round( (round(t/60, 1) - time[1])*60 , 0))
    else:
        time.append(round(t/3600, 0))
        time.append(math.floor( (t-time[0]*3600)/60))
        time.append( math.floor((((t-time[0]*3600)/60) - time[1])*60) )
        
        
    print (time)

race(720,850,70)
