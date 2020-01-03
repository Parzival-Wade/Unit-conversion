SI_time ={'s':1,'ms':0.001,'h':3600,'day':86400,'wk':604800,'mo':2628000,'yr':31536000,'century':3153600000,'millennium':31536000000.}
SI_dist = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000, 'mi':1609.344, 'yd':0.9144,'ft':0.3048,'in':0.0254,}

def value_valid_checker(value):
  try:
   value = int(value)
   
  except ValueError:
    try:
      value=(input("Pls enter the value again"))
      value_valid_checker(value)
    finally:
      pass


def conversion_checker():
  if user_input=="Distance":
    if input_unit in SI_dist.keys():
      pass
    elif output_unit in SI_dist.keys():
      pass
    else:
      print("Conversion is not possible. Sorry!!")
      exit()


def convert_SI_dist(val, unit_in, unit_out):
    return val*SI_dist[unit_in]/SI_dist[unit_out]

def convert_SI_time(val,unit_in, unit_out):
    return val * SI_time[unit_in] / SI_time[unit_out]



user_input=input("What do you want to convert?[Distance or Time] ")




if user_input=="Distance" :
    input_unit=input("Which unit you want to convert??[mm,cm,m,km,mi,yd,ft,in]")
    output_unit = input("Which unit you want to be converted into??[mm,cm,m,km,mi,yd,ft,in]")
    value=input("Pls enter the value")
    value_valid_checker(value)
    value = int(value)
    conversion_checker()
    print( convert_SI_dist(value,input_unit,output_unit))


elif user_input=="Time" :
    input_unit=input("Which unit you want to convert??[s,ms,h,day,wk,mo,yr,century,millennium]")
    output_unit = input("Which unit you want to be converted into??[s,ms,h,day,wk,mo,yr,century,millennium]")
    value=(input("Pls enter the value"))
    value_valid_checker(value)
    value = int(value)
    conversion_checker()   
    print( convert_SI_time(value,input_unit,output_unit))




