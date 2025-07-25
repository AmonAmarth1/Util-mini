
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
    pwm_out = 290

    I_LENGTH = 18
    I_UNIVERSAL_LENGTH = 6
    O_LENGTH = 8
    Q_LENGTH = 5
    T_LENGTH = 2

    SENS_LENGTH = 10

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
    types_io_input = {0: "Voltage", 1: "Current", 2: "Digital", 3: "Resistance"}
    types_io_output = {0: "0-10V", 1: "PWM", 2: "Digital"}
    types_io_output_2 = {18: "0-10V", 19: "PWM", 17: "Digital"}
    OUT_0_10V = 18
    OUT_DIGIT = 17
    types_product_num = {"--": 0, "NC": 1, "NO": 2, "4-20мА": 3, "0-1": 4, "0-5": 5, "0-10": 6, "3950": 7, "3435": 8, "NTC20k": 9, "pt1000": 10}


    reg_analog_var_access = 256

    input_vent = "1U"
    output_vent = "2U"
    types_converter = {"INVT": 0, "другой": 1, "VCI": 2, "LCI": 3, "Danfoss": 4, "Canroon": 5}
    types_converter_num = {0: "INVT", 1: "другой", 2: "VCI", 3: "LCI", 4: "Danfoss", 5: "Canroon"}
    register_converter = {"input_converter_modbus_use": 8, "output_converter_modbus_use": 7, "input_count": 51, "output_count": 60, "input_type": 53, "output_type": 52, "input_type_reserve": 1686, "output_type_reserve": 1655, "input_adres_1": 55, "output_adres_1": 54}
    reserve_converter = {0: "нет", 1: "Группа", 2: "Горячий", 3: "Каскадный"}
    '''
       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       type_reg: 6 - WRITE SINGLE REGISTER, 5 - WRITE SINGLE COIL, 7 - Write long 4 byte
       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    WRITE_LONG = 7

    type_reg_converter = {"input_converter_modbus_use": 5, "output_converter_modbus_use": 5, "input_count": 6, "output_count": 6, "input_type": 6, "output_type": 6, "input_type_reserve": 6, "output_type_reserve": 6, "input_adres_1": 6,"output_adres_1": 6}


    type_heat1 = {"electrical": "HE1", "liquid": "Y1"}
    type_heat_num = {0: "electrical", 1: "liquid"}
    type_heat_pump_reserve = {0: "Нет", 1: "Есть"}
    type_heat2 = {"humid": "Y2"}
    reg_heat = {"heat1_type": 22, "heat2_use": 17, "heat2_type": 16, "heat1_resereve_pump": 37,  "heat2_resereve_pump": 38}
    type_reg_heat = {"heat1_type": 5, "heat2_use": 5, "heat2_type": 5, "heat1_resereve_pump": 5, "heat2_resereve_pump": 5}

    type_recup = {"plastina": "3Y1", "rotor": "9U1", "glikol": "Y5"}
    type_recup_num = {0: "None", 1: "plastina", 2: "rotor", 3: "glikol"}
    reg_recup = {"use_recup": 19, "type_recup": 1817, "activate_modbus": 142, "id": 678, "nominal_rpm": 679, "type_conv": 680}
    type_reg_recup = {"use_recup": 5, "type_recup": 6, "activate_modbus": 5, "id": 6, "nominal_rpm": 6, "type_conv": 6}

    type_dx = {"freon": "E1", "liquid": "Y3"}
    type_dx_num = {0: "-", 1: "A", 2: "AA", 3: "AAA", 4: "AD", 5: "ADD"}
    reg_dx = {"use_dx": 24, "config_dx": 1627, "heat_dx": 25}
    type_reg_dx = {"use_dx": 5, "config_dx": 6, "heat_dx": 5}

    humidifier_type = {0: "TH1"}
    reg_humidifier = {"humidifier_use": 11, "drainage_use": 70}
    type_reg_humidifier = {"humidifier_use": 5, "drainage_use": 5}


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
    sensor_type_single = {1: "LMF", 2: "ПЛВ-АМ", 3: "ДТВК-АМ", 4: "ДТВК-АМ", 5: "conel", 6: "conel", 7: "LFH10R2", 8: "LFH10R2", 9: "Oj PTH", 10: "DSC-G", 11: "ПДВ-2К", 12: "ПДВ-1К"}
    sensor_type_single_gui = {0: "LMF 51 100 Pa", 1: "LMF 51 10k Pa", 2: "Vemax ПДВ-АМ 1000Pa", 3: "ДТВК-АМтемпература", 4: "ДТВК-АМвлажность", 5: "Conel влажность", 6: "Conel температура", 7: "LFH10R температура",
                          8: "LFH10R влажность", 9: "Oj PTH", 10: "DSC-G", 11: "ПДВ 2K <2K", 12: "ПДВ 2К >2K"}
    reg_modbus_sensor = {"id_sensor_1": 63, "type_sensor_1": 700, "type_var_sensor_1": 732, "modbus_sensors_use": 12, "sensors_use_bit": 189}
    type_reg_modbus_sensor = {"id_sensor_1": 6, "type_sensor_1": 6, "type_var_sensor_1": 6, "modbus_sensors_use": 5, "sensors_use_bit": 7}

print(Literal.sensor_name_num['TH3'][0])
print(Literal.sensor_name_num['TH3'][1])
print(Literal.sensor_type_single[1])

print(Literal.types_key_UO)
print(Literal.types_key_io)
print(Literal.types_key_UO['UO1'])

