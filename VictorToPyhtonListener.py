from antlr4 import *
from LexerVictor import LexerVictor
from ParserVictor import ParserVictor
from antlr4.error.ErrorListener import ConsoleErrorListener
from SemanticListener import SemanticListener

class VictorToPyhtonListener(ParseTreeListener):
    def __init__(self):
        self.output = ""
        self.inside_function = False
        self.asignaciones_bloque = set()

    def is_inside_block(self, ctx):
        # Verificar si el contexto actual es un hijo de un bloque
        current_ctx = ctx
        while current_ctx is not None:
            if isinstance(current_ctx, ParserVictor.BloqueContext):
                return True
            current_ctx = current_ctx.parentCtx
        return False

    def enterPrograma(self, ctx:ParserVictor.ProgramaContext):
        self.output += "# Código generado en Python\n"

    def enterDeclaracion_variable(self, ctx:ParserVictor.Declaracion_variableContext):
        if self.is_inside_block(ctx):
            self.output += f"\t"
        identificador = ctx.IDENTIFICADOR().getText()
        valor = ctx.expresion().getText()
        self.output += f"{identificador} = {valor};\n"

    def enterAsignacion(self, ctx):
        identificador = ctx.IDENTIFICADOR().getText()
        valor = ctx.expresion().getText()
        if self.is_inside_block(ctx):
            self.asignaciones_bloque.add(identificador)
        else:
            if identificador not in self.asignaciones_bloque:
                print(  self.asignaciones_bloque);
                self.output += f"{identificador} = {valor};\n"

    def enterBloque(self, ctx:ParserVictor.BloqueContext):
        # Recorrer las declaraciones dentro del bloque y realizar el reemplazo necesario
        
        for declaracion in ctx.declaraciones().declaracion():
            if isinstance(declaracion, ParserVictor.Declaracion_variableContext):
                identificador = declaracion.IDENTIFICADOR().getText()
                valor = declaracion.expresion().getText()
                self.output += f"{identificador} = {valor}\n"
            elif isinstance(declaracion, ParserVictor.ImprimirContext):
                expresion = declaracion.expresion().getText()
                self.output += f"print({expresion})\n"
        

    def exitBloque(self, ctx:ParserVictor.BloqueContext): 
        self.output += "\n"   

    def enterDeclaracion_funcion(self, ctx:ParserVictor.Declaracion_funcionContext):
        self.inside_function = True
        nombre_funcion = ctx.IDENTIFICADOR().getText()
        parametros = ", ".join([parametro.getText() for parametro in ctx.parametros().parametro()])
        bloque = ctx.bloque().getText()
        self.output += f"def  {nombre_funcion}({parametros}):\n "

    def enterImprimir(self, ctx:ParserVictor.ImprimirContext):
        if self.is_inside_block(ctx):
             self.output += f"\t"
        expresion = ctx.expresion().getText()
        self.output += f"print({expresion})\n"
            
    # Enter a parse tree produced by ParserVictor#if_statement.
    def enterIf_statement(self, ctx:ParserVictor.If_statementContext):
        if self.is_inside_block(ctx):
            self.output += f"\t"
        expresion  = ctx.expresion().getText()
        self.output += f"if { expresion}:\n \t"


    # Exit a parse tree produced by ParserVictor#if_statement.
    def exitIf_statement(self, ctx:ParserVictor.If_statementContext):
        
        self.output += "\n"

    # Enter a parse tree produced by ParserVictor#elseif_statement.
    def enterElseif_statement(self, ctx:ParserVictor.Elseif_statementContext):
        if self.is_inside_block(ctx):
            self.output += f"\t"
        expresion  = ctx.expresion().getText()
        self.output += f"elif { expresion}:\n \t"

    # Exit a parse tree produced by ParserVictor#elseif_statement.
    def exitElseif_statement(self, ctx:ParserVictor.Elseif_statementContext):
        self.output += "\n"


    def enterExpresion(self, ctx:ParserVictor.ExpresionContext):
        # No hace nada aquí para evitar agregar el ';' al final
        pass

    def exitDeclaracion_funcion(self, ctx:ParserVictor.Declaracion_funcionContext):
        self.inside_function = False
    


