def rtd( **args ):
    if "rate" in args and  "time" in args:
        args["distance"]= args["rate"]*args["time"]
    elif  "rate" in args and  "distance" in args:
        args["time"]= args["distance"]/args["rate"]
    elif  "time" in args and  "distance" in args:
        args["rate"]= args["distance"]/args["time"]
    else:
        raise Exception("%r does not compute" % ( args, ) )
    return args
#-------------------------------
print (rtd( rate = 60, time = 0.75 ))
print()
print (rtd( distance = 173, time = 2 ))
