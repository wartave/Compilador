# Generated from LexerVictor.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,43,271,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,1,0,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,
        1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,20,1,20,
        1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,
        1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,4,35,213,8,35,11,35,
        12,35,214,1,35,1,35,1,36,1,36,1,36,1,36,5,36,223,8,36,10,36,12,36,
        226,9,36,1,36,1,36,1,37,1,37,5,37,232,8,37,10,37,12,37,235,9,37,
        1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,
        1,40,4,40,251,8,40,11,40,12,40,252,1,41,4,41,256,8,41,11,41,12,41,
        257,1,42,5,42,261,8,42,10,42,12,42,264,9,42,1,42,1,42,4,42,268,8,
        42,11,42,12,42,269,0,0,43,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,
        20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,
        31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,
        42,85,43,1,0,5,3,0,9,10,13,13,32,32,2,0,10,10,13,13,3,0,10,10,13,
        13,34,34,3,0,65,90,95,95,97,122,1,0,48,57,277,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,
        0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,
        0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,
        0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,
        0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,
        0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,
        0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,
        0,0,0,85,1,0,0,0,1,87,1,0,0,0,3,93,1,0,0,0,5,98,1,0,0,0,7,102,1,
        0,0,0,9,108,1,0,0,0,11,113,1,0,0,0,13,115,1,0,0,0,15,117,1,0,0,0,
        17,119,1,0,0,0,19,121,1,0,0,0,21,123,1,0,0,0,23,125,1,0,0,0,25,127,
        1,0,0,0,27,129,1,0,0,0,29,132,1,0,0,0,31,135,1,0,0,0,33,138,1,0,
        0,0,35,141,1,0,0,0,37,144,1,0,0,0,39,147,1,0,0,0,41,149,1,0,0,0,
        43,151,1,0,0,0,45,153,1,0,0,0,47,155,1,0,0,0,49,157,1,0,0,0,51,159,
        1,0,0,0,53,161,1,0,0,0,55,163,1,0,0,0,57,165,1,0,0,0,59,175,1,0,
        0,0,61,184,1,0,0,0,63,191,1,0,0,0,65,196,1,0,0,0,67,203,1,0,0,0,
        69,206,1,0,0,0,71,212,1,0,0,0,73,218,1,0,0,0,75,229,1,0,0,0,77,238,
        1,0,0,0,79,243,1,0,0,0,81,250,1,0,0,0,83,255,1,0,0,0,85,262,1,0,
        0,0,87,88,5,118,0,0,88,89,5,101,0,0,89,90,5,114,0,0,90,91,5,115,
        0,0,91,92,5,97,0,0,92,2,1,0,0,0,93,94,5,119,0,0,94,95,5,111,0,0,
        95,96,5,114,0,0,96,97,5,107,0,0,97,4,1,0,0,0,98,99,5,105,0,0,99,
        100,5,110,0,0,100,101,5,116,0,0,101,6,1,0,0,0,102,103,5,102,0,0,
        103,104,5,108,0,0,104,105,5,111,0,0,105,106,5,97,0,0,106,107,5,116,
        0,0,107,8,1,0,0,0,108,109,5,98,0,0,109,110,5,111,0,0,110,111,5,111,
        0,0,111,112,5,108,0,0,112,10,1,0,0,0,113,114,5,43,0,0,114,12,1,0,
        0,0,115,116,5,45,0,0,116,14,1,0,0,0,117,118,5,42,0,0,118,16,1,0,
        0,0,119,120,5,47,0,0,120,18,1,0,0,0,121,122,5,37,0,0,122,20,1,0,
        0,0,123,124,5,61,0,0,124,22,1,0,0,0,125,126,5,62,0,0,126,24,1,0,
        0,0,127,128,5,60,0,0,128,26,1,0,0,0,129,130,5,61,0,0,130,131,5,61,
        0,0,131,28,1,0,0,0,132,133,5,33,0,0,133,134,5,61,0,0,134,30,1,0,
        0,0,135,136,5,62,0,0,136,137,5,61,0,0,137,32,1,0,0,0,138,139,5,60,
        0,0,139,140,5,61,0,0,140,34,1,0,0,0,141,142,5,124,0,0,142,143,5,
        124,0,0,143,36,1,0,0,0,144,145,5,38,0,0,145,146,5,38,0,0,146,38,
        1,0,0,0,147,148,5,33,0,0,148,40,1,0,0,0,149,150,5,59,0,0,150,42,
        1,0,0,0,151,152,5,44,0,0,152,44,1,0,0,0,153,154,5,40,0,0,154,46,
        1,0,0,0,155,156,5,41,0,0,156,48,1,0,0,0,157,158,5,123,0,0,158,50,
        1,0,0,0,159,160,5,125,0,0,160,52,1,0,0,0,161,162,5,91,0,0,162,54,
        1,0,0,0,163,164,5,93,0,0,164,56,1,0,0,0,165,166,5,105,0,0,166,167,
        5,110,0,0,167,168,5,112,0,0,168,169,5,117,0,0,169,170,5,116,0,0,
        170,171,5,84,0,0,171,172,5,101,0,0,172,173,5,120,0,0,173,174,5,116,
        0,0,174,58,1,0,0,0,175,176,5,115,0,0,176,177,5,104,0,0,177,178,5,
        111,0,0,178,179,5,119,0,0,179,180,5,84,0,0,180,181,5,101,0,0,181,
        182,5,120,0,0,182,183,5,116,0,0,183,60,1,0,0,0,184,185,5,100,0,0,
        185,186,5,117,0,0,186,187,5,114,0,0,187,188,5,105,0,0,188,189,5,
        110,0,0,189,190,5,103,0,0,190,62,1,0,0,0,191,192,5,119,0,0,192,193,
        5,104,0,0,193,194,5,101,0,0,194,195,5,110,0,0,195,64,1,0,0,0,196,
        197,5,101,0,0,197,198,5,108,0,0,198,199,5,115,0,0,199,200,5,101,
        0,0,200,201,5,105,0,0,201,202,5,102,0,0,202,66,1,0,0,0,203,204,5,
        105,0,0,204,205,5,102,0,0,205,68,1,0,0,0,206,207,5,101,0,0,207,208,
        5,108,0,0,208,209,5,115,0,0,209,210,5,101,0,0,210,70,1,0,0,0,211,
        213,7,0,0,0,212,211,1,0,0,0,213,214,1,0,0,0,214,212,1,0,0,0,214,
        215,1,0,0,0,215,216,1,0,0,0,216,217,6,35,0,0,217,72,1,0,0,0,218,
        219,5,47,0,0,219,220,5,47,0,0,220,224,1,0,0,0,221,223,8,1,0,0,222,
        221,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,
        227,1,0,0,0,226,224,1,0,0,0,227,228,6,36,0,0,228,74,1,0,0,0,229,
        233,5,34,0,0,230,232,8,2,0,0,231,230,1,0,0,0,232,235,1,0,0,0,233,
        231,1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,233,1,0,0,0,236,
        237,5,34,0,0,237,76,1,0,0,0,238,239,5,116,0,0,239,240,5,114,0,0,
        240,241,5,117,0,0,241,242,5,101,0,0,242,78,1,0,0,0,243,244,5,102,
        0,0,244,245,5,97,0,0,245,246,5,108,0,0,246,247,5,115,0,0,247,248,
        5,111,0,0,248,80,1,0,0,0,249,251,7,3,0,0,250,249,1,0,0,0,251,252,
        1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,82,1,0,0,0,254,256,7,
        4,0,0,255,254,1,0,0,0,256,257,1,0,0,0,257,255,1,0,0,0,257,258,1,
        0,0,0,258,84,1,0,0,0,259,261,7,4,0,0,260,259,1,0,0,0,261,264,1,0,
        0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,265,1,0,0,0,264,262,1,0,
        0,0,265,267,5,46,0,0,266,268,7,4,0,0,267,266,1,0,0,0,268,269,1,0,
        0,0,269,267,1,0,0,0,269,270,1,0,0,0,270,86,1,0,0,0,8,0,214,224,233,
        252,257,262,269,1,6,0,0
    ]

