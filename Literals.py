
class Literal:
    DIGITAL_INPUT = 2
    RESISTANCE_INPUT = 3
    DIGITAL_OUTPUT = 17
    VOLTAGE_OUTPUT = 18

    BIT_0 = 1
    BIT_1 = 2
    BIT_2 = 4
    BIT_3 = 8
    BIT_4 = 16
    BIT_5 = 32
    BIT_6 = 64
    BIT_7 = 128

    DEFAULT_BIN_OUTPUT_DIGIT = 32512

    NUMBER_UNIVERSAL_OUTPUT = 8

    POSITION_REG_BIN_DIGIT = 3
    reg_bin_digit = 303

    NEW_BIN_NUM_1 = DEFAULT_BIN_OUTPUT_DIGIT | BIT_0
    NEW_BIN_NUM_2 = DEFAULT_BIN_OUTPUT_DIGIT | BIT_1
    NEW_BIN_NUM_3 = DEFAULT_BIN_OUTPUT_DIGIT | BIT_2
    NEW_BIN_NUM_4 = DEFAULT_BIN_OUTPUT_DIGIT | BIT_3
    NEW_BIN_NUM_5 = DEFAULT_BIN_OUTPUT_DIGIT | BIT_4
    NEW_BIN_NUM_6 = DEFAULT_BIN_OUTPUT_DIGIT | BIT_5
    NEW_BIN_NUM_7 = DEFAULT_BIN_OUTPUT_DIGIT | BIT_6
    NEW_BIN_NUM_8 = DEFAULT_BIN_OUTPUT_DIGIT | BIT_7

    types_key_UO = {'UO1': NEW_BIN_NUM_1, 'UO2': NEW_BIN_NUM_2, 'UO3': NEW_BIN_NUM_3, 'UO4': NEW_BIN_NUM_4, 'UO5': NEW_BIN_NUM_5, 'UO6': NEW_BIN_NUM_6, 'UO7': NEW_BIN_NUM_7, 'UO8': NEW_BIN_NUM_8}
    types_key_io = {'Di': DIGITAL_INPUT, 'Ai': RESISTANCE_INPUT, 'Do': DIGITAL_OUTPUT, 'Ao': VOLTAGE_OUTPUT}
    types_product_num = {"NC": 1, "NO": 2, "3950": 7, "3435": 8}

    input_vent = "1U"
    output_vent = "2U"
    types_converter = {"INVT": 0, "VCI": 2, "LCI": 3, "Danfoss": 4, "Canroon": 5}
    register_converter = {"input_converter_modbus_use": 8, "output_converter_modbus_use": 7, "input_count": 51, "output_count": 60, "input_type": 53, "output_type": 52}

    '''
       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       type_reg: 6 - WRITE SINGLE REGISTER, 5 - WRITE SINGLE COIL, 7 - Write long 4 byte
       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    type_reg_converter = {"input_converter_modbus_use": 5, "output_converter_modbus_use": 5, "input_count": 6, "output_count": 6, "input_type": 6, "output_type": 6}


    type_heat1 = {"electrical": "HE1", "liquid": "Y1"}
    type_heat2 = {"humid": "Y2"}
    reg_heat = {"heat1_type": 22, "heat2_use": 17, "heat2_type": 16}
    type_reg_heat = {"heat1_type": 5, "heat2_use": 5, "heat2_type": 5}

    type_recup = {"plastina": "3Y1", "rotor": "9U1", "glikol": "Y5"}
    reg_recup = {"use_recup": 19, "type_recup": 1817}
    type_reg_recup = {"use_recup": 5, "type_recup": 6}

    type_dx = {"freon": "E1", "liquid": "Y3"}
    reg_dx = {"use_dx": 24, "config_dx": 1627}
    type_reg_dx = {"use_dx": 5, "config_dx": 6}

    humidifier_type = {0: "TH1"}
    reg_humidifier = {"humidifier_use": 11}
    type_reg_humidifier = {"humidifier_use": 5}

    mix_camera = {0: "4Y1"}
    reg_mix_camera = {"mix_camera_use": 21}
    type_reg_mix_camera = {"mix_camera_use": 5}

    N_T_IN = 2
    N_H_IN = 14
    N_T_ROOM = 4
    N_H_ROOM = 12
    N_T_OUT = 3
    N_H_OUT = 13
    sensor_name_num = {"TH1": (N_T_IN, N_H_IN), "TH2": (N_T_ROOM, N_H_ROOM), "TH3": (N_T_OUT, N_H_OUT)}
    sensor_name_var = {"TH1": "температура приток, влажность приток", "TH2": "температура помещения, влажность помещения", "TH3": "температура вытяжки, влажность вытяжки"}
    sensor_type = {"LMF": 1, "ПЛВ-АМ": 2, "ДТВК-АМ": (3,4), "ДТВП-АМ": (3,4), "conel": (5,6), "LFH10R2": (7,8), "Oj PTH": 9, "DSC-G": 10, "ПДВ-2К": 11, "ПДВ-1К": 12}
    reg_modbus_sensor = {"id_sensor_1": 63, "type_sensor_1": 700, "type_var_sensor_1": 732, "modbus_sensors_use": 12, "sensors_use_bit": 189}
    type_reg_modbus_sensor = {"id_sensor_1": 6, "type_sensor_1": 6, "type_var_sensor_1": 6, "modbus_sensors_use": 5, "sensors_use_bit": 7}

print(Literal.sensor_name_num['TH1'][0])
print(Literal.sensor_name_num['TH1'][1])

print(Literal.types_key_UO)
print(Literal.types_key_io)
print(Literal.types_key_UO['UO1'])

