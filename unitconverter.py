import pandas


user_input=input("What do you want to convert?[Distance or Time] ")


user_input_for_col=user_input+":unit"


user_input_list=user_input+":value"


data= pandas.read_csv('conversion_table.csv', index_col=user_input_for_col)


data_dict=data.to_dict()

conversions_list=data_dict[user_input_list]

def value_valid_checker(value):
    try:
        value = int(value)

    except ValueError:
        try:
            value = (input("Pls enter the value again"))
            value_valid_checker(value)
        finally:
            pass


def conversion_checker():
    if user_input == "Distance":
        if input_unit in conversions_list.keys():
            pass
        elif output_unit in conversions_list.keys():
            pass
        else:
            print("Conversion is not possible. Sorry!!")
            exit()


def converting(val,unit_in,unit_out):
    return val * conversions_list[unit_in] / conversions_list[unit_out]

input_unit=input("Which unit you want to convert??")
output_unit = input("Which unit you want to be converted into??")
value=input("Pls enter the value")
value_valid_checker(value)
value = int(value)
conversion_checker()
print(converting(value,input_unit,output_unit))