class LexerVictor(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VERSA = 1
    WORK = 2
    ENTERO = 3
    FLOTANTE = 4
    BOOLEANO = 5
    MAS = 6
    MENOS = 7
    MULTIPLICACION = 8
    DIVISION = 9
    MODULO = 10
    IGUAL = 11
    MAYOR = 12
    MENOR = 13
    IGUAL_IGUAL = 14
    DIFERENTE_QUE = 15
    MAYOR_IGUAL_QUE = 16
    MENOR_IGUAL_QUE = 17
    OR = 18
    AND = 19
    NOT = 20
    PUNTO_Y_COMA = 21
    COMA = 22
    PARENTESIS_IZQ = 23
    PARENTESIS_DER = 24
    LLAVE_IZQ = 25
    LLAVE_DER = 26
    CORCHETE_IZQ = 27
    CORCHETE_DER = 28
    INPUTTEXT = 29
    SHOWTEXT = 30
    DURING = 31
    WHEN = 32
    ELSEIF = 33
    IF = 34
    ELSE = 35
    ESPACIO = 36
    COMENTARIO = 37
    CADENA = 38
    TRUE = 39
    FALSE = 40
    IDENTIFICADOR = 41
    NUMERO_ENTERO = 42
    NUMERO_FLOTANTE = 43

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'versa'", "'work'", "'int'", "'float'", "'bool'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'='", "'>'", "'<'", "'=='", "'!='", "'>='", 
            "'<='", "'||'", "'&&'", "'!'", "';'", "','", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "'inputText'", "'showText'", "'during'", 
            "'when'", "'elseif'", "'if'", "'else'", "'true'", "'falso'" ]

    symbolicNames = [ "<INVALID>",
            "VERSA", "WORK", "ENTERO", "FLOTANTE", "BOOLEANO", "MAS", "MENOS", 
            "MULTIPLICACION", "DIVISION", "MODULO", "IGUAL", "MAYOR", "MENOR", 
            "IGUAL_IGUAL", "DIFERENTE_QUE", "MAYOR_IGUAL_QUE", "MENOR_IGUAL_QUE", 
            "OR", "AND", "NOT", "PUNTO_Y_COMA", "COMA", "PARENTESIS_IZQ", 
            "PARENTESIS_DER", "LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", 
            "CORCHETE_DER", "INPUTTEXT", "SHOWTEXT", "DURING", "WHEN", "ELSEIF", 
            "IF", "ELSE", "ESPACIO", "COMENTARIO", "CADENA", "TRUE", "FALSE", 
            "IDENTIFICADOR", "NUMERO_ENTERO", "NUMERO_FLOTANTE" ]

    ruleNames = [ "VERSA", "WORK", "ENTERO", "FLOTANTE", "BOOLEANO", "MAS", 
                  "MENOS", "MULTIPLICACION", "DIVISION", "MODULO", "IGUAL", 
                  "MAYOR", "MENOR", "IGUAL_IGUAL", "DIFERENTE_QUE", "MAYOR_IGUAL_QUE", 
                  "MENOR_IGUAL_QUE", "OR", "AND", "NOT", "PUNTO_Y_COMA", 
                  "COMA", "PARENTESIS_IZQ", "PARENTESIS_DER", "LLAVE_IZQ", 
                  "LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", "INPUTTEXT", 
                  "SHOWTEXT", "DURING", "WHEN", "ELSEIF", "IF", "ELSE", 
                  "ESPACIO", "COMENTARIO", "CADENA", "TRUE", "FALSE", "IDENTIFICADOR", 
                  "NUMERO_ENTERO", "NUMERO_FLOTANTE" ]

    grammarFileName = "LexerVictor.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

