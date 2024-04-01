# Generated from ParserVictor.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ParserVictor import ParserVictor
else:
    from ParserVictor import ParserVictor

# This class defines a complete listener for a parse tree produced by ParserVictor.
class ParserVictorListener(ParseTreeListener):

    # Enter a parse tree produced by ParserVictor#programa.
    def enterPrograma(self, ctx:ParserVictor.ProgramaContext):
        pass

    # Exit a parse tree produced by ParserVictor#programa.
    def exitPrograma(self, ctx:ParserVictor.ProgramaContext):
        pass


    # Enter a parse tree produced by ParserVictor#declaraciones.
    def enterDeclaraciones(self, ctx:ParserVictor.DeclaracionesContext):
        pass

    # Exit a parse tree produced by ParserVictor#declaraciones.
    def exitDeclaraciones(self, ctx:ParserVictor.DeclaracionesContext):
        pass


    # Enter a parse tree produced by ParserVictor#declaracion.
    def enterDeclaracion(self, ctx:ParserVictor.DeclaracionContext):
        pass

    # Exit a parse tree produced by ParserVictor#declaracion.
    def exitDeclaracion(self, ctx:ParserVictor.DeclaracionContext):
        pass


    # Enter a parse tree produced by ParserVictor#declaracion_variable.
    def enterDeclaracion_variable(self, ctx:ParserVictor.Declaracion_variableContext):
        pass

    # Exit a parse tree produced by ParserVictor#declaracion_variable.
    def exitDeclaracion_variable(self, ctx:ParserVictor.Declaracion_variableContext):
        pass


    # Enter a parse tree produced by ParserVictor#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx:ParserVictor.Declaracion_funcionContext):
        pass

    # Exit a parse tree produced by ParserVictor#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:ParserVictor.Declaracion_funcionContext):
        pass


    # Enter a parse tree produced by ParserVictor#imprimir.
    def enterImprimir(self, ctx:ParserVictor.ImprimirContext):
        pass

    # Exit a parse tree produced by ParserVictor#imprimir.
    def exitImprimir(self, ctx:ParserVictor.ImprimirContext):
        pass


    # Enter a parse tree produced by ParserVictor#capturar.
    def enterCapturar(self, ctx:ParserVictor.CapturarContext):
        pass

    # Exit a parse tree produced by ParserVictor#capturar.
    def exitCapturar(self, ctx:ParserVictor.CapturarContext):
        pass


    # Enter a parse tree produced by ParserVictor#parametros.
    def enterParametros(self, ctx:ParserVictor.ParametrosContext):
        pass

    # Exit a parse tree produced by ParserVictor#parametros.
    def exitParametros(self, ctx:ParserVictor.ParametrosContext):
        pass


    # Enter a parse tree produced by ParserVictor#parametro.
    def enterParametro(self, ctx:ParserVictor.ParametroContext):
        pass

    # Exit a parse tree produced by ParserVictor#parametro.
    def exitParametro(self, ctx:ParserVictor.ParametroContext):
        pass


    # Enter a parse tree produced by ParserVictor#bloque.
    def enterBloque(self, ctx:ParserVictor.BloqueContext):
        pass

    # Exit a parse tree produced by ParserVictor#bloque.
    def exitBloque(self, ctx:ParserVictor.BloqueContext):
        pass


    # Enter a parse tree produced by ParserVictor#sentencia.
    def enterSentencia(self, ctx:ParserVictor.SentenciaContext):
        pass

    # Exit a parse tree produced by ParserVictor#sentencia.
    def exitSentencia(self, ctx:ParserVictor.SentenciaContext):
        pass


    # Enter a parse tree produced by ParserVictor#if_statement.
    def enterIf_statement(self, ctx:ParserVictor.If_statementContext):
        pass

    # Exit a parse tree produced by ParserVictor#if_statement.
    def exitIf_statement(self, ctx:ParserVictor.If_statementContext):
        pass


    # Enter a parse tree produced by ParserVictor#elseif_statement.
    def enterElseif_statement(self, ctx:ParserVictor.Elseif_statementContext):
        pass

    # Exit a parse tree produced by ParserVictor#elseif_statement.
    def exitElseif_statement(self, ctx:ParserVictor.Elseif_statementContext):
        pass


    # Enter a parse tree produced by ParserVictor#while_statement.
    def enterWhile_statement(self, ctx:ParserVictor.While_statementContext):
        pass

    # Exit a parse tree produced by ParserVictor#while_statement.
    def exitWhile_statement(self, ctx:ParserVictor.While_statementContext):
        pass


    # Enter a parse tree produced by ParserVictor#for_statement.
    def enterFor_statement(self, ctx:ParserVictor.For_statementContext):
        pass

    # Exit a parse tree produced by ParserVictor#for_statement.
    def exitFor_statement(self, ctx:ParserVictor.For_statementContext):
        pass


    # Enter a parse tree produced by ParserVictor#asignacion_expresion.
    def enterAsignacion_expresion(self, ctx:ParserVictor.Asignacion_expresionContext):
        pass

    # Exit a parse tree produced by ParserVictor#asignacion_expresion.
    def exitAsignacion_expresion(self, ctx:ParserVictor.Asignacion_expresionContext):
        pass


    # Enter a parse tree produced by ParserVictor#asignacion.
    def enterAsignacion(self, ctx:ParserVictor.AsignacionContext):
        pass

    # Exit a parse tree produced by ParserVictor#asignacion.
    def exitAsignacion(self, ctx:ParserVictor.AsignacionContext):
        pass


    # Enter a parse tree produced by ParserVictor#expresion.
    def enterExpresion(self, ctx:ParserVictor.ExpresionContext):
        pass

    # Exit a parse tree produced by ParserVictor#expresion.
    def exitExpresion(self, ctx:ParserVictor.ExpresionContext):
        pass


    # Enter a parse tree produced by ParserVictor#expresion_aditiva.
    def enterExpresion_aditiva(self, ctx:ParserVictor.Expresion_aditivaContext):
        pass

    # Exit a parse tree produced by ParserVictor#expresion_aditiva.
    def exitExpresion_aditiva(self, ctx:ParserVictor.Expresion_aditivaContext):
        pass


    # Enter a parse tree produced by ParserVictor#expresion_multiplicativa.
    def enterExpresion_multiplicativa(self, ctx:ParserVictor.Expresion_multiplicativaContext):
        pass

    # Exit a parse tree produced by ParserVictor#expresion_multiplicativa.
    def exitExpresion_multiplicativa(self, ctx:ParserVictor.Expresion_multiplicativaContext):
        pass


    # Enter a parse tree produced by ParserVictor#expresion_unaria.
    def enterExpresion_unaria(self, ctx:ParserVictor.Expresion_unariaContext):
        pass

    # Exit a parse tree produced by ParserVictor#expresion_unaria.
    def exitExpresion_unaria(self, ctx:ParserVictor.Expresion_unariaContext):
        pass


    # Enter a parse tree produced by ParserVictor#expresion_primaria.
    def enterExpresion_primaria(self, ctx:ParserVictor.Expresion_primariaContext):
        pass

    # Exit a parse tree produced by ParserVictor#expresion_primaria.
    def exitExpresion_primaria(self, ctx:ParserVictor.Expresion_primariaContext):
        pass


    # Enter a parse tree produced by ParserVictor#booleano.
    def enterBooleano(self, ctx:ParserVictor.BooleanoContext):
        pass

    # Exit a parse tree produced by ParserVictor#booleano.
    def exitBooleano(self, ctx:ParserVictor.BooleanoContext):
        pass



del ParserVictor