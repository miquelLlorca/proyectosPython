from sympy import factorint


#####################################################################################################
LABELS = ['A','B','C','D','S']
def encode_label(label):
    if(label == ''):
        return 0
    pos = LABELS.index(label[0])
    return (pos+1)*int(label[1])
def decode_label(label):
    if(label==0):
        return ''
    label -= 1
    return LABELS[label%(len(LABELS))]+str(1+int(label/(len(LABELS))))

#####################################################################################################
INSTRUCTIONS = ['==','++','--','GOTO']
def encode_instruction(instruction):
    if('GOTO' in instruction):
        return 2 + encode_label(instruction.split()[3])
    
    for i, item in enumerate(INSTRUCTIONS):
        if(item == instruction[-2:]):
            return i
    return None
def decode_instruction(instruction):
    return INSTRUCTIONS[instruction]

#####################################################################################################
def encode_variable(instruction):
    if('GOTO' in instruction):
        # if z!=0 goto a
        variable = instruction.split()[1][:2]
    else:
        variable = instruction[:2]
        
    if(variable[0] == 'Y'):
        return 0
    code = 2*int(variable[1]) if variable[0]=='X' else 2*int(variable[1])+1
    return code - 1
def decode_variable(variable):
    variable += 1
    if(variable == 1):
        return 'Y'
    vars = ['X','Z']
    return vars[variable%2]+str(int(variable/2))

#####################################################################################################
def encode_line(line):
    a = encode_label(line[0])
    b = encode_instruction(line[1])
    c = encode_variable(line[1])
    return encode_pair(a,encode_pair(b,c))
def decode_line(x):
    label, b = decode_pair(x)
    instr, variable = decode_pair(b)
    goto = instr-2 if instr > 2 else 0
    
    full_line = [decode_label(label), '']
    if(instr > 2):
        full_line[1] = f'IF {decode_variable(variable)}!=0 GOTO {decode_label(goto)}'
    else:
        full_line[1] = decode_variable(variable) + decode_instruction(instr)
        
    return label, instr, variable, goto, full_line

#####################################################################################################
def encode_pair(a,b):
    return (2**a * (2*b + 1))-1
def decode_pair(x):
    x += 1
    for i in range(x):
        if(x%(2**(i+1)) != 0):
            a = i
            break
    b = int(((x/2**a)-1)/2)
    return a, b

#####################################################################################################
PRIMES = [2,3,5,7,11,13,17,19,23,29,31]
def encode_list(list):
    value = 1
    for i, item in enumerate(list):
        value *= PRIMES[i]**item
        print(f'{PRIMES[i]}^{item}',end=' · ')
    print()
    return value
def decode_list(x):
    lista = []
    factores = factorint(x)
    for key, item in factores.items():
        lista.append(item)
    return lista

#####################################################################################################
def encode_program(program):
    encoded_lines = []
    for line in program:
        a = encode_label(line[0])
        b = encode_instruction(line[1])
        c = encode_variable(line[1])
        value = encode_line(line)
        encoded_lines.append(value)
        print(line)
        print(f'   <{a},<{b},{c}>> => {value}')
        print()
    print(encoded_lines)
    return encoded_lines

def decode_program(x):
    encoded_lines = decode_list(x+1)
    program = []
    for line in encoded_lines:
        decoded = decode_line(line)
        program.append(line)
        print(f'{line} -> {decoded[:-1]} -> {decoded[-1]}')
        
        


#####################################################################################################

if(__name__=="__main__"):
    # ['A1','if X1!=0 GOTO B1'],
    # ['','Z1++'],
    # ['','if Z1!=0 GOTO S1'],
    # ['B1','X1--'],
    # ['','Y++'],
    # ['','Z1++'],
    # ['','if Z1!=0 GOTO A1'],
    # 
    # ['A1','X1++'],
    # ['','if X1!=0 GOTO A1']
    # 
    # ['A1','if X1!=0 GOTO A1'],
    # ['','Z1++'],
    # ['','if Z1!=0 GOTO S1'],
    # ['','X1--'],
    # ['','Y++'],
    # ['','Z1++'],
    # ['','if Z1!=0 GOTO A1'],
    # 
    # ['','Z1++'],
    # ['C1','if X2!=0 GOTO A1'],
    # ['','if Z1!=0 GOTO S1'],
    # ['A1','if X1!=0 GOTO B1'],
    # ['','if Z1!=0 GOTO A1'],
    # ['B1','X1--'],
    # ['','X2--'],
    # ['','if Z1!=0 GOTO C1'],
    program = [
        ['A1','X1--'],
        ['','Y++'],
        ['','if X1!=0 GOTO A1'],
    ]
    # encode_program(program)
    # print(decode_line(45))
    
    print(encode_pair(2,1))
    # p = 575#20780180811943383690687834675647971696770263629993897588428988938159395306289159456888626718029570181332625597671752474299404131332247315678654847840861888200712035882367022776256612130457818994494713564496364989056428857984352021877405035458603114653994837408229450170906541444901121677661807243120491133833323166688121663510235083450213180581928579137195537740330917414769714353984605721734452709186409242922209235124381408583026990350820699746993896145540762898048737958971404064659281292087927369580990882606624598147821917519639688927063223067225401194815143121863834478964026238440917189670580673467361416719637360264262972372113159953418249546918400750407178596560717420327162686112599568168346567894183796586696779500055795402553974328000596177890766085152369703433510415402732482172033183980270284236055407298290194950119042820338469099526922262262741538737333036654927192438960909715688983963323501104252441790706879060620290461924315876555447727592241645609981654608831832742983407702203169170897298524400929621469797500281666884227668630516736435858834136856600039207984923561552815014566929410575834744176019956571314919343843125582177064631072919734393251649519225876468215559886904460775428690391271015039604625352241856471101333755294005976106330072295737401183456686210623328674766616881656424251363782702829163872737806053241763107842042705472986090393431258803644759408916418282467339952190530314753614792539057248492215434460367864655135423984537605578899606877204428848115877257727866133881916363201051591755971512035329181052604271569477094769123445214537727169857857473130779627037883011933890735009642658826790439896987075020925881823860796277747981479096493632153550192289188712246372719481560682225878794535522256897806374468281073006020912992702851755739834659128081035794811974374767501651761609581900195978766505385417020079142329636348856280317163253589533717810854601431084606761953095184568751136556642475245468558997783818625083723722139049212912884817559835964052511915944578146155570213820026039870839608966387060712860184970027548355653076853945260271672168528311885893344879150390624999999999999999999
    # decode_program(p)
