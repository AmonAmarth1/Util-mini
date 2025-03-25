
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
    register_converter = {"input_converter_modbus_use": 7, "output_converter_modbus_use": 8, "input_count": 51, "output_count": 60, "input_type": 53, "output_type": 52}

    type_heat1 = {"electrical": "HE1", "humid": "Y1"}
    type_heat2 = {"humid": "Y2"}
    reg_heat = {"heat1_type": 22, "heat2_use": 17, "heat2_type": 16}

    type_recup = {"plastina": "3Y1", "rotor": "9U1", "glikol": "Y5"}
    reg_recup = {"use_recup": 19, "type_recup": 1817}

print(Literal.types_key_UO)
print(Literal.types_key_io)
print(Literal.types_key_UO['UO1'])

